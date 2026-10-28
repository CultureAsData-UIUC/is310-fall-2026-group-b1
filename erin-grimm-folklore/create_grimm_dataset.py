
import csv

# Erin Chon
# IS 310 - Milestone 2
# German Folklore and National Identity
#
# Research Question:
# How did the Brothers Grimm's collection of folktales
# contribute to perceptions of these stories as German,
# despite their connections to other cultural traditions?

# --------------------------------------------------
# STEP 1: SELECT 50 GRIMM FAIRY TALES
# --------------------------------------------------

tales = [
    [1, "The Frog King"],
    [2, "Cat and Mouse in Partnership"],
    [3, "Mary's Child"],
    [4, "The Story of a Boy Who Went Forth to Learn Fear"],
    [5, "The Wolf and the Seven Young Kids"],
    [6, "Faithful Johannes"],
    [7, "The Good Bargain"],
    [8, "The Strange Musician"],
    [9, "The Twelve Brothers"],
    [10, "The Pack of Scoundrels"],
    [11, "Little Brother and Little Sister"],
    [12, "Rapunzel"],
    [13, "The Three Little Men in the Woods"],
    [14, "The Three Spinning Women"],
    [15, "Hansel and Gretel"],
    [16, "The Three Snake-Leaves"],
    [17, "The White Snake"],
    [18, "Straw, Coal, and Bean"],
    [19, "The Fisherman and His Wife"],
    [20, "The Brave Little Tailor"],
    [21, "Cinderella"],
    [22, "The Riddle"],
    [23, "The Mouse, the Bird, and the Sausage"],
    [24, "Frau Holle"],
    [25, "The Seven Ravens"],
    [26, "Little Red Cap"],
    [27, "The Bremen Town Musicians"],
    [28, "The Singing Bone"],
    [29, "The Devil with the Three Golden Hairs"],
    [30, "Little Louse and Little Flea"],
    [31, "The Girl without Hands"],
    [32, "Clever Hans"],
    [33, "The Three Languages"],
    [34, "Clever Elsie"],
    [35, "The Tailor in Heaven"],
    [36, "Table-Be-Set, Gold-Donkey, and Cudgel-out-of-the-Sack"],
    [37, "Thumbthick"],
    [38, "Mrs. Fox's Wedding"],
    [39, "The Elves"],
    [40, "The Robber Bridegroom"],
    [41, "Herr Korbes"],
    [42, "The Godfather"],
    [43, "Frau Trude"],
    [44, "Godfather Death"],
    [45, "Thumbling's Travels"],
    [46, "Fitcher's Bird"],
    [47, "The Juniper Tree"],
    [48, "Old Sultan"],
    [49, "The Six Swans"],
    [50, "Little Brier-Rose"]
]

# --------------------------------------------------
# STEP 2: FOLKTALE CLASSIFICATIONS
# --------------------------------------------------

# ATU = Aarne-Thompson-Uther classification
# Source: D. L. Ashliman, University of Pittsburgh
# Some tales have multiple classifications.

atu_types = {
    1: "440",
    2: "15",
    3: "710",
    4: "326",
    5: "123",
    6: "516",
    7: "1642",
    8: "151",
    9: "451",
    10: "210",
    11: "450",
    12: "310",
    13: "403B, 480",
    14: "501",
    15: "327A",
    16: "612",
    17: "673",
    18: "295",
    19: "555",
    20: "1640",
    21: "510A",
    22: "851",
    23: "85",
    24: "480",
    25: "451",
    26: "333",
    27: "130",
    28: "780",
    29: "461, 930",
    30: "2022",
    31: "706",
    32: "1696",
    33: "671",
    34: "1450",
    35: "800",
    36: "563",
    37: "700",
    38: "65",
    39: "503*, 476*, 7015, 5070, 5085",
    40: "955",
    41: "210",
    42: "332",
    43: "334",
    44: "332",
    45: "700",
    46: "311",
    47: "720",
    48: "101",
    49: "451",
    50: "410"
}

