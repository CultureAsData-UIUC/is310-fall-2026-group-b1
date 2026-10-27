# Methodology: from stories to data

## Why these materials?

I started with The Arabian Nights because its stories contain supernatural beings, transformations, threats, bargains, and requests for mercy. These events give me a way to test whether shared labels can describe different narrative situations. I chose one identifiable edition instead of mixing retellings without tracking which version I was using. The source is Andrew Lang's 1898 English adaptation, made through an earlier French translation tradition, not an unmediated record of oral storytelling.

## What counts as a row?

**One row = one coded narrative event in a named story section of this particular edition.** A single story can contribute many rows. This is why the dataset contains 60 rows but only three story-section labels. Rows are not statistically independent stories. Some events are ordinary actions that establish context; not all directly involve a jinn. `jinn_explicit=yes` is reserved for events coded as involving the genius/jinn figure, rather than all magic.

## Transformation 1: cultural material to working representation

I first treated the literary narrative as a sequence of smaller events: someone travels, encounters a being, makes an accusation, asks for mercy, tells a story, or undergoes a transformation. This is already an interpretation: a continuous narrative is being divided into separate units. It changes the reading experience and can separate actions from their surrounding context. I kept short summaries, story-section names, and source locators to make that choice visible.

## Transformation 2: working representation to structured data

Next, I turned each event into one CSV row. I assigned an ID, a short summary, a motif label, an actor category, a role category, and a yes/no flag for explicit jinn involvement. The categories allow counting and comparison in Python, but they compress ambiguity. For example, a supernatural figure might threaten someone and later grant mercy; a single `supernatural_role` label may not capture that change. The coding reflects my working analysis, not an original historical taxonomy.

## Inclusion decisions

- Include events in the selected three story sections that can be identified in the chosen edition.
- Include some non-supernatural events when they help explain a later supernatural encounter.
- Preserve repeated events when they represent distinct moments, rather than claiming each row is a new story.
- Preserve source edition, editor, language pathway, and source URL across rows.

## Exclusion decisions

- Do not combine versions from other editions without recording their separate provenance.
- Do not infer a modern country from the *Arabian Nights*' mixed literary history.
- Do not treat a researcher's label as the story's universal cultural meaning.
- Do not fill the `cultural_meaning` column without a clearly attributed interpretation.
- Do not treat an event count as the number of independent stories or traditions.

## Data quality and uncertainty

The source locator is a web-extracted HTML line reference, not a printed page number. These references should be checked again against the actual passage. The `verification` column reports the status recorded during the initial collection; it is not an independent guarantee of accuracy. The current `motif_code` values are detailed and inconsistent in granularity; for a stronger comparison I will create a smaller shared codebook (for example, `threat`, `bargain`, `transformation`, `mercy`, `other`) while retaining the original detailed labels.

## Ethical and interpretive concern

Calling all supernatural beings 'jinn' would erase important distinctions. The current project keeps `actor_type` and `jinn_explicit` separate. The English adaptation also cannot stand in for every Arabic, Persian, South Asian, or Muslim storytelling tradition. Future comparisons will name specific editions, translators, collectors, and sources, and will distinguish a scholar's interpretation from my own coding.
