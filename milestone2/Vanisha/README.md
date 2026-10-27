# Milestone 2 — Jinn and supernatural encounters in folklore

## Research approach

This is an initial **custom-created, manually interpreted dataset**, not an automatically scraped dataset. The `motif_code` and `supernatural_role` fields are working classifications made for this project. They are **not** claims about the meanings assigned by every member of a cultural community. The `cultural_meaning` field is intentionally empty until an interpretation can be attributed to a named scholar or other identifiable source.

## Computational work

`analyze.py` uses Python's built-in `csv` and `collections` modules. It checks required columns, duplicate IDs, missing required fields, and allowed yes/no values, then counts events by story section, motif, role, and actor. The script is reproducible and does not require a GUI. It does not validate historical or literary accuracy, which requires returning to the source passages.

## Limits and next steps

This initial dataset overrepresents one story section, contains many non-jinn events that supply context, and depends on an English adaptation. Its line references were inherited from a web-extracted version of the Gutenberg HTML and need a final source check; they should not be treated as permanent page numbers. The next step is to check the 60 events directly against the edition, consolidate overlapping motif labels, and add independently documented versions from another tradition before claiming cross-cultural differences.
