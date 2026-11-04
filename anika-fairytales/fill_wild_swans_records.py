
import pandas as pd
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("fairytale_dataset.csv")

if not DATA_FILE.exists():
    raise FileNotFoundError("fairytale_dataset.csv was not found.")

df = pd.read_csv(DATA_FILE)

updates = {
    "Daughter of the Forest": {
        "author": "Juliet Marillier",
        "publication_year": 1999,
        "setting": "Early medieval Ireland, especially the Sevenwaters estate and surrounding forests",
        "character_changes": "Sorcha is the youngest and only daughter in a family of seven children. When her six brothers are transformed into swans by their stepmother, Sorcha must remain silent and make shirts from plants to break the curse.",
        "protagonist_agency": "High. Sorcha accepts a difficult task, endures hardship, and works to save her brothers even when she faces danger and isolation.",
        "major_themes": "Family loyalty, sacrifice, courage, love, silence, identity, and perseverance",
        "original_message": "The traditional Six Swans tale emphasizes sibling loyalty, sacrifice, and perseverance through a difficult task.",
        "adapted_message": "Love and loyalty can require great sacrifice, but courage and determination can overcome powerful obstacles.",
        "retelling_type": "Direct retelling"
    },

    "Six Crimson Cranes": {
        "author": "Elizabeth Lim",
        "publication_year": 2021,
        "setting": "Kiata, a fantasy kingdom inspired by East Asian cultures and folklore",
        "character_changes": "Princess Shiori is banished by her stepmother, who transforms her six brothers into cranes and removes Shiori's ability to speak. Shiori must uncover a conspiracy and find a way to save her brothers and kingdom.",
        "protagonist_agency": "High. Shiori investigates the curse, travels independently, uses her forbidden magic, and takes responsibility for saving her family and kingdom.",
        "major_themes": "Family, identity, magic, courage, sacrifice, trust, and responsibility",
        "original_message": "The traditional Six Swans tale emphasizes sibling loyalty, sacrifice, and the importance of completing a difficult task.",
        "adapted_message": "People should embrace their identities and abilities, and courage and trust can help overcome difficult circumstances.",
        "retelling_type": "Loose retelling"
    },

    "The Swan Kingdom": {
        "author": "Zoë Marriott",
        "publication_year": 2007,
        "setting": "A fictional fantasy kingdom with forests, magical traditions, and royal courts",
        "character_changes": "Alexandra loses her mother, sees her father fall under the influence of a mysterious woman, and is separated from her brothers. She discovers healing abilities and must find a way to restore her family and kingdom.",
        "protagonist_agency": "High. Alexandra uses her inherited gifts, survives exile, and works to reclaim her family's kingdom.",
        "major_themes": "Family, identity, healing, courage, magic, love, and self-discovery",
        "original_message": "The Wild Swans emphasizes family loyalty, sacrifice, and perseverance in breaking a curse.",
        "adapted_message": "People can discover their own strength and use their abilities to protect those they love.",
        "retelling_type": "Loose retelling"
    },

    "Princess of the Wild Swans": {
        "author": "Diane Zahler",
        "publication_year": 2012,
        "setting": "A fantasy kingdom with a castle, royal court, and a lake where cursed princes live as swans",
        "character_changes": "Princess Meriel's stepmother transforms her brothers into swans. Meriel must complete a difficult task to save them before the lake freezes, with help from two new friends.",
        "protagonist_agency": "High. Meriel takes responsibility for saving her brothers and works with others to complete the task despite the danger.",
        "major_themes": "Family, courage, friendship, sacrifice, perseverance, and loyalty",
        "original_message": "The traditional tale emphasizes sibling loyalty, silence, sacrifice, and perseverance.",
        "adapted_message": "Love for family and determination can help people overcome seemingly impossible challenges.",
        "retelling_type": "Direct retelling"
    },

    "Kingdom of Feathers": {
        "author": "Deborah Grace White",
        "publication_year": 2021,
        "setting": "A fantasy world with two neighboring kingdoms, royal courts, and dragons",
        "character_changes": "Princess Wren's six older brothers are transformed into swans. She must remain silent for six years while working to break their curse, while Prince Basil faces a war between their kingdoms.",
        "protagonist_agency": "High. Wren takes responsibility for saving her brothers and works with Basil to prevent further conflict between their kingdoms.",
        "major_themes": "Family, sacrifice, communication, trust, peace, courage, and love",
        "original_message": "The traditional Wild Swans tale emphasizes sibling loyalty, sacrifice, and perseverance through a vow of silence.",
        "adapted_message": "Trust, cooperation, and understanding can overcome conflict and help people protect those they love.",
        "retelling_type": "Direct retelling"
    },

    "Nettled": {
        "author": "Sarah Carlisle",
        "publication_year": 2024,
        "setting": "The fantasy kingdom of Cwmyr, with royal families, forests, and magical creatures",
        "character_changes": "Princess Maeryn's seven brothers are transformed into giant spiders instead of swans. Maeryn must remain silent and knit with nettles while trying to break their curse. Prince Eadmund initially misunderstands her behavior.",
        "protagonist_agency": "High. Maeryn takes responsibility for breaking the curse and continues her work despite isolation and suspicion from others.",
        "major_themes": "Family, sacrifice, trust, love, courage, perseverance, and misunderstanding",
        "original_message": "The traditional Wild Swans tale emphasizes sibling loyalty, sacrifice, and perseverance through a difficult task.",
        "adapted_message": "Love and loyalty require patience and determination, and people should look beyond appearances before judging others.",
        "retelling_type": "Direct retelling"
    },

    "Silenced Beauty": {
        "author": "Ashley Mendoza",
        "publication_year": 2025,
        "setting": "A fantasy kingdom with a royal court, a royal bridal competition, and a magical curse",
        "character_changes": "Alianna's brothers are transformed into swans after a warning about the royal mage goes wrong. Alianna loses her voice and enters a royal bridal competition to get close enough to break the curse and expose the threat.",
        "protagonist_agency": "High. Alianna enters the competition intentionally, investigates the danger surrounding the kingdom, and works to save her brothers.",
        "major_themes": "Family, courage, faith, love, betrayal, forgiveness, and self-worth",
        "original_message": "The traditional Wild Swans tale emphasizes sibling loyalty, sacrifice, and perseverance despite a vow of silence.",
        "adapted_message": "Courage, faith, kindness, and determination can help people overcome betrayal and protect their families.",
        "retelling_type": "Direct retelling"
    },

    "Princess of Feathers": {
        "author": "Laura Greenwood",
        "publication_year": 2022,
        "setting": "A magical fantasy kingdom centered around Grimm Academy and a royal princess competition",
        "character_changes": "Princess Elisa discovers that her brothers have been cursed into swans. She must remain silent while trying to save them, all while dealing with a dangerous prophecy and a growing romance.",
        "protagonist_agency": "High. Elisa works to save her brothers, investigates her prophecy, and makes decisions about her future.",
        "major_themes": "Family, friendship, courage, destiny, sacrifice, romance, and independence",
        "original_message": "The traditional Wild Swans tale emphasizes sibling loyalty, sacrifice, and perseverance through silence.",
        "adapted_message": "People can challenge expectations about their futures and use courage and cooperation to protect the people they love.",
        "retelling_type": "Direct retelling"
    }
}

