
import pandas as pd
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("fairytale_dataset.csv")

if not DATA_FILE.exists():
    raise FileNotFoundError("fairytale_dataset.csv was not found.")

df = pd.read_csv(DATA_FILE)

updates = {
    "Dreaming Anastasia": {
        "author": "Joy Preble",
        "publication_year": 2009,
        "setting": "Modern-day Chicago and historical Russia during the Romanov era",
        "character_changes": "Baba Yaga becomes a powerful witch connected to the disappearance of Anastasia Romanov. Teenager Anne experiences dreams that connect her to Anastasia and must help save her.",
        "protagonist_agency": "High. Anne investigates her dreams, works with Ethan, and takes responsibility for helping Anastasia.",
        "major_themes": "History, identity, love, magic, family, destiny, and betrayal",
        "original_message": "Traditional Baba Yaga folklore often presents the witch as a dangerous and unpredictable figure who tests or challenges those who encounter her.",
        "adapted_message": "The past can shape the present, but courage and personal choices can help people overcome seemingly impossible situations.",
        "retelling_type": "Folklore-inspired"
    },

    "The Door by the Staircase": {
        "author": "Katherine Marsh",
        "publication_year": 2016,
        "setting": "A fictional town in upstate New York, near a mysterious spiritualist community",
        "character_changes": "Mary Hayes is an orphan adopted by Madame Z, a mysterious woman connected to Russian folklore and Baba Yaga. Mary discovers that her new guardian has secrets and that the town contains real magic.",
        "protagonist_agency": "High. Mary investigates the secrets surrounding Madame Z, forms friendships, and uses her courage and intelligence to help herself and others.",
        "major_themes": "Family, belonging, friendship, bravery, trust, and identity",
        "original_message": "Baba Yaga folklore often warns people about dangerous strangers and emphasizes cleverness and courage when facing the unknown.",
        "adapted_message": "Family can be created through love and trust, and people should not be judged only by their appearances or reputations.",
        "retelling_type": "Folklore-inspired"
    },

    "Vassa in the Night": {
        "author": "Sarah Porter",
        "publication_year": 2016,
        "setting": "A dark, magical version of modern-day Brooklyn",
        "character_changes": "Vassa lives with her stepmother and stepsisters and becomes trapped working at a dangerous convenience store owned by Babs Yagg, a modern version of Baba Yaga. Vassa receives help from a magical wooden doll named Erg.",
        "protagonist_agency": "High. Vassa uses her intelligence, determination, and the help of Erg to survive the store's challenges and confront the witch.",
        "major_themes": "Family, belonging, independence, magic, survival, identity, and growing up",
        "original_message": "The traditional Vasilisa story emphasizes courage, cleverness, and the importance of guidance when facing danger.",
        "adapted_message": "People can overcome dangerous situations through resourcefulness, courage, and help from unexpected allies.",
        "retelling_type": "Loose retelling"
    },

    "The House with Chicken Legs": {
        "author": "Sophie Anderson",
        "publication_year": 2018,
        "setting": "A magical world in which a walking house travels between places and the world of the living and the dead",
        "character_changes": "Marinka is the granddaughter of Baba Yaga and is expected to follow her grandmother's role of guiding the dead to the afterlife. Instead, she wants to make friends and choose her own future.",
        "protagonist_agency": "High. Marinka challenges the future expected of her, makes friends, and searches for a way to decide her own destiny.",
        "major_themes": "Life and death, friendship, family, freedom, identity, grief, and belonging",
        "original_message": "Baba Yaga folklore often portrays the witch as a mysterious guardian of the boundary between the living and the dead.",
        "adapted_message": "People should have the freedom to choose their own paths, even when family traditions create expectations for them.",
        "retelling_type": "Folklore-inspired"
    },

    "A Wolf for a Spell": {
        "author": "Karah Sutton",
        "publication_year": 2020,
        "setting": "A magical forest and an imaginary kingdom inspired by imperial Russia",
        "character_changes": "A young wolf named Zima switches bodies with Baba Yaga after asking the witch for help. Zima must learn to act as the witch while working with an orphan girl named Nadya to protect the forest.",
        "protagonist_agency": "High. Zima makes difficult decisions, works with Nadya, and helps bring wolves, witches, and villagers together against a dangerous enemy.",
        "major_themes": "Friendship, courage, family, cooperation, identity, forgiveness, and generosity",
        "original_message": "Baba Yaga folklore often presents the witch as a powerful and unpredictable figure who can be dangerous but may also provide help.",
        "adapted_message": "People who seem different can work together, and bravery and generosity matter more than appearances or assumptions.",
        "retelling_type": "Folklore-inspired"
    }
}

# Verify that every book appears exactly once under Baba Yaga
for title in updates:
    matches = (
        (df["original_tale"] == "Baba Yaga") &
        (df["book_title"] == title)
    )

    if matches.sum() != 1:
        raise ValueError(
            f"Expected exactly one Baba Yaga record for '{title}'. "
            "No changes were saved."
        )

# Verify all required columns exist
for title, information in updates.items():
    for field in information:
        if field not in df.columns:
            raise ValueError(f"Missing CSV column: {field}")

# Create a backup before updating
backup_file = Path(
    "fairytale_dataset_backup_"
    + datetime.now().strftime("%Y%m%d_%H%M%S")
    + ".csv"
)

df.to_csv(backup_file, index=False)

# Fill only blank fields
for title, information in updates.items():
    matches = (
        (df["original_tale"] == "Baba Yaga") &
        (df["book_title"] == title)
    )

    for field, value in information.items():
        current_value = df.loc[matches, field].iloc[0]

        if pd.isna(current_value) or str(current_value).strip() == "":
            df.loc[matches, field] = value

# Save the updated dataset
df.to_csv(DATA_FILE, index=False)

print("\n--- BABA YAGA RECORDS UPDATED ---")

for title in updates:
    matches = (
        (df["original_tale"] == "Baba Yaga") &
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
