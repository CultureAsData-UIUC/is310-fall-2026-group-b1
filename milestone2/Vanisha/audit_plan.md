# Audit and comparison plan

## Existing collection

I plan to compare my custom motif labels with the **Berezkin and Duvakin Catalogue of Folklore and Mythological Motifs**, a comparative folklore motif catalogue. Starting point: https://www.ruthenia.ru/folklore/berezkin/ and an English browsing interface often linked at https://folkloredatabase.com/db_browse.php . I will check access, metadata, citation requirements, and the catalogue's own descriptions before extracting records.

## How it connects to my CSV

My CSV uses event-level labels, while a motif catalogue may describe patterns across whole narratives or traditions. I will select a small set of categories related to supernatural encounters, transformations, bargains, threats, and mercy. For each one, I will document the catalogue's label and description, compare it with the actual source passage and my `motif_code`, and note whether the mapping is exact, partial, ambiguous, or absent. A missing match is not necessarily a catalogue mistake: the two projects may have different units of analysis.

## Audit questions

1. Who created the catalogue labels and what are their source references?
2. Are story versions, collectors, original languages, translators, and publication dates recorded?
3. Does one broad motif label group events that function differently within their stories?
4. Which events in my dataset cannot be matched clearly to a catalogue category?
5. How might a catalogue's geographic categories obscure translation history and mixed literary traditions?

## Computational steps

1. Export or manually transcribe a *small permitted sample* of catalogue motif labels and definitions into a second CSV with source URLs.
2. Build a simple lookup table connecting my detailed `motif_code` values to broader audit categories.
3. Use Python to count exact, partial, and unmatched categories, and summarize missing provenance fields.
4. Re-read mismatches against the source texts and record interpretive notes instead of silently forcing matches.
5. If the site allows automated access, consider a rate-limited collection script; otherwise use manual sampling. Check robots.txt, usage terms, and archival availability first.

## Planned expansion

The current 60 events come from one English adaptation. To make a real cross-tradition claim, I need a separately documented comparison corpus (for example, a specific South Asian collection with a named collector or translator). I will keep versions distinct and will not infer 'cultural meaning' simply from a region label. A new field will distinguish **my interpretation** from **a published scholar's interpretation**, with a citation for each.

## What would count as a useful result?

The audit should reveal where cross-cultural motif classification is helpful for finding similar stories, and where it leaves out differences in version, narrator, translation, narrative function, or interpretation. I do not expect every label to map neatly.
