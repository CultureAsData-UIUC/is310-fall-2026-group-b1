
import pandas as pd
import shutil
import re
from pathlib import Path
from datetime import datetime

CSV_FILE = Path("fairytale_dataset.csv")

# The five selected tales and their Fairytalez popularity ranks
RANKS = {
    "Rapunzel": 2,
    "Cinderella": 3,
    "Baba Yaga": 20,
    "The Wild Swans": 85,
    "The Pied Piper of Hamelin": 79,
}

# All 27 new books
books = [
    # RAPUNZEL — 10
    ("Rapunzel", "Kingdom of Locks", "Deborah Grace White", 2021, "Direct retelling"),
    ("Rapunzel", "Rapunzel", "Barbara Rogasky", 1982, "Direct retelling"),
    ("Rapunzel", "Golden Curse", "M. Lynn", 2019, "Direct retelling"),
    ("Rapunzel", "Entangled", "Mila Young", 2018, "Direct retelling"),
    ("Rapunzel", "The Abandoned Princess", "Melanie Cellier", 2023, "Direct retelling"),
    ("Rapunzel", "Braids of Silver", "Laura Greenwood", 2020, "Direct retelling"),
    ("Rapunzel", "Tower of Thorns", "Laura Greenwood", 2020, "Direct retelling"),
    ("Rapunzel", "Turret", "Camille Peters", 2021, "Direct retelling"),
    ("Rapunzel", "Rootbound", "Margaret Owen", 2026, "Continuation"),
    ("Rapunzel", "Golden", "Cameron Dokey", 2006, "Direct retelling"),

    # CINDERELLA — 8
    ("Cinderella", "The Glass Gate", "Hanna Sandvig", None, "Direct retelling"),
    ("Cinderella", "Ellie and the Prince", "J.M. Stengl", None, "Loose retelling"),
    ("Cinderella", "The Mystery Princess", "Melanie Cellier", None, "Direct retelling"),
    ("Cinderella", "The Peasant's Dream", "Melanie Dickerson", None, "Direct retelling"),
    ("Cinderella", "Kingdom of Cinders", "Deborah Grace White", 2021, "Direct retelling"),
    ("Cinderella", "Pumpkins and Proms", "Laura Greenwood", 2020, "Direct retelling"),
    ("Cinderella", "A Curse of Ash and Iron", "Christine Norris", 2014, "Direct retelling"),
    ("Cinderella", "Ever After", "Wendy Loggia", 1998, "Direct retelling"),

    # BABA YAGA — 7
    ("Baba Yaga", "Egg & Spoon", "Gregory Maguire", 2014, "Folklore-inspired"),
    ("Baba Yaga", "Baba Yaga's Assistant", "Marika McCoola", 2015, "Folklore-inspired"),
    ("Baba Yaga", "Baba Yaga and Vasilisa the Brave", "Marianna Mayer", 1994, "Direct retelling"),
    ("Baba Yaga", "Finding Baba Yaga", "Jane Yolen", 2018, "Loose retelling"),
    ("Baba Yaga", "The Witch and the Tsar", "Olesya Salnikova Gilmore", 2022, "Folklore-inspired"),
    ("Baba Yaga", "Baba Yaga Laid an Egg", "Dubravka Ugrešić", 2008, "Folklore-inspired"),
    ("Baba Yaga", "Thistlefoot", "GennaRose Nethercott", 2022, "Folklore-inspired"),

    # THE PIED PIPER — 2
    ("The Pied Piper of Hamelin", "To Sway a Swindler", "Megan Charlie", 2025, "Direct retelling"),
    ("The Pied Piper of Hamelin", "A Fable of Riddles and Redemption", "Sara Farnsworth", 2026, "Multi-tale adaptation"),
]

COLUMNS = [
    "adaptation_id",
    "original_tale",
    "fairytale_rank",
    "book_title",
    "author",
    "publication_year",
    "medium",
    "setting",
    "character_changes",
    "protagonist_agency",
    "major_themes",
    "original_message",
    "adapted_message",
    "source_url",
    "retelling_type",
]


def normalize(value):
    if pd.isna(value):
        return ""
    return str(value).strip().casefold()


def main():
    if not CSV_FILE.exists():
        print("ERROR: fairytale_dataset.csv was not found.")
        return

    data = pd.read_csv(CSV_FILE)

    # Support either spelling if an earlier script created that column.
    if "fairytale_rank" not in data.columns and "fairytalez_rank" in data.columns:
        data = data.rename(columns={"fairytalez_rank": "fairytale_rank"})

    # Preserve the existing dataset's columns and add any missing schema columns.
    for column in COLUMNS:
        if column not in data.columns:
            data[column] = ""

    # Remove the title the user explicitly excluded.
    excluded = data["book_title"].apply(normalize) == "cinders of glass"
    removed_count = int(excluded.sum())
    data = data.loc[~excluded].copy()

    existing_titles = {
        normalize(title) for title in data["book_title"].dropna()
    }

    # Determine next adaptation ID.
    used_ids = []
    for value in data["adaptation_id"].dropna():
        match = re.fullmatch(r"A(\d+)", str(value).strip())
        if match:
            used_ids.append(int(match.group(1)))

    next_id = max(used_ids, default=0) + 1
    additions = []

    for tale, title, author, year, retelling_type in books:
        if normalize(title) in existing_titles:
            print(f"Already present; skipped: {title}")
            continue

        record = {column: "" for column in COLUMNS}
        record.update({
            "adaptation_id": f"A{next_id:03d}",
            "original_tale": tale,
            "fairytale_rank": RANKS[tale],
            "book_title": title,
            "author": author,
            "publication_year": year if year is not None else "",
            "medium": "Book",
            "retelling_type": retelling_type,
        })

        additions.append(record)
        existing_titles.add(normalize(title))
        next_id += 1

    if not additions and removed_count == 0:
        print("No changes needed. All these titles are already present.")
        return

    # Back up the original CSV before saving changes.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = Path(f"fairytale_dataset_backup_{timestamp}.csv")
    shutil.copy2(CSV_FILE, backup)

    updated = pd.concat(
        [data, pd.DataFrame(additions, columns=COLUMNS)],
        ignore_index=True
    )

    updated = updated.reindex(columns=COLUMNS)
    updated.to_csv(CSV_FILE, index=False)

    print("\n--- UPDATE COMPLETE ---")
    print(f"New books added: {len(additions)}")
    print(f"Excluded Cinders of Glass removed: {removed_count}")
    print(f"Total records now: {len(updated)}")
    print(f"Backup: {backup}")

    print("\n--- COUNTS BY FAIRY TALE ---")
    print(updated["original_tale"].value_counts().to_string())

    print("\n--- BOOKS STILL NEEDING INFORMATION ---")
    required_fields = [
        "author", "publication_year", "setting",
        "character_changes", "protagonist_agency",
        "major_themes", "original_message",
        "adapted_message", "source_url", "retelling_type"
    ]

    for field in required_fields:
        missing = updated[field].isna() | (
            updated[field].astype(str).str.strip() == ""
        )
        if missing.any():
            print(f"{field}: {int(missing.sum())} missing")

    print("\nUpdated CSV saved successfully.")


if __name__ == "__main__":
    main()
