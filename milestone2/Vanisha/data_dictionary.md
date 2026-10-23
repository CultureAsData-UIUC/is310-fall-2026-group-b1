# Data dictionary

**Row definition:** one narrative event from a documented story section in Andrew Lang's 1898 English adaptation. Blank cells mean 'not established or not recorded,' not necessarily 'none.'

| Field | Meaning |
|---|---|
| `record_id` | Unique row identifier, e.g. JN001 |
| `story_title` | Story-section label within this edition |
| `source_collection` | Title of the literary collection |
| `editor` | Editor credited for this adaptation |
| `edition_year` | Year of the cited edition, not the tale's original creation date |
| `source_language` | Language and translation pathway of this edition |
| `tradition_attribution` | Cautious description of the collection's literary tradition |
| `unit_of_analysis` | What one row represents |
| `passage_line` | Locator from a web-extracted source, not a stable printed line number |
| `event_summary` | Short researcher-written paraphrase of an event |
| `motif_code` | Detailed researcher-assigned event label; categories are provisional |
| `actor_type` | Main actor category: `human`, `genius`, `human_magician`, or `transformed_human` |
| `supernatural_role` | Researcher-assigned role: `threat`, `helper`, `mixed`, `victim`, or `none` |
| `jinn_explicit` | `yes` when the coded event explicitly involves the genius/jinn figure; otherwise `no` |
| `source_url` | Link to the source edition |
| `source_evidence` | Source locator note for follow-up verification |
| `verification` | Recorded collection-time verification status, not an independent guarantee |
| `interpretation_by` | Attribution for a proposed interpretation, currently researcher coding |
| `cultural_meaning` | Intentionally blank until a specific attributed interpretation is sourced |
| `limitation` | Caveats about the row and sampling |

## Category decisions

`motif_code` has many fine-grained labels such as `mercy_request`, `conditional_mercy`, and `transformation`. These are **working codes**, not a validated cross-cultural motif system. They are appropriate for exploring the text but need a more consistent codebook before broader comparison. `supernatural_role` is also simplified: the same figure can change roles within a story. `jinn_explicit` separates jinn events from other kinds of magic.

## Sampling warning

The dataset has 60 rows across three story sections, heavily weighted toward the first two. It should not be used to estimate the prevalence of motifs across cultures, languages, or even *The Arabian Nights* as a whole.
