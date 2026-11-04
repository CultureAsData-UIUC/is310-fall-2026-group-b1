# Greek Myths as Teaching Tools: Divine Punishment Stories (Milestone 2)

**Rui Yang · IS 310 Culture As Data · Fall 2026 · Group B1 (folklore and legends)**

## 1. What this dataset is

Greek myths are usually collected as stories: who did what to whom. This dataset records **what a story was used to do**, and **where that interpretation comes from**.

Following the Milestone 1 feedback, I narrowed my topic from "the social functions of Greek myth" to one aspect: **myths of mortals (and a few immortals) who cross a line and are punished by the gods**. These are the stories most often described as teaching tools. I want to test that description against the sources.

**Research question:** When ancient authors tell a punishment myth, what do they use it to teach, and is it the same lesson each time the story is retold?

## 2. Unit of analysis and boundaries

- **One row = one version of a myth in one specific ancient source.** Niobe in Homer's *Iliad* and Niobe in Ovid's *Metamorphoses* are two rows. I chose this unit because the same myth is often used for different purposes in different texts. A myth-level row would hide that.
- **Interpretations are kept in a separate table** (`function_claims.csv`). One version can carry several claims, and claims can disagree. This follows the feedback to separate evidence from interpretation and to allow more than one reading.
- **Time and language:** Greek sources from Homer (c. 750–700 BCE) to the mythographers of the Roman Empire (1st–3rd c. CE). Sixteen Latin versions (Ovid and Virgil) are included and **marked as Roman reception**. For several myths, such as Arachne and Baucis and Philemon, Ovid is the earliest full telling to survive.
- **Size:** 72 versions of 50 myths, with 111 function claims.

## 3. Files

| File | What it is |
|---|---|
| `data/myth_versions.csv` | The dataset: one row per version of a myth in a source |
| `data/function_claims.csv` | What each version is claimed to teach, and the evidence for each claim |
| `scripts/myth_audit.py` | Validates the data, summarises it, and audits it against Theoi.com |
| `output/validation_report.txt` | Problems the script found in the data (currently none) |
| `output/theoi_audit.csv` | Audit results: does Theoi cite the same ancient source? |
| `output/theoi_cache/` | Saved copies of the Theoi pages used in the audit |

## 4. Fields

### `myth_versions.csv`

| Field | Meaning |
|---|---|
| `version_id` | Unique ID (V001…) |
| `myth_id`, `myth` | Groups versions of the same myth (M01…) |
| `figures` | Main characters, separated by `;` |
| `transgression` | What the person did wrong *according to this source*. "Not stated" is recorded when the source gives no crime. |
| `transgressor_status` | mortal, hero, demigod, titan, giant, nymph, or satyr |
| `punisher`, `punishment` | Who punishes and how, according to this source |
| `source_author`, `source_work`, `source_locus` | Where the version is found. Square brackets, as in [Aeschylus], mean disputed authorship. |
| `source_language`, `approx_date`, `period` | Greek or Latin; approximate date; one of archaic, classical, hellenistic, roman_imperial |
| `genre` | The kind of text (epic, tragedy, epinician lyric, mythography…) |
| `narrative_frame` | **How the source uses the story** (see below) |
| `locus_confidence` | How sure I am of the line numbers. "Medium" ones still need checking against a printed edition. |
| `theoi_page` | The matching Theoi.com page, if one exists |
| `notes` | Anything that doesn't fit the columns |

**`narrative_frame` values:**
- `poet_narration`: the poet tells the story directly.
- `character_narration`: a character tells it, with no clear persuasive aim.
- `exemplum_in_speech`: a character tells it **to make someone do or believe something**.
- `lyric_narration`: told inside a victory ode or other lyric poem.
- `choral_ode`: sung by a tragic chorus.
- `dramatic_plot`: the story is the plot of a play.
- `philosophical_argument`: used as part of an argument.
- `mythographic_summary`: a handbook summary.
- `local_tradition`: tied to a place, landmark, or cult.

### `function_claims.csv`

| Field | Meaning |
|---|---|
| `function_code` | What the story is claimed to teach or do (codebook below) |
| `claim` | The claim in one sentence |
| `evidence_type` | `explicit_in_text` (the source says it), `implied_in_text` (the plot clearly suggests it), `scholarly` (a published interpretation), or `compiler_inference` (my own reading) |
| `evidence_locus` | Where the evidence is |
| `interpreter` | Whose interpretation this is |
| `confidence` | high, medium, or low |
| `contested`, `alternative_reading` | Whether the claim can reasonably be read another way, and how |

