# Milestone 2: Audit and Connection Plan

## 1. Research Question

How did the Brothers Grimm's collection and classification of folktales contribute to the perception of these stories as German, despite their connections to other cultural traditions?

My project examines how cultural identity is shaped through the collection, publication, and classification of folklore. Although the Brothers Grimm's stories are commonly associated with German culture, some tales have documented connections to earlier literary works, storytellers, and storytelling traditions beyond Germany.

I want to investigate how existing datasets represent these stories and whether their organizational choices preserve or obscure their cultural complexity.

## 2. Existing Dataset to Audit

For my audit, I plan to examine the *Grimms' Fairy Tales* dataset published on Kaggle.

**Dataset:** [Grimms' Fairy Tales — Kaggle](https://www.kaggle.com/datasets/tschomacker/grimms-fairy-tales)

**Platform:** Kaggle

**Unit of observation:** To be confirmed after inspecting the downloaded files. I expect to examine individual fairy tales as the primary units.

I selected this dataset because it provides an existing digital representation of the Brothers Grimm's stories. It offers an opportunity to examine how folktales are organized and what information is considered important enough to preserve.

I will first verify the dataset's actual fields, number of records, source text, edition, and documentation before evaluating its limitations.

## 3. Connection to My Custom Dataset

My custom dataset contains 50 entries from the Brothers Grimm's *Children's and Household Tales*, specifically KHM 1–50.

Each record includes a KHM number, English title, ATU classification, and fields for historical sources and cultural connections.

For 11 stories, I have recorded historical-source information based on documented research. The remaining stories require further investigation.

My custom dataset is intended to make source attribution and cultural connections visible, rather than treating the collection's German identity as proof of each story's geographic origin.

I plan to compare my records with the existing Kaggle dataset to understand how different approaches to structuring folktales influence what readers and researchers can learn.

## 4. Audit Questions

My audit will address five questions:

1. **Source attribution:** Does the existing dataset identify the individuals or written works that supplied stories to the Brothers Grimm?

2. **Cultural connections:** Does it document connections between Grimm tales and stories from other cultural traditions?

3. **National identity:** How does the dataset's title, description, and organization frame the tales as part of German cultural heritage?

4. **Classification:** Does it provide identifiers or folktale classifications that connect individual Grimm stories to broader storytelling traditions?

5. **Historical variation:** Does it identify which edition or translation each tale represents, and does it acknowledge changes between editions?

These questions will help me investigate which aspects of cultural history existing data preserves and which it leaves out.

## 5. Planned Audit Method

### Step 1: Examine the Kaggle dataset

I will download and inspect the existing dataset to determine its size, fields, file formats, source documentation, and unit of observation.

I will record which fields capture narrative content and which, if any, preserve historical or cultural metadata.

### Step 2: Match stories across datasets

I will compare entries in the Kaggle dataset with my 50 selected Grimm tales.

When possible, I will use KHM identifiers. If those identifiers are unavailable, I will match stories by title and manually verify ambiguous matches.

Because English titles vary across translations, I will record alternative titles and avoid assuming that differently named stories are distinct tales.

### Step 3: Compare metadata

For matched stories, I will examine whether the Kaggle dataset records information corresponding to the fields in my custom dataset.

| Cultural information | Custom dataset | Existing dataset |
|---|---|---|
| Story title | Included | To be verified |
| KHM identifier | Included | To be verified |
| ATU classification | Included | To be verified |
| Documented storyteller or written source | Partially researched | To be verified |
| Source region | Partially researched | To be verified |
| Cross-cultural connections | Partially researched | To be verified |
| Historical uncertainty | Recorded for researched tales | To be verified |
| Edition or translation | Not yet coded as a field | To be verified |

I will distinguish between metadata that is absent, metadata that is present but incomplete, and metadata that cannot be assessed.

### Step 4: Conduct computational checks

I plan to use Python to compare the two datasets.

Possible computational methods include:

- Counting the number of matching tales.
- Identifying missing or inconsistent identifiers.
- Comparing available metadata fields.
- Checking for duplicate records.
- Summarizing missing historical-source information.
- Visualizing differences in metadata completeness.

These checks will help make representational differences easier to identify.

### Step 5: Interpret the findings

Finally, I will examine what the differences reveal about the representation of folklore as data.

For example, a dataset containing titles and story texts may support literary or computational analysis while providing limited information about historical storytellers and cultural transmission.

I will consider whether the dataset's structure encourages users to associate the tales exclusively with German culture, while recognizing that a dataset's title alone does not prove how audiences interpret the stories.

### Preliminary Dataset Inspection

I downloaded and examined the existing `grimms_fairytales.csv` dataset. It contains 63 records with three columns: an unnamed row index, `Title`, and `Text`.

Unlike my custom dataset, the existing dataset does not include dedicated fields for KHM identifiers, ATU classifications, historical storytellers, source regions, or cross-cultural connections.

I identified a possible segmentation error in record 23, which appears to separate an additional episode of *Little Red Cap* into its own record. This suggests that the process of converting the stories into structured data may have incorrectly divided one narrative into multiple entries.

For my future audit, I plan to examine how stories were separated into records, compare story titles across datasets, and investigate how missing historical metadata affects the representation of German folklore.

## 6. Expected Findings

I expect that my custom dataset and the existing dataset will emphasize different aspects of the Brothers Grimm's collection.

The Kaggle dataset may prioritize access to story content, while my custom dataset prioritizes historical-source information, classification, and cultural connections.

However, I cannot determine whether these expectations are correct until I inspect the Kaggle files.

I am particularly interested in *Rapunzel*, *Little Red Cap*, and *Little Brier-Rose*, because their documented literary histories offer useful case studies for examining cross-cultural connections.

These examples may illustrate how the difference between a story's publication identity and its historical transmission can become obscured in structured data.

## 7. Limitations and Ethical Considerations

An important limitation is the difficulty of identifying a folktale's original geographic or cultural origin.

Stories can circulate orally and through written publications across languages and national borders. The existence of an earlier French or Italian version does not necessarily establish where a tale originated.

I will therefore avoid assigning definitive national origins without sufficient evidence.

Another limitation involves the historical sources available to researchers. Some storytellers are documented, while others remain unidentified. This can result in unequal representation of particular individuals and traditions.

My audit will distinguish between missing metadata in an existing dataset and gaps in the historical record itself.

I also recognize that my custom dataset makes interpretive decisions. Selecting KHM 1–50, using English titles, and assigning standardized classifications can simplify complex cultural materials.

## 8. Scholarly Context

**Norberg, Jakob.** *The Brothers Grimm and the Making of German Nationalism*. Cambridge University Press, 2022.

Norberg provides historical context for the relationship between the Grimm brothers and German nationalism. His work supports my investigation of how folklore became associated with national identity.

**Zipes, Jack.** *The Brothers Grimm: From Enchanted Forests to the Modern World*. 2nd ed., Palgrave Macmillan, 2002.

Zipes examines the Grimm brothers' collecting and editing practices. His scholarship helps explain why the collection should not be treated as a straightforward transcription of unchanged oral stories.

**Bottigheimer, Ruth B.** *Grimms' Bad Girls & Bold Boys: The Moral & Social Vision of the Tales*. Yale University Press, 1987.

Bottigheimer examines the moral and social dimensions of Grimm tales and their editorial development. Her work supports my concern that datasets representing stories as stable, individual objects may conceal historical revisions.

## 9. Next Steps

During the second half of the semester, I plan to:

1. Complete additional historical research for my custom dataset.
2. Inspect the Kaggle dataset and document its structure.
3. Match overlapping tales between the two datasets.
4. Use Python to compare metadata completeness.
5. Investigate selected tales with strong documented cross-cultural connections.
6. Reflect on how dataset design influences the representation of folklore and national identity.

My overall goal is to understand how cultural information is preserved, transformed, or omitted when folklore becomes structured data.
