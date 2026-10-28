# German Folklore and National Identity: Initial Custom Dataset

**Researcher:** Erin Chon  
**Course:** IS 310 — Culture as Data  
**Milestone:** 2 — Initial Custom Dataset and Audit Plan

## Research Question

How did the Brothers Grimm's collection and classification of folktales contribute to the perception of these stories as German, despite their connections to other cultural traditions?

## Dataset Overview

This project examines the relationship between German folklore, cultural origins, and the development of German national identity. The Brothers Grimm collected and edited folktales that became closely associated with German culture. However, individual stories also have connections to storytellers, literary works, and traditions beyond German-speaking regions.

My initial dataset contains 50 entries from the Brothers Grimm's *Children's and Household Tales* (*Kinder- und Hausmärchen*). Each entry represents one numbered tale in the collection.

The dataset uses KHM numbers, English titles, folktale classifications, and historical-source information to investigate how stories are categorized and represented. My goal is to make visible the cultural connections that may be overlooked when folktales are collectively labeled as German.

## Dataset Organization

The dataset is stored in `grimm_folklore_dataset.csv` and contains 50 records and 10 fields.

| Field | Description |
|---|---|
| `khm_number` | Number assigned to the tale in the Grimm collection |
| `title` | English title of the tale |
| `atu_type` | Aarne–Thompson–Uther folktale classification |
| `tale_type` | Narrative category, not yet coded |
| `documented_source` | Known storyteller or written source associated with the Grimm version |
| `source_region` | Geographic, linguistic, or publication association of the source |
| `cross_cultural_connection` | Documented connections to other storytelling traditions |
| `source_evidence_status` | Status of evidence supporting the recorded source attribution |
| `origin_notes` | Explanations of historical uncertainty and interpretive decisions |
| `source_citation` | Reference supporting the historical information |

The ATU classification system organizes folktales according to recurring narrative patterns. This allows researchers to recognize similarities between stories across different traditions.

However, sharing an ATU classification does not necessarily mean that stories originated in the same country or were transmitted directly between cultures.

For the `source_evidence_status` field, I distinguish between documented, probable, and unknown attributions. These categories describe the available evidence for a recorded source, not certainty about a tale's ultimate geographic origin.

## Inclusion and Exclusion Decisions

I selected KHM 1–50 from the standard numbering of the Brothers Grimm's collection. This creates a consistent and reproducible sample rather than selecting only the most recognizable fairy tales.

I included multiple narrative types to avoid representing Grimm folklore solely through famous stories such as *Cinderella*, *Rapunzel*, and *Little Red Riding Hood*.

This initial dataset excludes tales numbered above KHM 50, modern film adaptations, and unrelated folklore collections.

The dataset also does not attempt to assign every tale a definitive country of origin. Folktales circulated through multiple languages, regions, and storytelling traditions, making exact origins difficult to establish.

I chose to focus on documented historical connections rather than making assumptions about whether individual tales were originally German, French, or from another culture.

## Transformation 1: Cultural Materials to Working Representations

The original cultural materials consist of folktales collected, edited, and published by the Brothers Grimm.

These stories contain narrative details, historical contexts, editorial decisions, and cultural connections that cannot be fully represented through numerical categories.

My first transformation involved selecting individual tales and representing each through its title, KHM number, classification, and historical research notes.

I used D. L. Ashliman's Grimm tale index to identify the stories and their ATU classifications. I also consulted individual tale annotations to investigate documented storytellers, earlier written versions, and connections to other cultural traditions.

This process simplifies the stories by reducing their narrative complexity, oral storytelling traditions, and differences between historical versions into standardized categories.

For example, a tale that circulated through several cultures may be represented by a single KHM identifier. While this makes it easier to organize, it can also obscure the different versions and traditions associated with that story.

## Transformation 2: Working Representations to Structured Data

In the second transformation, I converted the working representation into structured fields using Python in Google Colab.

Each tale became one row in a CSV file. I assigned KHM numbers as identifiers and used ATU classifications to describe recurring narrative patterns.

For cultural origins, I distinguished documented sources from broader cultural connections.

For example, KHM 26, *Little Red Cap*, has documented connections to Jeanette and Marie Hassenpflug, as well as an earlier French literary version published by Charles Perrault in 1697.

Rather than identifying the story as definitively French or German, I recorded these connections separately.

Similarly, *Rapunzel* has connections to earlier Italian and French literary traditions, while the Grimms' immediate source was a German-language story published by Friedrich Schultz in 1790.

These examples demonstrate how a tale's historical transmission can be more complicated than a single national label suggests.

This distinction is significant because the country associated with a storyteller, publication, or earlier written version does not necessarily establish where a story originated.

Additionally, some KHM entries contain multiple narratives or classifications. Preserving these distinctions within a structured dataset presents challenges because a single row cannot fully represent every version of a tale.

## Computational Process

I used Python to create and validate the dataset.

My script `create_grimm_dataset.py` organizes the selected tales, assigns ATU classifications, incorporates researched historical metadata, and exports the records into CSV format.

The validation process checks:

- Total number of records
- Duplicate KHM identifiers
- Availability of ATU classifications
- Number of researched historical sources
- Missing or incomplete values

The validation identified 50 records, no duplicate KHM numbers, and ATU classifications for all 50 tales.

Historical-source metadata has currently been researched for 11 entries, including nine documented source attributions and two probable attributions. The remaining 39 tales require further investigation.