# --------------------------------------------------
# STEP 3: HISTORICAL AND CULTURAL RESEARCH
# --------------------------------------------------

# These records contain documented historical evidence.
# Sources and cultural parallels are NOT necessarily
# proof of a tale's original geographic origin.


research = {
    1: {
        "documented_source": "Wild family oral tradition (probable)",
        "source_region": "Kassel, Hesse",
        "cross_cultural_connection": "Comparable frog-bridegroom tales in other traditions",
        "source_evidence_status": "probable",
        "origin_notes": "The precise informant is unknown. The tale apparently came from the Wild family's oral tradition in Kassel.",
        "source_citation": "https://sites.pitt.edu/~dash/grimm001.html"
    },

    12: {
        "documented_source": "Friedrich Schultz, Kleine Romane (1790)",
        "source_region": "Leipzig (publication location)",
        "cross_cultural_connection": "Italian Petrosinella by Basile; French Persinette by de la Force",
        "source_evidence_status": "documented",
        "origin_notes": "The Grimms used a printed German-language story by Schultz. Earlier Italian and French literary variants also exist. Publication location is not the tale's origin.",
        "source_citation": "https://sites.pitt.edu/~dash/grimm012a.html"
    },

    15: {
        "documented_source": "Hessian oral stories; Wild household (probable)",
        "source_region": "Hesse, German-speaking region",
        "cross_cultural_connection": "Italian Ninnillo and Nennella by Basile; related French Little Thumb by Perrault",
        "source_evidence_status": "probable",
        "origin_notes": "The specific original storyteller is uncertain. Dortchen Wild contributed a verse in 1813. The Grimms revised the tale across editions.",
        "source_citation": "https://sites.pitt.edu/~dash/grimm015.html"
    },

    19: {
        "documented_source": "Philipp Otto Runge manuscript",
        "source_region": "Low German language tradition",
        "cross_cultural_connection": "Related ATU 555 tales about wishes and dissatisfaction",
        "source_evidence_status": "documented",
        "origin_notes": "Runge transmitted a Low German manuscript. It reached the Grimms in 1809. The earlier storyteller and ultimate origin are not established.",
        "source_citation": "https://sites.pitt.edu/~dash/grimm019.html"
    },

    21: {
        "documented_source": "Dorothea Viehmann and other sources",
        "source_region": "Not yet verified",
        "cross_cultural_connection": "French Cinderella by Charles Perrault; other ATU 510A variants",
        "source_evidence_status": "documented",
        "origin_notes": "Viehmann was among the Grimms' sources. Multiple versions contributed to the tale, which was substantially revised for the 1819 edition.",
        "source_citation": "https://sites.pitt.edu/~dash/grimm021.html"
    },

    24: {
        "documented_source": "Henriette Dorothea Wild; later details from G. A. F. Goldmann",
        "source_region": "Kassel-associated Wild family; Goldmann in Hannover",
        "cross_cultural_connection": "Frau Holle regional legendary traditions",
        "source_evidence_status": "documented",
        "origin_notes": "Dortchen Wild supplied the initial version. Goldmann contributed details incorporated into the second edition.",
        "source_citation": "https://sites.pitt.edu/~dash/grimm024.html"
    },

    26: {
        "documented_source": "Jeanette and Marie Hassenpflug",
        "source_region": "Not yet verified",
        "cross_cultural_connection": "French literary version by Charles Perrault (1697)",
        "source_evidence_status": "documented",
        "origin_notes": "Jeanette supplied the main story; Marie supplied the additional episode. The earlier French version does not establish the tale's ultimate origin.",
        "source_citation": "https://sites.pitt.edu/~dash/grimm026.html"
    },

    27: {
        "documented_source": "Dorothea Viehmann",
        "source_region": "Not yet verified",
        "cross_cultural_connection": "Other ATU 130 animal tales",
        "source_evidence_status": "documented",
        "origin_notes": "Viehmann supplied the Grimm version. The tale first appeared in the 1819 edition.",
        "source_citation": "https://sites.pitt.edu/~dash/grimm027.html"
    },

    39: {
        "documented_source": "Gretchen Wild",
        "source_region": "Kassel-associated Wild family",
        "cross_cultural_connection": "European helpful-elf and changeling legends",
        "source_evidence_status": "documented",
        "origin_notes": "Gretchen Wild supplied all three narratives grouped under KHM 39. This record combines multiple tales and classifications.",
        "source_citation": "https://sites.pitt.edu/~dash/grimm039.html"
    },

    47: {
        "documented_source": "Philipp Otto Runge",
        "source_region": "Low German language tradition",
        "cross_cultural_connection": "Other ATU 720 tales about the murdered child",
        "source_evidence_status": "documented",
        "origin_notes": "Runge's written version appeared in 1808 before the Grimms published it. They also knew other versions.",
        "source_citation": "https://sites.pitt.edu/~dash/grimm047.html"
    },

    50: {
        "documented_source": "Marie Hassenpflug",
        "source_region": "Not yet verified",
        "cross_cultural_connection": "French Sleeping Beauty version by Charles Perrault",
        "source_evidence_status": "documented",
        "origin_notes": "Marie Hassenpflug supplied the Grimm version. The earlier French literary version does not establish the tale's original birthplace.",
        "source_citation": "https://sites.pitt.edu/~dash/grimm050.html"
    }
}