# The two books titled The Wild Swans need URL-based identification.
wild_swans_records = {
    "22046015": {
        "author": "K.M. Shea",
        "publication_year": 2014,
        "setting": "The fantasy kingdom of Arcainia",
        "character_changes": "Elise is the foster-daughter of the king. Her seven foster-brothers are transformed into swans by their stepmother. Elise must knit seven shirts from stinging nettles without speaking to break the curse.",
        "protagonist_agency": "High. Elise accepts the challenge, works to break the curse, and makes important decisions about her future.",
        "major_themes": "Family, sacrifice, love, courage, loyalty, forgiveness, and perseverance",
        "original_message": "The traditional Wild Swans tale emphasizes sibling loyalty, sacrifice, and completing a difficult task despite hardship.",
        "adapted_message": "Love and sacrifice can overcome difficult circumstances, and people should not be judged by their appearances or status.",
        "retelling_type": "Direct retelling"
    },

    "9767": {
        "author": "Peg Kerr",
        "publication_year": 1999,
        "setting": "England in 1689 and New York City in 1981",
        "character_changes": "The novel combines two stories. Lady Eliza Grey searches for her eleven brothers after they are transformed into swans, while Elias Latham struggles with rejection and AIDS in 1980s New York.",
        "protagonist_agency": "High. Eliza works to save her brothers despite exile and accusations of witchcraft. Elias also makes choices about survival, relationships, and finding acceptance.",
        "major_themes": "Family, rejection, love, acceptance, persecution, loyalty, illness, and community",
        "original_message": "The traditional Wild Swans tale emphasizes sibling loyalty, sacrifice, and perseverance through a difficult task.",
        "adapted_message": "People facing rejection and persecution need compassion and acceptance, and love and loyalty can help people endure suffering.",
        "retelling_type": "Loose retelling"
    }
}

