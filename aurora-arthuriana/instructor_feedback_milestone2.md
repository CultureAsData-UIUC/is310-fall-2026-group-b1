# Instructor Feedback for Milestone 2

I really like the creativity and intellectual ambition of this project. Representing Arthurian cinema as a network of adaptations, inspirations, continuations, and earlier texts makes sense for your argument that no Arthurian work stands entirely alone. The graph is not simply a visualization added after the research; its relational form is itself an interpretation of how Arthurian stories accumulate, circulate, and become remade.

I also appreciate how transparent you are about the current stage of collection. Data collection is allowed to remain in progress at this milestone, especially for a project that requires substantial reading and source verification. You have clearly explained why the current graph is partial and described your reading, note-taking, and graph-building process. I would not rush to add nodes simply to reach a numerical target. The more important next step is to make the evidence and methodology behind the existing relationships reproducible and legible to another researcher.

## Initial Custom Dataset & What Counts as Data in the Graph?

To answer your question from the reflection, both nodes and edges are data, but they represent different kinds of records:

- A **node** represents a cultural object, such as a film, book, medieval text, comic, or stage production.
- An **edge** represents a claimed relationship between two cultural objects, such as adaptation, inspiration, or continuation.

So it remains up to you if the dataset should be 50-100 nodes or edges. I personally think that each edge can count as a substantive data record when it is documented with its direction, relationship type, evidence, and source. This distinction could also help your final documentation. Rather than reporting one total number of “data points,” you might explain how many cultural objects and how many documented relationships the project currently contains.

The Python and DOT files preserve the graph structure, but much of the research evidence currently lives separately in `data_notes.md`. Someone can see that an edge exists without being able to tell from the graph data why you included it, which source supports it, or how confident you are in the relationship.

I would consider keeping the Graphviz visualization as the project's primary public form while moving the underlying information into two simple structured files:

1. Nodes: One row per cultural object could include fields such as:

- Stable node ID
- Title
- Date or year
- Media format
- Creator, director, author, or composer
- Language or production context when relevant
- Source used to verify the object
- Notes about uncertain dates or titles

2. Relationships: One row per directed relationship could include:

- Source node ID
- Target node ID
- Relationship type
- Evidence or brief explanation
- Citation and page number
- Evidence status or confidence
- Researcher notes

The Python script could read these files and generate the Graphviz output. This would preserve your creative format rather than replacing it with a conventional spreadsheet. It would also make the method more transparent: another researcher could inspect the relationships, identify the supporting evidence, revise a disputed edge, and rebuild the same graph.

### Defining Relationships

The distinction among `adaptation`, `inspiration`, and `continuation` is useful, but I am curious how you decide which label applies. A direct film version of a novel is relatively straightforward, while a scholarly argument that a film uses a Perceval-style motif may be a different kind and strength of relationship.

Your methodology might explain:

- What evidence is sufficient for a direct adaptation
- How you distinguish influence from thematic similarity
- Whether a scholar's interpretation is recorded differently from a creator's statement
- How you represent a work adapted through several intermediate works
- Whether a continuation means the same fictional series, production franchise, or narrative sequence
- How uncertain or contested relationships remain visible

You might preserve a relationship even when the evidence is uncertain, as long as its status is documented. That would be more transparent than either excluding every ambiguous connection or presenting all edges as equally established. I would also make the direction of every edge explicit in the documentation. The current graph appears to point from an earlier or influencing work toward the later work, but stating that rule will make the data easier to interpret and reuse.

### Provenance and Research Notes

The research notes are one of the strongest parts of the submission. They show the reading and uncertainty behind the graph, including the conflicting dates for *Knights of the Round Table* and the distinction between a direct source and a scholar's interpretation of a motif. I would preserve this exploratory notebook-like space even after the structured files are created.

For reproducibility, I would connect each accepted edge back to the relevant note and citation. Page numbers from the books are especially valuable. For web sources such as Wikipedia or Variety, add an access date and explain what claim the source supports. When sources disagree, preserve the competing dates and document how you chose what appears in the node rather than silently resolving the conflict.

The release-date contradiction is not an inconvenience that must disappear before the graph can be valid. It is a useful example of why cultural-data provenance matters. You might include fields such as `date_as_recorded`, `date_status`, and `date_note`, or simply document the uncertainty in the node metadata.

## Computational Reproducibility

The Python script successfully demonstrates how Graphviz can produce the DOT and PDF files. For the final project, I would add a short set of reproduction instructions that explains:

- The required Python package
- The separate Graphviz system installation
- The command used to build the graph
- Which files the script reads
- Which files it creates
- Whether existing output is overwritten

