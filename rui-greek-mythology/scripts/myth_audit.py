"""Validate the Greek myth dataset and audit it against Theoi.com.

Usage (from the project folder):
    python scripts/myth_audit.py            # validate, summarise, audit Theoi (uses cache)
    python scripts/myth_audit.py --offline  # skip Theoi; validate and summarise only
    python scripts/myth_audit.py --refresh  # re-download Theoi pages instead of using the cache

Outputs:
    output/validation_report.txt   problems found in the two CSV files
    output/theoi_audit.csv         one row per version that has a Theoi page
    output/theoi_cache/            downloaded Theoi pages (so we only fetch each page once)
"""

import argparse
import csv
import html
import re
import time
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

try:
    from rich.console import Console
    from rich.table import Table
except ImportError:  # the script still works without rich, just less pretty
    Console = None
    Table = None

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "output"
CACHE = OUT / "theoi_cache"
THEOI = "https://www.theoi.com/"

# Controlled vocabularies. Changing these is an interpretive decision, so they live
# in one place and the README explains each value.
VOCAB = {
    "transgressor_status": {"mortal", "hero", "demigod", "titan", "giant", "nymph", "satyr"},
    "source_language": {"Greek", "Latin"},
    "period": {"archaic", "classical", "hellenistic", "roman_imperial"},
    "narrative_frame": {
        "poet_narration", "character_narration", "exemplum_in_speech", "lyric_narration",
        "choral_ode", "dramatic_plot", "philosophical_argument", "mythographic_summary",
        "local_tradition",
    },
    "locus_confidence": {"high", "medium", "low"},
    "function_code": {
        "RESPECT_GODS", "MORTAL_LIMITS", "XENIA", "JUSTICE", "GRATITUDE", "SELF_RESTRAINT",
        "SEXUAL_NORMS", "KINSHIP", "GENDER_ROLES", "WORK_ETHIC", "POLITICAL_ORDER",
        "EXPLAIN_SUFFERING", "ETIOLOGY", "CONSOLATION_PERSUASION", "DIVINE_ARBITRARINESS",
    },
    "evidence_type": {"explicit_in_text", "implied_in_text", "scholarly", "compiler_inference"},
    "confidence": {"high", "medium", "low"},
    "contested": {"yes", "no"},
}

VERSION_REQUIRED = [
    "version_id", "myth_id", "myth", "figures", "transgression", "transgressor_status",
    "punisher", "punishment", "source_author", "source_work", "source_locus",
    "source_language", "approx_date", "period", "genre", "narrative_frame", "locus_confidence",
]
CLAIM_REQUIRED = ["claim_id", "version_id", "function_code", "claim", "evidence_type",
                  "interpreter", "confidence", "contested"]

# How Theoi names the works we cite (Theoi often uses Latin or Greek titles).
WORK_ALIASES = {
    "Library": ["Bibliotheca", "Library"],
    "Library (Epitome)": ["Bibliotheca E", "Epitome", "Bibliotheca"],
    "Olympian 1": ["Olympian Ode 1", "Olympian 1"],
    "Pythian 2": ["Pythian Ode 2", "Pythian 2"],
    "Pythian 3": ["Pythian Ode 3", "Pythian 3"],
    "Isthmian 7": ["Isthmian Ode 7", "Isthmian 7"],
    "Ode 11": ["Fragment 11", "Ode 11", "Epinician 11"],
    "Hymn 6 (to Demeter)": ["Hymn 6", "Hymn to Demeter"],
    "Description of Greece": ["Description of Greece", "Guide to Greece"],
    "Histories": ["Histories"],
    "Oedipus Tyrannus": ["Oedipus the King", "Oedipus Tyrannus", "Oedipus Rex"],
}
AUTHOR_ALIASES = {
    "Apollodorus": ["Pseudo-Apollodorus", "Apollodorus"],
    "[Aeschylus]": ["Aeschylus"],
    "Antoninus Liberalis": ["Antoninus Liberalis"],
}

# The name each figure goes by on Theoi (Greek spellings), used to check whether the
# page actually discusses this myth and not just links to it from the menu.
THEOI_NAMES = {
    "M01": ["Prometheus"], "M02": ["Pandora"], "M05": ["Tityos"], "M07": ["Niobe"],
    "M08": ["Arakhne", "Arachne"], "M09": ["Lykaon", "Lycaon"], "M11": ["Polyphemos"],
    "M14": ["Aktaion", "Actaeon"], "M15": ["Pentheus"], "M16": ["Lykourgos"],
    "M17": ["Bellerophon"], "M18": ["Phaethon"], "M20": ["Marsyas"], "M21": ["Midas"],
    "M22": ["Salmoneus"], "M23": ["Aias", "Ajax"], "M25": ["Agamemnon"],
    "M26": ["Asklepios", "Asclepius"], "M27": ["Koronis", "Coronis"],
    "M28": ["Hippolytos", "Hippolytus"], "M30": ["Orion"], "M31": ["Erysikhthon"],
    "M32": ["Kassiepeia", "Cassiopeia", "Cassiope", "Cassiepi"], "M33": ["Oineus", "Meleagros"],
    "M36": ["Aloadai", "Otos", "Ephialtes"], "M37": ["cattle", "Kine", "kine"],
    "M39": ["Minos"], "M40": ["Admetos", "Admetus"], "M42": ["Io "], "M43": ["Kallisto"],
    "M44": ["Narkissos"], "M45": ["Minyad"], "M46": ["Proitid", "Proetid", "Proitos"],
    "M49": ["Aglauros"],
}


