import pandas as pd
from pathlib import Path
from datetime import datetime

# Load the existing dataset
DATA_FILE = Path("fairytale_dataset.csv")

if not DATA_FILE.exists():
    raise FileNotFoundError("fairytale_dataset.csv was not found.")

df = pd.read_csv(DATA_FILE)

# Information for the four unfinished Rapunzel books
updates = {
    "The Golden Braid": {
        "author": "Melanie Dickerson",
        "publication_year": 2015,
        "setting": "Medieval Germany, including the village and city of Hagenheim",
        "character_changes": "Rapunzel is skilled at throwing knives, painting, and singing. Her protective mother tries to control her future, but Rapunzel develops her own identity and discovers secrets about her past.",
        "protagonist_agency": "High. Rapunzel makes decisions, helps rescue others, pursues an education, and takes control of her future.",
        "major_themes": "Independence, education, identity, courage, faith, love, and trust",
        "original_message": "The traditional tale emphasizes confinement, perseverance, and eventual rescue.",
        "adapted_message": "People should be able to make their own choices, pursue knowledge, and take control of their futures.",
        "retelling_type": "Direct retelling"
    },

    "An Inconvenient Princess": {
        "author": "Melanie Cellier",
        "publication_year": 2018,
        "setting": "A magical fairy-tale kingdom",
        "character_changes": "The story follows Penny, an ordinary seventh child who searches for her adventurous twin sister. Her journey involves a mysterious tower, a rogue fairy, and a Rapunzel-inspired princess.",
        "protagonist_agency": "High. Penny takes responsibility for finding her sister and works through magical problems rather than waiting for someone else to solve them.",
        "major_themes": "Family, self-worth, expectations, courage, independence, and finding one's own path",
        "original_message": "The traditional tale emphasizes confinement, perseverance, and eventual rescue.",
        "adapted_message": "Being ordinary does not make someone less important, and people can shape their own happily ever after.",
        "retelling_type": "Direct retelling"
    },

    "Bad Hair Day": {
        "author": "Sarah Mlynowski",
        "publication_year": 2014,
        "setting": "A modern world connected to the fairy-tale world through a magical mirror",
        "character_changes": "Siblings Abby and Jonah enter the story of Rapunzel. They try to free Rapunzel from her tower and reunite her with her parents, giving the traditional story a happier outcome.",
        "protagonist_agency": "Moderate to high. Abby and Jonah actively work to change the story, while Rapunzel gains the opportunity to escape her confinement and reunite with her family.",
        "major_themes": "Family, friendship, problem-solving, self-acceptance, and consequences",
        "original_message": "The traditional tale emphasizes confinement, perseverance, and eventual rescue.",
        "adapted_message": "People can correct mistakes, help others, and create happier outcomes through their actions.",
        "retelling_type": "Direct retelling"
    },

    "Rapunzel Cuts Loose": {
        "author": "Joan Holub and Suzanne Williams",
        "publication_year": 2014,
        "setting": "Grimmlandia, especially Grimm Academy, a magical school for fairy-tale characters",
        "character_changes": "Rapunzel attends Grimm Academy with Cinderella, Red Riding Hood, and Snow White. Her fast-growing hair develops magical powers that she struggles to control while helping her friends protect the academy.",
        "protagonist_agency": "High. Rapunzel works with her friends, searches for a way to control her magical hair, and helps stop the E.V.I.L. Society.",
        "major_themes": "Friendship, teamwork, courage, confidence, problem-solving, and adolescence",
        "original_message": "The traditional tale emphasizes confinement, perseverance, and eventual rescue.",
        "adapted_message": "Confidence, friendship, and cooperation can help people overcome challenges.",
        "retelling_type": "Direct retelling"
    }
}

# Make sure each book appears exactly once in the dataset
for title in updates:
    matches = (
        (df["original_tale"] == "Rapunzel") &
        (df["book_title"] == title)
    )

    if matches.sum() != 1:
        raise ValueError(
            f"Expected exactly one Rapunzel record for {title}. "
            "No changes were saved."
        )

# Make a backup before changing the dataset
backup_file = Path(
    "fairytale_dataset_backup_"
    + datetime.now().strftime("%Y%m%d_%H%M%S")
    + ".csv"
)

df.to_csv(backup_file, index=False)

# Fill in only fields that are currently blank
for title, information in updates.items():
    matches = (
        (df["original_tale"] == "Rapunzel") &
        (df["book_title"] == title)
    )

    for field, value in information.items():

        if field not in df.columns:
            raise ValueError(f"Missing CSV column: {field}")

        current_value = df.loc[matches, field].iloc[0]

        if pd.isna(current_value) or str(current_value).strip() == "":
            df.loc[matches, field] = value

# Save the updated dataset
df.to_csv(DATA_FILE, index=False)

# Display the results
print("\n--- RAPUNZEL RECORDS UPDATED ---")

for title in updates:
    matches = (
        (df["original_tale"] == "Rapunzel") &
        (df["book_title"] == title)
    )

    row = df.loc[matches].iloc[0]

    print(
        f"{row['book_title']} | "
        f"{row['author']} | "
        f"{row['publication_year']}"
    )

print("\nBackup saved as:", backup_file)
print("Updated dataset saved as:", DATA_FILE)