# German Folklore and National Identity: Initial Custom Dataset
**Milestone:** 2 — Initial Custom Dataset and Audit Plan

## Research Question

How did the Brothers Grimm's collection and classification of folktales contribute to the perception of these stories as German, despite their connections to other cultural traditions?

## Dataset Overview

This project examines the relationship between German folklore, cultural origins, and the development of German national identity. The Brothers Grimm collected and edited folktales that became closely associated with German cultural. However, individual stories also have connections to storytellers, literary works, and traditions beyond German speaking areas.

My initial dataset contains 50 entries from the Brothers Grimm's *Children's and Household Tales* (*Kinder- und Hausmärchen*). Each entry represents one tale in the collection. The dataset uses KHM numbers, English titles, folktale classifications, and historical-source information to investigate how stories are categorized and represented.

## Dataset Organization

The dataset is stored in `grimm_folklore_dataset.csv` and contains 50 records and 10 fields.

| Field | Description |
|---|---|
| `khm_number` | Official number assigned to the tale in the Grimm collection |
| `title` | Title of the tale |
| `atu_type` | Aarne–Thompson–Uther folktale classification |
| `tale_type` | Narrative category, not yet coded |
| `documented_source` | Known person/written source associated with the Grimm version |
| `source_region` | Geographic region associated with the source |
| `cross_cultural_connection` | Documented connections to other traditions |
| `source_evidence_status` | Status of evidence supporting the recorded source |
| `origin_notes` | Explanations of historical uncertainty |
| `source_citation` | Reference supporting the historical information |

## Inclusion and Exclusion Decisions

I selected KHM 1–50 from the standard numbering of the Brothers Grimm's collection. This creates a consistent and reproducible sample rather than selecting only the most recognizable fairy tales. I included multiple narrative types to avoid representing Grimm folklore solely through famous stories such as *Cinderella*, *Rapunzel*, and *Little Red Riding Hood*. This initial dataset excludes tales numbered above KHM 50 and film adaptations. The dataset also does not try to assign every tale a definitive country of origin because these stories circulate through multiple languages and region making exact origins difficult to establish.

## Transformation 1: Cultural Materials to Working Representations

The original cultural materials consist of folktales collected and published by the Brothers Grimm. These stories contain narrative details, historical contexts, editorial decisions, and cultural connections that cannot be fully represented through the numerical categories. My first transformation involved selecting  tales and representing each through its title, KHM number, classification, and research notes. I used D. L. Ashliman's Grimm tale index to identify the stories and their ATU classifications. This process simplifies the stories narrative complexity, oral performances, and differences between historical versions.

## Transformation 2: Working Representations to Structured Data

In the second transformation, I converting the working representation into fields using Python on Cocalc. Each tale became one row in a CSV file and I assigned KHM numbers as identifiers and used ATU classifications to describe recurring narrative patterns. For cultural origins I distinguished documented sources from broader cultural connections. Rather than identifying the story as definitively French or German, I recorded these connections separately. This distinction is significant because the country associated with a storyteller or earlier written version does not necessarily establish where it originated from.

## Computational Process

I used Python to create and validate the dataset. My script `create_grimm_dataset.py` organizes the selected tales, assigns classifications, incorporates researched metadata, and exports the records into CSV format.

The validation process checks:

- Total number of records
- Duplicate KHM identifiers
- Availability of ATU classifications
- Number of documented historical sources
- Missing or incomplete values

The initial validation identified 50 records, no duplicate KHM numbers, and ATU classifications for all 50 tales. Historical source metadata has currently been researched for two entries. The remaining 48 require further investigation.

## Preliminary Findings and Limitations

The initial dataset demonstrates that the Grimm collection can be represented through a standardized classification system, but ATU classifications describe recurring narrative patterns rather than establishing a tale's geographical origin. The greatest limitation is the incomplete historical source information. Although all entries have titles and classifications, most do not yet contain verified information about their storytellers or cultural connections.In the future I will focus on expanding historical research while maintaining distinctions between documented evidence, cultural parallels, and uncertain origins.

### Scholarly Sources

**Zipes, Jack.** *The Brothers Grimm: From Enchanted Forests to the Modern World*. 2nd ed., Palgrave Macmillan, 2002.

This source is relevant because my project investigates how stories collected from different sources became associated with German cultural identity.

**Bottigheimer, Ruth B.** *Grimms' Bad Girls & Bold Boys: The Moral & Social Vision of the Tales*. Yale University Press, 1987.

This relates to my dataset because representing each tale as a single record can obscure the differences between its historical versions.

## Sources Used for Dataset Construction

Ashliman, D. L. *The Grimm Brothers' Children's and Household Tales*. University of Pittsburgh. https://sites.pitt.edu/~dash/grimmtales.html

Ashliman, D. L. *Little Red Cap (KHM 26)*. https://sites.pitt.edu/~dash/grimm026.html

Ashliman, D. L. *Little Brier-Rose (KHM 50)*. https