**Function codebook:**
- `RESPECT_GODS`: honour the gods; don't neglect sacrifice or rites.
- `MORTAL_LIMITS`: don't compete with or imitate the gods.
- `XENIA`: hospitality between guest and host.
- `JUSTICE`: fair dealing, keeping agreements.
- `GRATITUDE`: repay benefactors.
- `SELF_RESTRAINT`: moderation of appetite, greed, or recklessness.
- `SEXUAL_NORMS`: sexual and marital conduct.
- `KINSHIP`: duties within the family.
- `GENDER_ROLES`: claims about what women or men are.
- `WORK_ETHIC`: the need for labour.
- `POLITICAL_ORDER`: how communities and rulers should work.
- `EXPLAIN_SUFFERING`: why humans suffer.
- `ETIOLOGY`: explains a rite, place, landmark, animal, or natural feature.
- `CONSOLATION_PERSUASION`: used to comfort or persuade a listener.
- `DIVINE_ARBITRARINESS`: the story presents the gods as unfair. This code records the counter-reading, so that "teaching tool" doesn't become the only possible answer.

## 5. From cultural material to data

**Step 1: from stories to a working representation.** I started with the myths and the sources that tell them, read in English translation. For each version I noted the plot, who tells the story, to whom, and why. Already at this stage I was making choices:
- what counts as "the" transgression when a source gives none (Homer's Tantalus and Sisyphus)
- whether a victim like Io belongs in a "punishment" dataset at all
- how to treat a source that gives two competing versions (Apollodorus on Actaeon)

**Step 2: from that representation to structured data.**
- **Free-text columns** keep the story's own terms: transgression, punishment, figures.
- **Controlled vocabularies** make the data comparable: `narrative_frame`, `period`, `function_code`. Every controlled value is defined in the codebook above and checked by the script.
- **Interpretations go in their own table**, each with its evidence type and an alternative reading where one exists. A single "purpose" column would have forced one meaning per story.

## 6. Inclusion and exclusion decisions

- **Included:** stories where a figure is punished, or is harmed in a way the source frames as punishment, by a god or by divine order.
- **Included as boundary cases:** Icarus (no god punishes him), Io and Callisto (victims rather than wrongdoers), and Ovid's Ceyx and Alcyone (the same couple with no crime). They show where the category breaks down.
- **Included as a philosophical use:** Plato's Myth of Er and Protagoras' Prometheus story.
- **Excluded:**
  - historical anecdotes, such as Croesus in Herodotus
  - punishments of gods by gods, such as the Titans, because they are about cosmic order rather than human conduct
  - versions known only from brief allusions
  - fragmentary plays, such as Sophocles' *Tereus* and Euripides' *Phaethon*: there isn't enough text to judge how the story was used
- **Translations:** all reading was done in English translation. The line numbers follow the standard numbering of the Greek and Latin texts.

## 7. Computational process

`scripts/myth_audit.py` is a Python script. It needs no extra packages; if `rich` is installed, it prints tables with it.

```bash
python scripts/myth_audit.py            # validate + summarise + Theoi audit
python scripts/myth_audit.py --offline  # validate + summarise only
```

It does three things:
1. **Validates** both files. It checks required fields, allowed values, unique IDs, and that every claim links to a real version. It also checks that any claim marked `explicit_in_text` gives a line reference, and that every `contested` claim gives an alternative reading. This keeps my own rules honest.
2. **Summarises** the data:
   - versions by period and language
   - how sources use the stories
   - which functions are supported by explicit evidence versus my inference
   - the myths told in more than one source, with their different frames and functions
3. **Audits Theoi.com.** For each version linked to a Theoi page, it downloads the page once (cached, with a pause between requests). It then checks whether Theoi cites the same author and work, near the same line numbers. It also counts how often the myth's figure is named on the page, using Theoi's Greek spellings.

**Limitations:**
- The citation check is a text pattern match. Theoi numbers some works differently, so a "no" means "check by hand", not "Theoi is wrong".
- Name counts include menu links, so a count of 1–2 usually means the page barely discusses the myth.

### First results

- The validation finds no problems.
- **Periods:** 21 versions are archaic, 19 classical, 1 hellenistic, and 31 Roman imperial (15 in Greek, 16 in Latin).
- **Evidence:** Of 111 claims, 84 are stated outright in the source, 7 rest only on my own inference, and 16 are marked contested.
- **Most common lessons:** respect the gods (19 claims) and know your mortal limits (23). But 12 claims record a source presenting the gods as unfair. The "teaching tool" reading is common, but it isn't the only one the ancient texts support.
- **Same myth, different jobs:**
  - Niobe is a warning in Ovid but a **consolation** in the *Iliad*.
  - Actaeon is a warning in Euripides, but Ovid calls his fault **bad luck, not crime**.
  - Prometheus is about sacrifice in Hesiod, tyranny in *Prometheus Bound*, and democratic politics in Plato.
- **Theoi coverage:**
  - 52 of 72 versions could be linked to a Theoi page. Theoi cites the same work for 48 of those and near the same lines for 41.
  - 16 myths have no Theoi page I could find, including Tantalus, Sisyphus, Ixion, Oedipus, and the Myth of Er.
  - Theoi is organised around divine beings. Mortal wrongdoers often appear only on the punishing god's "Wrath" page, or not at all.

## 8. Audit and connection plan

**What I'm auditing: Theoi Greek Mythology (theoi.com).**
- Theoi is a large, widely used site that organises mythology by god and creature, and quotes ancient sources in translation under each entry.
- My instructor suggested it, and it is far larger than my dataset.
- Britannica, which I proposed in Milestone 1, stays as a secondary comparison: it describes itself as not offering interpretation, which is itself relevant.
- DigiMyth (Sapienza University of Rome) is a second option if I need a more scholarly, structured source.

**How it connects:** both datasets cite the same ancient passages, so I can line my rows up against Theoi's citations passage by passage.

**What I plan to investigate:**
1. **Coverage:** which punishment myths and which versions Theoi includes or leaves out, and whether mortal and female figures are left out more often.
2. **Classification:** Theoi files stories under the god who punishes, such as "Wrath of Artemis". My dataset files them by what the story is used to teach. What does each way of classifying hide?
3. **Interpretation:** Theoi mostly quotes sources without saying what a story meant. Where it does comment, I'll compare that with my evidence-coded claims.

**Scaling up after this milestone:**
- **Option 1:** Extend the script to read every Theoi "Wrath" and "Punishment in Hades" page and extract all quoted citations automatically. That could produce 500–1,000 citation records. I would then classify their narrative frame with keyword rules and hand-check a sample. The hard part is that the most interesting fields, `narrative_frame` and `function_code`, are interpretive. Automating them will flatten exactly the complexity this dataset is meant to keep.
- **Option 2:** Merge my 72 hand-coded versions with Theoi's citations, and use my rows as a "gold standard" to measure what an automatic approach gets wrong.

## 9. Reflection

When I started this project, I wanted to explore the social functions of Greek myths in general, but after the feedback from Milestone 1, I decided to focus on myths involving punishment by the gods. I think this made the project more focused and easier to analyze. One thing I found interesting was that the same myth could have different meanings depending on the source. For example, Niobe is a warning in Ovid, but her story in the Iliad is more about consolation. This made me realize that myths do not always teach one specific lesson, and their meaning can change depending on the context. I also think the one-row-per-version approach worked well because it allowed me to compare different versions without treating them as having the same meaning. However, deciding how to classify some myths was difficult, especially when the characters were victims rather than people who had done something wrong.
For the next stage, I would consider adjusting the function codebook because some stories can fit into multiple categories, and their meanings are not always clear. I would keep the Latin sources because they provide useful comparisons, but I would make sure to distinguish Roman reception from Greek traditions. I also think Theoi is a useful starting point for checking sources, although it does not cover every version in my dataset. The most important thing I learned is that turning cultural material into data requires making decisions about what to include and how to interpret it. The script can check the structure and identify problems, but it cannot fully decide what a myth means. That still requires reading the sources and understanding their context.

## 10. Scholarly sources

> These short explanations are a starting point; rewrite them in your own words and add page numbers once you've read the relevant sections.

1. **"V. Mythology." *New Surveys in the Classics* 46 (2016): 64–78.** This survey treats myth as part of Greek religion rather than as entertainment. That is the basis for my `RESPECT_GODS` and `ETIOLOGY` codes, and for recording when a story is tied to a rite or cult.
2. **Detienne, Marcel, and Jean-Pierre Vernant, eds. *The Cuisine of Sacrifice among the Greeks*. Trans. Paula Wissing. University of Chicago Press, 1989.** Vernant's essay reads Hesiod's Prometheus story as the founding story of Greek animal sacrifice. It's the source of claim C002, and an example of a myth "doing" something for a community beyond teaching a moral.
3. **Buxton, Richard. *Imaginary Greece: The Contexts of Mythology*. Cambridge University Press, 1994.** Buxton argues that Greek myths must be understood through the settings in which they were told: the household, festivals, the theatre, and so on. That is the idea behind my `narrative_frame` field and my one-row-per-version design.

## 11. Things still to verify

- Line numbers marked `medium` in `locus_confidence`, and claims marked `medium` or `low` confidence, should be checked against a translation, such as the Loeb Classical Library or the Perseus Digital Library.
- Theoi's `Titan/Phaethon.html` page may describe a different Phaethon than Ovid's son of the Sun.

## 12. AI use statement

Claude proposed the narrowed scope and data structure, drafted the 72 dataset rows and 111 function claims from its own knowledge of the ancient sources, wrote myth_audit.py, and drafted sections 1–8, 10 and 11 of this README. 
