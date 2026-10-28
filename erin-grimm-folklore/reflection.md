# Milestone 2: Initial Dataset Reflection

## What Is Working?

My project focuses on German oral folklore and how the Brothers Grimm contributed to the development of German national identity through their collection and publication of folktales.

I have successfully created an initial structured dataset containing 50 fairy tales from *Children's and Household Tales*. Each tale is identified by its KHM number and English title, and I have added Aarne–Thompson–Uther classifications to identify broader narrative types.

I used Python to organize the information, generate a CSV file, and perform validation checks. My validation confirmed that the dataset contains 50 records with no duplicate KHM identifiers.

I have also researched the documented sources of 11 stories, including *Rapunzel*, *Cinderella*, *Little Red Cap*, and *Little Brier-Rose*. These examples have helped me understand that the Brothers Grimm's collection includes stories transmitted through both oral and written traditions.

One aspect that is working particularly well is the distinction between a tale's documented source and its possible cultural origins. This allows me to investigate how stories become associated with national identity without automatically assuming that their origins belong to a single country.

## What Is Not Working or Remains Challenging?

My greatest challenge is determining the historical origins of individual folktales. Many stories circulated across different countries and languages before being included in the Brothers Grimm's collection. Finding an earlier written version does not necessarily establish where a story originally developed.

Another challenge is the availability of historical information. While I have recorded source information for 11 tales, 39 records still require additional research. This means my dataset currently provides more complete information about tale classifications than about historical storytellers or cross-cultural connections.

I have also realized that assigning a single cultural origin to each story would oversimplify its history. In some cases, the Grimms received stories from identifiable individuals, while in others, their sources were earlier published works or combinations of oral accounts.

A computational challenge has been deciding how to organize this complexity into consistent fields. For example, some tales have multiple ATU classifications, and one KHM entry can contain several related narratives.

## What Have I Learned?

Before beginning this project, I primarily associated the Brothers Grimm with the preservation of traditional German stories. However, my research has shown me that their collection involved a more complicated process of gathering, adapting, editing, and publishing existing narratives.

For example, *Rapunzel* has connections to earlier Italian and French literary traditions, while *Little Red Cap* has a documented relationship to Charles Perrault's French version.

These examples challenge the assumption that every story published by the Brothers Grimm originated exclusively within Germany.

I have also learned that creating a dataset involves interpretive choices. Deciding which information to include, how to categorize it, and how to represent uncertainty affects how future users might understand the stories.

My initial dataset shows how numerical identifiers and standardized classifications can make cultural materials easier to compare while also potentially obscuring historical differences.

## Preliminary Audit Observations

I downloaded an existing Grimm fairy-tale dataset containing 63 records and examined its structure.

The dataset contains story titles and full texts but does not provide dedicated columns for historical storytellers, source regions, ATU classifications, or cross-cultural connections.

I also identified a possible segmentation problem in which an additional episode of *Little Red Cap* appears as a separate record.

This raised an interesting question about how computational methods can unintentionally change the representation of cultural materials. If an additional episode is counted as an independent tale, the dataset's record count may not accurately represent the number of distinct stories.

These observations will guide my planned audit during the second half of the semester.

## What Might Change?

I plan to continue researching the historical sources and cultural connections of the selected tales.

I may also revise some of my dataset categories to distinguish more clearly between oral storytellers, written literary sources, publication locations, and cultural parallels.

Another possible change is adding a field for the historical edition of each tale. Because the Grimms revised their stories across multiple editions, recording edition information could help preserve differences that are otherwise lost when each tale is represented as one record.

For now, I plan to maintain my focus on KHM 1–50 rather than expanding the dataset. My priority is improving the quality of the existing records.


## Next Steps

For the second half of the semester, I plan to continue researching source information, improve the consistency of my metadata, and compare my custom dataset with the existing Grimm fairy-tale dataset.

My overall goal is to examine how folklore becomes associated with national identity and how the process of structuring stories as data can preserve or erase their cultural complexity.
