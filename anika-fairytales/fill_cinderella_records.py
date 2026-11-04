
import pandas as pd
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("fairytale_dataset.csv")

if not DATA_FILE.exists():
    raise FileNotFoundError("fairytale_dataset.csv was not found.")

df = pd.read_csv(DATA_FILE)

updates = {
    "Cinder": {
        "author": "Marissa Meyer",
        "publication_year": 2012,
        "setting": "New Beijing, a futuristic city in a world recovering from World War IV",
        "character_changes": "Cinderella becomes Cinder, a cyborg mechanic who is treated as a second-class citizen. She becomes involved in a political conflict involving Prince Kai, a deadly plague, and the Lunar people.",
        "protagonist_agency": "High. Cinder uses her mechanical skills, investigates her past, and makes difficult decisions that affect the future of Earth.",
        "major_themes": "Identity, discrimination, freedom, technology, responsibility, courage, and belonging",
        "original_message": "The traditional Cinderella story emphasizes kindness, perseverance, and the possibility of a better life despite mistreatment.",
        "adapted_message": "A person's identity and worth are not determined by social status or physical differences, and individuals can shape their own futures.",
        "retelling_type": "Loose retelling"
    },

    "Ella Enchanted": {
        "author": "Gail Carson Levine",
        "publication_year": 1997,
        "setting": "The fantasy kingdom of Kyrria, with castles, villages, ogres, and giants",
        "character_changes": "Ella is given a curse of obedience by a fairy at birth. Rather than simply accepting her circumstances, she searches for a way to break the curse and control her own life.",
        "protagonist_agency": "High. Ella actively searches for a cure, challenges unfair expectations, and ultimately breaks her curse herself.",
        "major_themes": "Free will, independence, identity, love, courage, and challenging expectations",
        "original_message": "The traditional Cinderella story emphasizes kindness and perseverance through mistreatment, followed by a chance for a better life.",
        "adapted_message": "True independence means having control over your own choices, and courage can mean refusing to accept unfair expectations.",
        "retelling_type": "Direct retelling"
    },

    "Princess of Glass": {
        "author": "Jessica Day George",
        "publication_year": 2010,
        "setting": "A fantasy world inspired by early nineteenth-century England, including the kingdoms of Westfalin and Ionia",
        "character_changes": "The story follows Princess Poppy and a servant named Eleanor, who becomes involved in a Cinderella-like situation after a fairy godmother interferes with their lives.",
        "protagonist_agency": "Moderate to high. Eleanor and Poppy make decisions about their futures, relationships, and responsibilities rather than simply waiting for rescue.",
        "major_themes": "Love, jealousy, political alliances, identity, friendship, and responsibility",
        "original_message": "The traditional Cinderella story emphasizes kindness, perseverance, and hope despite mistreatment.",
        "adapted_message": "People should be valued for who they are rather than their status, appearance, or social position.",
        "retelling_type": "Direct retelling"
    },

    "Cinderella and the Colonel": {
        "author": "K.M. Shea",
        "publication_year": 2014,
        "setting": "A fantasy kingdom recovering from war and a hostile takeover",
        "character_changes": "Cinderella is an orphaned duchess who disguises herself as a servant to protect her lands and people. She develops a relationship with Colonel Friedrich, who belongs to the country occupying hers.",
        "protagonist_agency": "High. Cinderella works to protect her people, manage her financial problems, and make decisions about her future and relationship with Friedrich.",
        "major_themes": "Love, sacrifice, independence, political conflict, loyalty, forgiveness, and responsibility",
        "original_message": "The traditional Cinderella story emphasizes kindness and perseverance despite mistreatment, eventually leading to a better future.",
        "adapted_message": "Strength and compassion can help people overcome hardship, and understanding between opposing groups can create change.",
        "retelling_type": "Direct retelling"
    },

    "The Coronation Ball": {
        "author": "Melanie Cellier",
        "publication_year": 2020,
        "setting": "The fictional kingdom of Northhelm, especially the palace kitchens and royal court",
        "character_changes": "The story follows Hanna, the sister of Hans, as she works toward becoming a pastry chef and develops a relationship with Stefan. Its Cinderella connection comes through its fairy-tale setting and Cinderella-inspired storyline.",
        "protagonist_agency": "High. Hanna works toward her career goals and must decide whether to stand up for herself and pursue the future she wants.",
        "major_themes": "Independence, hard work, love, ambition, self-worth, and overcoming obstacles",
        "original_message": "The traditional Cinderella story emphasizes hope and perseverance despite difficult circumstances.",
        "adapted_message": "People can build better futures by believing in their abilities and standing up for themselves.",
        "retelling_type": "Loose retelling"
    },

    "Shard of Glass": {
        "author": "Emily Deady",
        "publication_year": 2020,
        "setting": "A small fantasy kingdom with a royal palace and coastal surroundings",
        "character_changes": "Ashlin, once a noblewoman, becomes a palace servant after her family's finances collapse. She uses her sewing skills and develops a relationship with Prince Onric while magical threats endanger the kingdom.",
        "protagonist_agency": "High. Ashlin uses her own skills to help protect the kingdom and makes difficult choices about her family and relationship with the prince.",
        "major_themes": "Family, selflessness, love, identity, responsibility, magic, and personal strength",
        "original_message": "The traditional Cinderella story emphasizes kindness and perseverance despite mistreatment.",
        "adapted_message": "A person's worth comes from their character and abilities, not their social position, and selflessness should not mean giving up one's own future.",
        "retelling_type": "Direct retelling"
    },

    "Cinders of Glass": {
        "author": "Celeste Baxendell",
        "publication_year": 2022,
        "setting": "A fantasy kingdom with a royal court, marketplace, and enchanted objects",
        "character_changes": "Liora lives with her stepmother and stepsisters after her father is cast out as a traitor. She sells enchanted matches and becomes involved in a conflict surrounding Prince Cynrik and a visiting princess.",
        "protagonist_agency": "High. Liora takes action to protect her family and becomes involved in uncovering a dangerous plot.",
        "major_themes": "Family, loyalty, sacrifice, identity, love, betrayal, and responsibility",
        "original_message": "Cinderella emphasizes kindness and perseverance, while The Little Match Girl highlights poverty, suffering, and compassion.",
        "adapted_message": "Family loyalty and compassion matter, but people must also make difficult choices to protect themselves and others.",
        "retelling_type": "Multi-tale adaptation"
    },

    "Cinders, Stars, and Glass Slippers": {
        "author": "Brittany Fichter",
        "publication_year": 2017,
        "setting": "The fantasy kingdom of Ashland, with royal courts, castles, and political conflict",
        "character_changes": "Elaina grows up aboard her father's ship after her mother's death. She has military knowledge and magical abilities, and her relationship with Prince Nicholas develops as the kingdom faces a possible civil war.",
        "protagonist_agency": "High. Elaina makes decisions about her safety, uses her skills to help others, and takes an active role in the kingdom's conflict.",
        "major_themes": "Love, courage, independence, family, sacrifice, magic, and political conflict",
        "original_message": "The traditional Cinderella story emphasizes kindness, perseverance, and hope for a better future.",
        "adapted_message": "A strong relationship involves mutual respect, and people can shape their own futures through courage and their abilities.",
        "retelling_type": "Direct retelling"
    }
}

# Verify that every book appears exactly once under Cinderella
for title in updates:
    matches = (
        (df["original_tale"] == "Cinderella") &
        (df["book_title"] == title)
    )

    if matches.sum() != 1:
        raise ValueError(
            f"Expected exactly one Cinderella record for '{title}'. "
            "No changes were saved."
        )

# Check required columns before making changes
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
        (df["original_tale"] == "Cinderella") &
        (df["book_title"] == title)
    )

    for field, value in information.items():
        current_value = df.loc[matches, field].iloc[0]

        if pd.isna(current_value) or str(current_value).strip() == "":
            df.loc[matches, field] = value

# Save the updated dataset
df.to_csv(DATA_FILE, index=False)

print("\n--- CINDERELLA RECORDS UPDATED ---")

for title in updates:
    matches = (
        (df["original_tale"] == "Cinderella") &
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