# Verify that the eight uniquely titled books appear exactly once
for title in updates:
    matches = (
        (df["original_tale"] == "The Wild Swans") &
        (df["book_title"] == title)
    )

    if matches.sum() != 1:
        raise ValueError(
            f"Expected exactly one record for '{title}'. "
            "No changes were saved."
        )

# Verify that each duplicate title is identified by its Goodreads ID
for book_id in wild_swans_records:
    matches = (
        (df["original_tale"] == "The Wild Swans") &
        (df["book_title"] == "The Wild Swans") &
        (df["source_url"].astype(str).str.contains(book_id, regex=False))
    )

    if matches.sum() != 1:
        raise ValueError(
            f"Expected exactly one Wild Swans record with Goodreads ID "
            f"{book_id}, but found {matches.sum()}. No changes were saved."
        )

# Check all columns before making changes
all_updates = list(updates.values()) + list(wild_swans_records.values())

for information in all_updates:
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

# Fill the eight uniquely titled records
for title, information in updates.items():
    matches = (
        (df["original_tale"] == "The Wild Swans") &
        (df["book_title"] == title)
    )

    for field, value in information.items():
        current_value = df.loc[matches, field].iloc[0]

        if pd.isna(current_value) or str(current_value).strip() == "":
            df.loc[matches, field] = value

# Fill the two duplicate-title records using their Goodreads IDs
for book_id, information in wild_swans_records.items():
    matches = (
        (df["original_tale"] == "The Wild Swans") &
        (df["book_title"] == "The Wild Swans") &
        (df["source_url"].astype(str).str.contains(book_id, regex=False))
    )

    for field, value in information.items():
        current_value = df.loc[matches, field].iloc[0]

        if pd.isna(current_value) or str(current_value).strip() == "":
            df.loc[matches, field] = value

# Save the updated dataset
df.to_csv(DATA_FILE, index=False)

print("\n--- WILD SWANS RECORDS UPDATED ---")

for title in updates:
    matches = (
        (df["original_tale"] == "The Wild Swans") &
        (df["book_title"] == title)
    )
    row = df.loc[matches].iloc[0]
    print(f"{row['book_title']} | {row['author']} | {row['publication_year']}")

for book_id in wild_swans_records:
    matches = (
        (df["original_tale"] == "The Wild Swans") &
        (df["book_title"] == "The Wild Swans") &
        (df["source_url"].astype(str).str.contains(book_id, regex=False))
    )
    row = df.loc[matches].iloc[0]
    print(
        f"{row['book_title']} ({book_id}) | "
        f"{row['author']} | {row['publication_year']}"
    )

print("\nBackup saved as:", backup_file)
print("Updated dataset saved as:", DATA_FILE)