def read_csv(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate(versions, claims):
    """Return a list of human-readable problems. An empty list means the data is clean."""
    problems = []
    seen = set()
    for i, row in enumerate(versions, start=2):  # row 1 is the header
        vid = row.get("version_id", "?")
        for field in VERSION_REQUIRED:
            if not (row.get(field) or "").strip():
                problems.append(f"myth_versions.csv line {i} ({vid}): '{field}' is empty")
        if vid in seen:
            problems.append(f"myth_versions.csv line {i}: duplicate version_id {vid}")
        seen.add(vid)
        for field in ("transgressor_status", "source_language", "period",
                      "narrative_frame", "locus_confidence"):
            if row.get(field) and row[field] not in VOCAB[field]:
                problems.append(f"myth_versions.csv line {i} ({vid}): '{row[field]}' "
                                f"is not an allowed {field}")
    claim_ids = set()
    for i, row in enumerate(claims, start=2):
        cid = row.get("claim_id", "?")
        for field in CLAIM_REQUIRED:
            if not (row.get(field) or "").strip():
                problems.append(f"function_claims.csv line {i} ({cid}): '{field}' is empty")
        if cid in claim_ids:
            problems.append(f"function_claims.csv line {i}: duplicate claim_id {cid}")
        claim_ids.add(cid)
        if row.get("version_id") not in seen:
            problems.append(f"function_claims.csv line {i} ({cid}): version "
                            f"{row.get('version_id')} does not exist")
        for field in ("function_code", "evidence_type", "confidence", "contested"):
            if row.get(field) and row[field] not in VOCAB[field]:
                problems.append(f"function_claims.csv line {i} ({cid}): '{row[field]}' "
                                f"is not an allowed {field}")
        if row.get("evidence_type") in ("explicit_in_text", "implied_in_text", "scholarly") \
                and not (row.get("evidence_locus") or "").strip():
            problems.append(f"function_claims.csv line {i} ({cid}): evidence_type is "
                            f"{row['evidence_type']} but no evidence_locus is given")
        if row.get("contested") == "yes" and not (row.get("alternative_reading") or "").strip():
            problems.append(f"function_claims.csv line {i} ({cid}): marked contested "
                            f"but no alternative_reading")
    without_claims = seen - {c["version_id"] for c in claims}
    for vid in sorted(without_claims):
        problems.append(f"{vid} has no function claims")
    return problems


def fetch(page, refresh=False):
    """Download a Theoi page once and keep a local copy."""
    CACHE.mkdir(parents=True, exist_ok=True)
    local = CACHE / page.replace("/", "__")
    if local.exists() and not refresh:
        return local.read_text(encoding="utf-8")
    req = urllib.request.Request(THEOI + page, headers={"User-Agent": "Mozilla/5.0 (IS310 class project)"})
    try:
        text = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
    except Exception as err:  # 404s and timeouts are audit findings, not crashes
        return f"__ERROR__ {err}"
    local.write_text(text, encoding="utf-8")
    time.sleep(1)  # be polite to a small volunteer-run site
    return text


def page_text(raw):
    raw = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", raw)
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", raw)))


def first_numbers(locus):
    """'24.602–617' -> (24, 602); '507–616' -> (None, 507); '320c–322d' -> (None, 320)."""
    nums = [int(n) for n in re.findall(r"\d+", locus or "")]
    if "." in (locus or "") and len(nums) >= 2:
        return nums[0], nums[1]
    return (None, nums[0]) if nums else (None, None)


def audit_version(row, text):
    """Does Theoi cite the same author and work, near the same lines?"""
    authors = AUTHOR_ALIASES.get(row["source_author"], [row["source_author"]])
    works = WORK_ALIASES.get(row["source_work"], [row["source_work"]])
    cites = []
    for a in authors:
        for w in works:
            pattern = re.escape(a) + r"[^.;]{0,40}?" + re.escape(w) + r"\s*([\d.\s,a-e]{0,25})"
            cites += re.findall(pattern, text)
    author_cited = any(a in text for a in authors)
    book, line = first_numbers(row["source_locus"])
    locus_match = False
    for c in cites:
        nums = [int(n) for n in re.findall(r"\d+", c)]
        if not nums or line is None:
            continue
        if book is not None and len(nums) >= 2:
            locus_match |= nums[0] == book and abs(nums[1] - line) <= 40
        elif book is None:
            locus_match |= abs(nums[0] - line) <= 40
    names = THEOI_NAMES.get(row["myth_id"], [row["myth"]])
    mentions = sum(text.count(n) for n in names)
    return {
        "author_cited": "yes" if author_cited else "no",
        "work_cited": "yes" if cites else "no",
        "locus_match": "yes" if locus_match else ("n/a" if not cites else "no"),
        "myth_mentions": mentions,
        "cited_as": " | ".join(sorted({c.strip() for c in cites}))[:120],
    }


def show(console, title, columns, rows):
    if console:
        t = Table(title=title)
        for c in columns:
            t.add_column(c)
        for r in rows:
            t.add_row(*[str(x) for x in r])
        console.print(t)
    else:
        print(f"\n== {title} ==")
        print(" | ".join(columns))
        for r in rows:
            print(" | ".join(str(x) for x in r))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="skip the Theoi audit")
    ap.add_argument("--refresh", action="store_true", help="re-download Theoi pages")
    args = ap.parse_args()
    console = Console() if Console else None
    OUT.mkdir(exist_ok=True)

    versions, claims = read_csv("myth_versions.csv"), read_csv("function_claims.csv")

    problems = validate(versions, claims)
    (OUT / "validation_report.txt").write_text(
        "\n".join(problems) if problems else "No problems found.\n", encoding="utf-8")
    print(f"Validation: {len(problems)} problem(s). See output/validation_report.txt")
    for p in problems[:15]:
        print("  -", p)

    myths = {v["myth_id"] for v in versions}
    print(f"\n{len(versions)} versions of {len(myths)} myths; {len(claims)} function claims.")

    show(console, "Versions by period and language", ["period", "Greek", "Latin"],
         [(p, sum(v["period"] == p and v["source_language"] == "Greek" for v in versions),
           sum(v["period"] == p and v["source_language"] == "Latin" for v in versions))
          for p in ["archaic", "classical", "hellenistic", "roman_imperial"]])

    show(console, "How the source uses the story (narrative_frame)", ["frame", "versions"],
         Counter(v["narrative_frame"] for v in versions).most_common())

    by_code = defaultdict(Counter)
    for c in claims:
        by_code[c["function_code"]][c["evidence_type"]] += 1
    show(console, "What the stories are claimed to teach, by kind of evidence",
         ["function", "explicit", "implied", "scholarly", "my inference", "total"],
         sorted(((k, v["explicit_in_text"], v["implied_in_text"], v["scholarly"],
                  v["compiler_inference"], sum(v.values())) for k, v in by_code.items()),
                key=lambda r: -r[-1]))

    # Same myth, different uses: the core question of the dataset.
    codes_by_version = defaultdict(set)
    for c in claims:
        codes_by_version[c["version_id"]].add(c["function_code"])
    multi = []
    for mid in sorted(myths):
        vs = [v for v in versions if v["myth_id"] == mid]
        if len(vs) > 1:
            multi.append((vs[0]["myth"], len(vs),
                          ", ".join(sorted({v["narrative_frame"] for v in vs})),
                          ", ".join(sorted(set().union(*(codes_by_version[v["version_id"]] for v in vs))))))
    show(console, "Myths told in more than one source", ["myth", "versions", "frames", "functions"], multi)

    contested = sum(c["contested"] == "yes" for c in claims)
    print(f"\nContested claims: {contested} of {len(claims)}. "
          f"Claims resting only on my own inference: "
          f"{sum(c['evidence_type'] == 'compiler_inference' for c in claims)}.")

    if args.offline:
        return

    audit_rows = []
    no_page = [v for v in versions if not v.get("theoi_page")]
    for v in versions:
        if not v.get("theoi_page"):
            continue
        raw = fetch(v["theoi_page"], refresh=args.refresh)
        if raw.startswith("__ERROR__"):
            result = {"author_cited": "", "work_cited": "", "locus_match": "",
                      "myth_mentions": 0, "cited_as": raw}
        else:
            result = audit_version(v, page_text(raw))
        audit_rows.append({"version_id": v["version_id"], "myth": v["myth"],
                           "source": f"{v['source_author']}, {v['source_work']} {v['source_locus']}",
                           "theoi_page": v["theoi_page"], **result})

    with open(OUT / "theoi_audit.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(audit_rows[0].keys()))
        w.writeheader()
        w.writerows(audit_rows)

    show(console, "Theoi audit (does Theoi cite the same ancient source?)",
         ["version", "myth", "source", "author", "work", "lines", "mentions"],
         [(r["version_id"], r["myth"], r["source"], r["author_cited"], r["work_cited"],
           r["locus_match"], r["myth_mentions"]) for r in audit_rows])
    n = len(audit_rows)
    print(f"\nTheoi coverage: {n} of {len(versions)} versions have a Theoi page I could link; "
          f"{len(no_page)} have none.")
    print(f"Theoi cites the same work for {sum(r['work_cited'] == 'yes' for r in audit_rows)} of {n}; "
          f"near the same lines for {sum(r['locus_match'] == 'yes' for r in audit_rows)} of {n}.")
    print("Myths with no Theoi page: " + ", ".join(sorted({v['myth'] for v in no_page})))
    print("Full results: output/theoi_audit.csv")


if __name__ == "__main__":
    main()
