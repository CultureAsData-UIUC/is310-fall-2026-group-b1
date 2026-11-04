\# Modern Fairy-Tale Book Retellings



\## Project Overview



This project investigates how modern book adaptations reinterpret traditional fairy tales. I am interested in how adaptations change characters, settings, protagonist agency, themes, and the messages of their original stories.



My research question is:



\*\*How do modern book retellings of highly visible and less visible fairy tales differ in themes, character changes, settings, and interpretations of original stories?\*\*



I chose this topic because fairy tales are repeatedly adapted for new audiences. Some stories, such as Cinderella and Rapunzel, are widely recognizable, while others may receive less attention.



\## Sampling and Data Collection



I used Fairytalez.com's "Top 100 Most Popular Fairy Tales" as my sampling frame.



I selected five stories:



| Fairy Tale | Fairytalez Rank | Visibility |

|---|---:|---|

| Rapunzel | 2 | High |

| Cinderella | 3 | High |

| Baba Yaga | 20 | Medium |

| The Pied Piper of Hamelin | 79 | Lower |

| The Wild Swans | 85 | Lower |



I aimed to collect approximately 50–100 book adaptations. My final dataset contains 62 books.



| Fairy Tale | Number of Books |

|---|---:|

| Rapunzel | 15 |

| Cinderella | 15 |

| Baba Yaga | 12 |

| The Wild Swans | 10 |

| The Pied Piper of Hamelin | 10 |

| \*\*Total\*\* | \*\*62\*\* |



I used Goodreads and other available book information sources to identify potential adaptations and collect information about titles, authors, publication years, and descriptions.



Each row represents one book adaptation.



\## Approach



I used the Create Data from Scratch approach to construct a small, bespoke dataset. Although I relied on existing sources to identify books, I made the decisions about which books to include and how to annotate each record.



The dataset is stored in `fairytale\_dataset.csv`.



It contains 15 fields:



\- adaptation\_id

\- original\_tale

\- fairytale\_rank

\- book\_title

\- author

\- publication\_year

\- medium

\- setting

\- character\_changes

\- protagonist\_agency

\- major\_themes

\- original\_message

\- adapted\_message

\- source\_url

\- retelling\_type



These fields allow me to compare adaptations beyond their titles and publication information.



\## Inclusion and Exclusion Criteria



I included published books that substantially adapt or draw upon one of the five selected fairy tales.



I used six retelling classifications:



1\. \*\*Direct retelling:\*\* Adapts a specific fairy tale and retains its central plot or characters.

2\. \*\*Loose retelling:\*\* Has a recognizable source tale but substantially changes its story.

3\. \*\*Folklore-inspired:\*\* Uses characters, motifs, or elements from a broader folklore tradition without retelling one specific plot.

4\. \*\*Multi-tale adaptation:\*\* Combines elements from multiple fairy tales.

5\. \*\*Continuation:\*\* Continues the events of an existing fairy tale.

6\. \*\*Uncertain:\*\* Available information is insufficient to confidently determine the relationship to the original story.



I excluded simple reprints and editions, works with only superficial references to a fairy tale, and books that did not substantially relate to one of the selected stories.



These decisions were important because a book featuring a folklore character does not necessarily retell that character's original story.



\## Computational Tools and Methods



I used Python and pandas to organize and analyze the dataset. I also used matplotlib to create charts.



Python and pandas helped me:



\- Store and organize book records in CSV format.

\- Check for missing information.

\- Count books associated with each fairy tale.

\- Group books by retelling type.

\- Summarize publication years.

\- Generate tables for comparing the different stories.



Matplotlib helped create visualizations of the number of books per fairy tale and the distribution of retelling types.



These tools helped identify missing information and patterns, but they did not replace the interpretive work involved in creating the dataset. I still had to examine book descriptions and make decisions about whether a book qualified as an adaptation and how it should be categorized.



\## Initial Findings



The dataset contains 62 books across five fairy tales.



Direct retellings are the largest category, accounting for 38 books, or approximately 61.3% of the sample.



However, the distribution differs between stories. Rapunzel has 13 direct retellings out of 15 books, while Cinderella has 12. Baba Yaga has nine folklore-inspired books out of 12, making it noticeably different from the other stories.



This suggests that some fairy tales are more frequently adapted through recognizable versions of their original plots, while others provide characters and folklore elements that authors incorporate into new stories.



These are preliminary observations from the sample rather than conclusions about all published fairy-tale adaptations.



\## Challenges and Limitations



One challenge was deciding whether a book was a direct retelling, a loose retelling, or simply inspired by folklore. Some book descriptions clearly identified their source material, while others required closer interpretation.



Another challenge was collecting consistent information. Some books had detailed descriptions of their characters, settings, and themes, while other sources provided less information.



The dataset also has limitations related to sampling. Fairytalez's popularity ranking represents one website's ranking and should not be treated as a definitive measurement of cultural visibility. The number of books collected for each story represents my sample, not the total number of adaptations that exist.



My interpretations of themes, protagonist agency, and adapted messages are also subjective. Another researcher might classify some books differently.



\## Next Steps



After the initial dataset submission, I plan to expand the project computationally.



My goal is to investigate whether the patterns in the original 62 books continue when more adaptations are collected.



I plan to explore web scraping, book databases, and available APIs to identify additional books. I could also use automated text analysis to identify recurring words and themes in book descriptions.



Scaling the dataset will introduce challenges. Automated searches may collect books that only mention a fairy tale rather than actually adapt it. Automated classification may also have difficulty distinguishing direct retellings from loose retellings or folklore-inspired works.



I would use computational methods to suggest classifications and identify potential records, but manually review uncertain results.



Ultimately, I want to compare the original manually annotated dataset with a larger computationally collected dataset to investigate what changes when cultural materials are studied at a larger scale.



\## Project Files



| File | Description |

|---|---|

| `fairytale\_dataset.csv` | Original 62-book dataset |

| `fairytale\_dataset.py` | Main dataset program |

| `fairytale\_analysis.py` | Analysis and visualization program |

| `fairytale\_retelling\_counts.csv` | Retelling-type count results |

| `analysis\_output/` | Generated charts and analysis tables |

| `README.md` | Project documentation |

| `ai-chat-log.md` | Documentation of AI assistance |



\## Running the Analysis



Install the required Python libraries:



```powershell

py -m pip install pandas matplotlib

