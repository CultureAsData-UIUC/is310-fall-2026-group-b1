# Milestone 2

"Since each new Camelot builds, however grudgingly, on the stones of its predecessors and each new Arthurian utopia creates itself in dialogue with other Arthurian pasts, no Arthurian text stands completely alone, including [...] Hollywood's cinematic retellings of the rise and fall of Camelot." (Aronstein, p. 30)

## Initial Documentation

To preface, I want to say that I have not yet collected/organized all of my data points. That is because:
1) I wasn't able to get the go ahead for my unique format until shortly before the deadline (amidst many other midterm projects which unfortunately took away from the amount of time I had to construct this dataset), and
2) collecting this form of relational data takes a lot of background reading (reading up on every individual data point) and I'm unfortunately an incredibly slow reader (thank you neurodiversity).

In order to complete this dataset, I will continue researching and going through the process of reading --> taking notes --> coding described below.

\
In this dataset, I have created a relational digraph that documents movies based in Arthurian legend and the other Arthurian media that influenced these movies. The graph is made up of color-coded nodes (pieces of media) and edges (relationships). The key for the colors is as follows:

media formats:
 - Film = green
 - Medieval Text = red
 - Novel = blue
 - Other = yellow

relationship types:
 - Adaptation = purple
 - Inspiration = cyan
 - Continuation (i.e. same series) = black

As my research continues, there are likely to be additional media formats or relationship types added to this key. For this dataset, I am defining Arthurian cinema as movies primarily focusing on stories or characters from Arthurian legend. This does not include every film featuring an Arthurian character (ex: *Night at the Museum: Secret of the Tomb*, which features Sir Lancelot), nor does it include every film inspired by or referencing Arthurian legend (ex: *Ready Player One*, in which the questing protagonist goes by the name Parzival). While I hope for this dataset to end up representing all of Arthurian cinema, for now, I am starting with movies with easily documentable influences (direct adaptations, inspirations discussed in scholarship, series, etc.).

In order to collect information on inspirations and influences, I read through various chapters from the books cited below. After my grandfather came in to speak to our class and mentioned that no one goes to the library to get physical books for research nowadays, I decided to get actual physical books to do the research for this project. I was able to find only a handful of resources on our library's catelog related to Arthurian cinema, the most expansive/relevant of which are the four books cited here.

Scholarly Sources:\
  Aronstein, S. L. (2005). *Hollywood knights : Arthurian cinema and the politics of nostalgia*. Palgrave Macmillan.

  Harty, K. J. (2006). Cinema Arthuriana. In Lacy, N. J. (Ed.), *A history of Arthurian scholarship* (pp.252-260). D.S. Brewer.

  Harty, K. J. (Ed.). (1999). *King Arthur on film : New essays on Arthurian cinema*. McFarland & Company.

  Umland, R. A., & Umland, S. J. (1996). *The use of Arthurian legend in Hollywood film : from Connecticut Yankees to fisher kings*. Greenwood Press.

As stated previously, I am a dreadfully slow reader. As such, I have gotten through only a very small percentage of the above scholarly sources. In order to get a more straightforward/quick starting list of movies, I sought out Wikipedia's list of [films based on Arthurian legend](https://en.wikipedia.org/wiki/List_of_works_based_on_Arthurian_legends#Film), which is where I collected information about direct adaptations and series. The key word here is *starting* list. As I continue my research, I will be on the lookout for any contradictory information or inaccuracies to Wikipedia's information (I have already found one such perplexing contradiction when it comes to the release year of MGM's *The Knights of the Round Table*, see data_notes.md for more details).

As I went through my research, I took notes in the data_notes.md file in this directory. This file documents my growing understanding of Arthurian cinema as a whole as well as the specific relationships I have found to exist/possibly exist for each film (with the sources of this information listed next to each potential relationship). Not every potential relationship listed in my notes document will make it into my final dataset as I may deem some influences to be too minimal/not documented well enough to include (at least for now). 

Once I have deemed a relationship from my notes to be substantial or well-supported, I then add that relationship and any yet-to-be-created nodes to my cinematic_arthuriana_influences.py file (located in this directory). I do this via the Graphviz library which allows me to use python to create dot graphs. The output of this python script is the .gv file in this directory, featuring the python code translated into dot format, and the pdf in this directory, which shows the visualized graph that is created from this code.

The graph created from this code should be an easy-to-understand representation of the influences on Arthurian cinema, but in the case that someone should like more information on the relationships documented in the graph, they will be able to view my research notes via GitHub. As for reusing this data, one may find it useful to simply find relationships visually via the graph, or one may prefer to use the source code of the graph (in dot or python format) to go through the relationships more systematically.

## Audit & Connection Plan

I plan to audit [The Arthurian Preservation Project](https://www.arthurianpreservationproject.com). This website is "An Archive of Open-Access Arthurian Media," with the four-fold mission to locate, digitize, archive, and educate. While my custom dataset is focused on the relationships between arthurian media, this archive is focused on preserving arthurian media, providing access to said media, and providing educational guides for navigating the complex world of arthuriana. As the archive's format-based organizational structure is fairly straightforward (though there would certainly be complexities to investigate here), I have decided to investigate the way media is organized in the two educational guides:
- [The Beginner's Guide to Medieval Arthuriana](https://www.arthurianpreservationproject.com/further-reading/beginners-guide-to-medieval-arthuriana)
- [The Beginner's Guide to Arthurian Cinema](https://www.arthurianpreservationproject.com/further-reading/beginners-guide-to-arthurian-cinema)

Exploring these two pages will be very interesting because the way information is organized on these pages is very unique/evidently subjective and specific to their educational purpose, which is very different from many other, often seemingly objective, ways of organizing collections of media (ex: the format-based organization of the site's navigation side-bar).

## Reflection

I feel fairly good about my project as a whole at this point.

I'm a bit uncertain about how I will deal with any further information inconsistencies/uncertainties (not entirely sure how to deal with the one I've identified so far), but such is the life of someone working with cultural data. Also, I definitely need to figure out how to make my key show up in my final visualization so one doesn't have to go to the source code to understand the color-coding.

One question I have going forward is does each relationship count as an individual datapoint separate from the nodes it is connecting (for the purpose of the "50-100 nodes" requirement)?

Additionally, do you have any recommendations as to how I should go about conducting my audit? It'd be especially helpful to have a better understanding of what the final product of that audit is meant to be.

## Bonus

Things I might do, if I were to take this project further (beyond the end of the semester):
- talk with Arthurian scholars to get their input on the dataset
- turn the graph into a format that can easily be rendered in html and create a webpage where people can access the graph
- learn more about Graphviz's attributes and stylize the graph a bit more
- watch every movie in the database to gain further understandings of the story inspirations and archetypes
    - and read as much written arthuriana as I can to understand these things even more