The current script ends with `dot.render(view=True)`, which automatically tries to open the rendered file. Using an explicit filename and `view=False` may make it easier to run consistently on another computer or in an automated environment.

I would also consider generating a web-friendly SVG in addition to the PDF. SVG would preserve the graph as a scalable visual and could later support the HTML version you mention without requiring you to build a fully interactive site now.

I also think color coding is intuitive once someone reads the key in the Python file, but ideally the rendered graph would include that key directly. I agree with your own reflection that readers should not need to inspect source code to understand the colors.

I would also avoid relying on color alone. Shapes, line styles, or edge labels could reinforce the distinctions among media and relationships for readers viewing the graph in grayscale or with color-vision differences. For example, films and books might use different node shapes, while adaptation and inspiration edges could use different line styles as well as colors.

Stable node IDs would also help. The current Python code uses complete display labels such as `Prince Valiant (1954)` as identifiers. If you revise a title or uncertain year, every edge using that label must also change. A short ID such as `film_prince_valiant_1954` could remain stable while a separate label changes as the research develops.

Your current strategy of beginning with well-documented relationships is reasonable. I would continue collecting at a pace that allows you to read and verify the evidence. The final graph does not need to include every Arthurian film ever made in order to make a meaningful argument.

It may help to define a bounded final scope, such as:

- A particular date range
- A set of films discussed in the four scholarly books
- Several adaptation chains followed in depth
- A focused comparison among direct adaptation, indirect influence, and continuation

A bounded graph with transparent evidence may be more persuasive than an apparently comprehensive graph whose edges cannot all be traced. If your scope continues to evolve, document what is included, what is excluded, and why.

## Audit of the Arthurian Preservation Project

The Arthurian Preservation Project is a strong audit choice because it organizes related cultural materials for a different purpose. Your graph emphasizes relationships and influence, while the archive emphasizes preservation, access, formats, and education. The two beginner's guides are especially interesting because their organization is interpretive even when it appears straightforward to a reader.

For the audit's final product, you might create a small structured table in which each row represents an item or recommendation in one of the guides. Possible fields include:

- Guide name
- Work or resource
- Media format
- Position or section in the guide
- Description supplied by the site
- Relationship to another work
- Reason or evidence for its placement, if stated
- Metadata or provenance supplied
- What is absent or uncertain
- Whether the item appears in your graph

You could then compare how the two guides create an educational pathway through Arthuriana and how that pathway differs from your relationship-based graph. I would also investigate who created the project, its stated preservation criteria, what it includes or excludes, how stable its links are, and how it handles copyright and open access.

The audit does not need to prove that one organization is better. A useful finding could be that each structure supports a different use: your graph traces influence, the site's format navigation supports discovery, and the guides construct a beginner's sequence through a complex field.

## Scholarship and Reflection

The scholarly foundation is strong and directly connected to the project. And your notes already show that scholarship can support both edges and explanations of why those relationships matter.

I would continue distinguishing a bibliographic relationship from an interpretive argument. “Film A adapts Novel B” is not the same kind of claim as “Film A uses Arthurian legend to express Cold War political ideals.” Both may belong in the project, but perhaps in different fields or layers.

Your reflection is also refreshingly honest about pace, uncertainty, and the challenges of physical-book research. For the final essay, I would discuss how your process changed as you moved from reading to notes to code to graph. Which edges were easy to establish? Which did you reject? What did the graph make visible that prose notes did not? What complexity did the graph flatten? Those questions would make the methodology as interesting as the finished visualization.

## Priorities for the Final Project

For the next stage, I would suggest focusing on:

- Preserving the creative graph as the main form while separating nodes and relationships into documented structured files.
- Giving each node and edge a stable ID and connecting every accepted relationship to evidence and a citation.
- Explaining how adaptation, inspiration, and continuation are distinguished and how uncertain relationships are represented.
- Defining a feasible final scope rather than trying to represent all Arthurian cinema immediately.
- Keeping conflicting dates and other uncertainties visible in the data and documentation.
- Adding a visible legend and using shapes, labels, or line styles so the graph does not depend on color alone.
- Adding reproduction instructions and generating the graph without automatically opening the output.
- Considering SVG as a web-friendly output while keeping the current PDF.
- Creating a bounded audit table for the Arthurian Preservation Project's two educational guides.
- Reflecting on what was accepted, rejected, simplified, or made visible as the research moved from reading to graph data.

Overall, this is one of the most formally creative submissions I've ever received, and I would encourage you to keep experimenting with the relational structure. Reproducibility does not require making the project less imaginative. It means making the sources, decisions, uncertainty, and transformation process visible enough that another person can understand how this particular Arthurian network came to exist.