Computational validation helps identify missing information and maintain consistency across records. However, it cannot independently determine whether a historical attribution is accurate. That requires additional research and interpretation.

## Preliminary Findings and Limitations

One of my initial findings is that the Brothers Grimm's collection includes stories with documented connections to both oral storytelling and earlier written publications.

For example, *The Fisherman and His Wife* and *The Juniper Tree* were associated with written versions transmitted by Philipp Otto Runge. Meanwhile, other stories were supplied by individuals connected to the Grimms' social networks.

These examples show that the collection was developed through multiple forms of cultural transmission rather than a single method of gathering oral folklore.

Historical-source metadata has currently been researched for 11 of the 50 tales. Nine records have documented source attributions, while two have probable attributions. The remaining 39 tales require further historical research.

This limitation demonstrates the difficulty of tracing folklore origins because many stories circulated through oral traditions and written publications before appearing in the Brothers Grimm's collection.

Another limitation is that my dataset uses English titles, which may differ across translations.

The `source_region` field also contains different kinds of geographic information. In some cases, it refers to a storyteller's association with a particular region, while in others it refers to a publication location or linguistic tradition. These should not be interpreted as equivalent evidence of a tale's national origin.

The `tale_type` field has not yet been coded, and the ATU classifications currently provide the main narrative categorization.

Future revisions may introduce additional fields to better distinguish these types of information.

## Connection to the Audit

For the second half of the semester, I plan to compare my custom dataset against an existing Grimm fairy-tale dataset downloaded from Kaggle.

My preliminary inspection of the existing dataset identified 63 records containing story titles and full texts. Unlike my custom dataset, it does not include dedicated columns for KHM classifications, ATU types, historical storytellers, or cross-cultural connections.

I also identified a possible data-segmentation error involving *Little Red Cap*, where an additional episode appears to have been treated as a separate record.

This raises questions about how computational extraction and dataset organization can unintentionally change the representation of cultural materials.

My audit will investigate these differences in greater detail, focusing on how cultural information is preserved, simplified, or omitted.

The full audit roadmap is available in `audit_plan.md`.

## Scholarly Sources

**Norberg, Jakob.** *The Brothers Grimm and the Making of German Nationalism*. Cambridge University Press, 2022.

Norberg examines the relationship between the Brothers Grimm and the development of German nationalism. This source is relevant because it helps explain how collecting, publishing, and studying folklore contributed to ideas about German cultural identity.

**Zipes, Jack.** *The Brothers Grimm: From Enchanted Forests to the Modern World*. 2nd ed., Palgrave Macmillan, 2002.

Zipes examines the Brothers Grimm's collection and editing practices, challenging the romanticized perception that they simply preserved unchanged oral folktales. This source supports my investigation of how stories collected from different sources became associated with German cultural identity.

**Bottigheimer, Ruth B.** *Grimms' Bad Girls & Bold Boys: The Moral & Social Vision of the Tales*. Yale University Press, 1987.

Bottigheimer examines the moral and social meanings of the Grimm tales and how editorial revisions shaped them. This relates to my dataset because representing each tale as a single record can obscure differences between historical versions.

Together, these sources demonstrate how folklore collection, literary editing, and national identity are interconnected.

## Sources Used for Dataset Construction

The following resources were used to identify tales, classifications, and historical-source information.

- Ashliman, D. L. [*The Grimm Brothers' Children's and Household Tales*](https://sites.pitt.edu/~dash/grimmtales.html). University of Pittsburgh.
- Ashliman, D. L. [*The Frog King (KHM 1)*](https://sites.pitt.edu/~dash/grimm001.html).
- Ashliman, D. L. [*Rapunzel: A Comparison of the Versions of 1812 and 1857*](https://sites.pitt.edu/~dash/grimm012a.html).
- Ashliman, D. L. [*Hansel and Gretel (KHM 15)*](https://sites.pitt.edu/~dash/grimm015.html).
- Ashliman, D. L. [*The Fisherman and His Wife (KHM 19)*](https://sites.pitt.edu/~dash/grimm019.html).
- Ashliman, D. L. [*Cinderella (KHM 21)*](https://sites.pitt.edu/~dash/grimm021.html).
- Ashliman, D. L. [*Frau Holle (KHM 24)*](https://sites.pitt.edu/~dash/grimm024.html).
- Ashliman, D. L. [*Little Red Cap (KHM 26)*](https://sites.pitt.edu/~dash/grimm026.html).
- Ashliman, D. L. [*The Bremen Town Musicians (KHM 27)*](https://sites.pitt.edu/~dash/grimm027.html).
- Ashliman, D. L. [*The Elves (KHM 39)*](https://sites.pitt.edu/~dash/grimm039.html).
- Ashliman, D. L. [*The Juniper Tree (KHM 47)*](https://sites.pitt.edu/~dash/grimm047.html).
- Ashliman, D. L. [*Little Brier-Rose (KHM 50)*](https://sites.pitt.edu/~dash/grimm050.html).

## Future Research

My next steps involve expanding historical-source research, refining dataset categories, and comparing the custom records with existing cultural data.
I plan to investigate whether additional metadata can preserve information about regional traditions, earlier literary versions, and differences between historical editions.


## Project Files

- [Custom Dataset](grimm_folklore_dataset.csv)
- [Dataset Creation Script](create_grimm_dataset.py)
- [Validation Script](validate_dataset.py)
- [Audit and Comparison Plan](audit_plan.md)
- [Milestone 2 Reflection](reflection.md)