# --------------------------------------------------
# STEP 4: CREATE STRUCTURED DATASET
# --------------------------------------------------

filename = "grimm_folklore_dataset.csv"

fieldnames = [
    "khm_number",
    "title",
    "atu_type",
    "tale_type",
    "documented_source",
    "source_region",
    "cross_cultural_connection",
    "source_evidence_status",
    "origin_notes",
    "source_citation"
]

with open(filename, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for khm, title in tales:

        # Retrieve researched information when available
        info = research.get(khm, {})

        writer.writerow({
            "khm_number": khm,
            "title": title,
            "atu_type": atu_types.get(khm, "unknown"),
            "tale_type": "not_yet_coded",
            "documented_source": info.get(
                "documented_source", "unknown"
            ),
            "source_region": info.get(
                "source_region", "unknown"
            ),
            "cross_cultural_connection": info.get(
                "cross_cultural_connection", "not_yet_researched"
            ),
            "source_evidence_status": info.get(
                "source_evidence_status", "unknown"
            ),
            "origin_notes": info.get(
                "origin_notes", ""
            ),
            "source_citation": info.get(
                "source_citation", ""
            )
        })

# --------------------------------------------------
# STEP 5: VALIDATE THE DATASET
# --------------------------------------------------

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

print("DATASET VALIDATION")
print("------------------------------")

# Total number of records
print("Total stories:", len(data))

# Check for duplicate identifiers
khm_numbers = [row["khm_number"] for row in data]
duplicates = len(khm_numbers) - len(set(khm_numbers))

print("Duplicate KHM numbers:", duplicates)

# Check ATU classifications
classified = sum(
    row["atu_type"] != "unknown"
    for row in data
)

print("Stories with ATU classifications:", classified)

# Check historical research
researched = sum(
    row["documented_source"] != "unknown"
    for row in data
)

print("Stories with documented sources:", researched)

print("Stories needing source research:", len(data) - researched)

# Check completeness
print("\nCOLUMN COMPLETENESS")
print("------------------------------")

missing_markers = {
    "",
    "unknown",
    "not_yet_coded",
    "not_yet_researched",
    "Not yet verified"
}

for column in fieldnames:
    missing = sum(
        row[column] in missing_markers
        for row in data
    )
    print(f"{column}: {missing} incomplete records")

# Final checks
assert len(data) == 50, "Dataset should contain 50 stories."
assert duplicates == 0, "Duplicate KHM numbers found."
assert classified == 50, "Some ATU classifications are missing."

print("\nDataset validation passed!")
print("CSV file created:", filename)
