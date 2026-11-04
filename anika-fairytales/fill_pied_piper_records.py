
import pandas as pd
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("fairytale_dataset.csv")

if not DATA_FILE.exists():
    raise FileNotFoundError("fairytale_dataset.csv was not found.")

df = pd.read_csv(DATA_FILE)

updates = {
    "After Hamelin": {
        "author": "Bill Richardson",
        "publication_year": 2000,
        "setting": "The fictional town of Hamelin and a magical dream world containing the Piper's mountain fortress",
        "character_changes": "Penelope is the only child who escapes the Piper's music because she becomes deaf. Years later, she remembers her childhood adventure and explains how she used deep dreaming to enter the dream world and rescue the missing children.",
        "protagonist_agency": "High. Penelope chooses to enter the dream world and uses her unusual ability, courage, and friendships to rescue the children.",
        "major_themes": "Courage, friendship, disability, imagination, family, memory, and perseverance",
        "original_message": "The traditional Pied Piper story warns about broken promises and the consequences of failing to honor agreements.",
        "adapted_message": "Even after a terrible loss, courage, friendship, and determination can help people recover what was taken from them.",
        "retelling_type": "Continuation"
    },

    "Silent Melody": {
        "author": "Alice Ivinya",
        "publication_year": 2021,
        "setting": "Thirteenth-century Germany, including Hamelin and a magical kingdom ruled by the Heartless Queen",
        "character_changes": "Adelaide is a deaf girl who cannot hear the Pied Piper's music. When her younger sister and the other children disappear, she teams up with a blind girl and eventually the Piper himself to try to rescue them.",
        "protagonist_agency": "High. Adelaide uses her abilities, courage, and intelligence to search for the missing children and challenge the Heartless Queen.",
        "major_themes": "Disability, identity, courage, family, friendship, trust, self-worth, and love",
        "original_message": "The traditional Pied Piper story emphasizes the consequences of broken promises and the danger of following a mysterious stranger.",
        "adapted_message": "Differences do not make someone less capable, and courage and determination can turn perceived weaknesses into strengths.",
        "retelling_type": "Direct retelling"
    },

    "Wild Magic": {
        "author": "Cat Weatherill",
        "publication_year": 2007,
        "setting": "Hamelin and the magical world of Elvendale",
        "character_changes": "Mari and her brother Jakob follow the Pied Piper's enchanted music into Elvendale. They discover that the Piper is an elf suffering from a centuries-old curse that transforms him into a dangerous beast.",
        "protagonist_agency": "High. Mari and Jakob must make decisions, face dangerous creatures, and find a way to survive the magical world and deal with the Piper's curse.",
        "major_themes": "Family, magic, curses, identity, danger, courage, and sacrifice",
        "original_message": "The traditional Pied Piper story warns about broken promises and the danger of allowing a mysterious stranger to lead children away.",
        "adapted_message": "People's actions can have lasting consequences, and breaking a curse may require difficult choices and sacrifice.",
        "retelling_type": "Direct retelling"
    },

    "The Last Child of Hamelin": {
        "author": "Ray Ballantyne",
        "publication_year": 2014,
        "setting": "Hamelin and the mysterious Koppelberg Mountain, approximately sixty years after the original disappearance",
        "character_changes": "Pieter grows up in a town still suffering from the loss of its children. He discovers that he can hear the Piper's music and becomes connected to the mystery of the missing children. He works with Old Simon, who was left behind when the Piper took the others.",
        "protagonist_agency": "High. Pieter investigates the Piper's music, develops his musical abilities, and helps uncover the mystery of what happened to the missing children.",
        "major_themes": "Music, memory, hope, family, friendship, mystery, and healing",
        "original_message": "The traditional Pied Piper story warns about broken promises and the consequences of betrayal.",
        "adapted_message": "Even when a community has experienced tragedy, hope and cooperation can help people confront the past and find a way forward.",
        "retelling_type": "Continuation"
    },

    "The Enchanted Sonata": {
        "author": "Heather Dixon Wallwork",
        "publication_year": 2018,
        "setting": "A magical empire filled with palaces, fairies, enormous rats, and a prince",
        "character_changes": "Clara Stahlbaum receives a magical nutcracker and is transported into an enchanted world. She encounters a magician who uses music as magic, combining elements of The Nutcracker with the Pied Piper legend.",
        "protagonist_agency": "High. Clara must confront the magician, navigate the unfamiliar magical world, and reconsider the future she originally planned for herself.",
        "major_themes": "Music, love, independence, courage, magic, identity, and self-discovery",
        "original_message": "The Pied Piper story warns about broken promises and the consequences of manipulation, while The Nutcracker explores imagination and transformation.",
        "adapted_message": "People can discover new possibilities when they move beyond their expectations and make their own choices.",
        "retelling_type": "Multi-tale adaptation"
    },

    "The Piper's Pursuit": {
        "author": "Melanie Dickerson",
        "publication_year": 2019,
        "setting": "Hamlin in 1424, in the German region of the Holy Roman Empire",
        "character_changes": "Katerina is a warrior-minded young woman determined to protect her town from a dangerous beast and her abusive stepfather. She teams up with Steffan, a duke's son, as children begin disappearing and the Pied Piper legend unfolds.",
        "protagonist_agency": "High. Katerina actively investigates the danger, protects her community, and refuses to let others decide her future.",
        "major_themes": "Courage, faith, forgiveness, romance, freedom, family, and responsibility",
        "original_message": "The traditional Pied Piper story emphasizes the consequences of broken promises and the danger of betraying a community.",
        "adapted_message": "Courage, forgiveness, and cooperation can help people overcome oppression and protect others.",
        "retelling_type": "Direct retelling"
    },

    "A Piper's Song": {
        "author": "C.K. Johnson",
        "publication_year": 2015,
        "setting": "A modern-day world with a hidden community of people descended from the original Pied Piper",
        "character_changes": "Kyra discovers that she is descended from the Pied Piper and has inherited the ability to control people through music. After accidentally using her power on someone at school, she must learn to control it and understand her family's history.",
        "protagonist_agency": "High. Kyra actively works to control her abilities, makes decisions about her family's expectations, and determines how she wants to use her powers.",
        "major_themes": "Identity, family, responsibility, music, self-control, belonging, and growing up",
        "original_message": "The traditional Pied Piper story warns about the dangerous power of music and the consequences of broken promises.",
        "adapted_message": "Having inherited power does not determine how someone must use it; individuals are responsible for their own choices.",
        "retelling_type": "Loose retelling"
    },

    "Songs of Stone": {
        "author": "Celeste Baxendell",
        "publication_year": 2022,
        "setting": "A magical fantasy kingdom with royal courts, enchanted landscapes, and supernatural disasters",
        "character_changes": "Piper works for the Red Enchanter and uses an enchanted fife to control people, create storms, and kidnap children. Prince Valens investigates mysterious disasters and becomes involved in Piper's life as he tries to understand her actions.",
        "protagonist_agency": "High. Piper must decide whether to continue obeying the Red Enchanter or resist him, while Valens independently investigates the disasters and searches for the truth.",
        "major_themes": "Freedom, responsibility, identity, redemption, love, trust, magic, and sacrifice",
        "original_message": "The traditional Pied Piper story warns about the misuse of power and the consequences of broken promises.",
        "adapted_message": "People can choose to change their actions, take responsibility for past mistakes, and work toward a better future.",
        "retelling_type": "Multi-tale adaptation"
    }
}

# Verify every book appears exactly once under The Pied Piper of Hamelin
for title in updates:
    matches = (
        (df["original_tale"] == "The Pied Piper of Hamelin") &
        (df["book_title"] == title)
    )

    if matches.sum() != 1:
        raise ValueError(
            f"Expected exactly one record for '{title}'. "
            "No changes were saved."
        )

# Verify required columns
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
        (df["original_tale"] == "The Pied Piper of Hamelin") &
        (df["book_title"] == title)
    )

    for field, value in information.items():
        current_value = df.loc[matches, field].iloc[0]

        if pd.isna(current_value) or str(current_value).strip() == "":
            df.loc[matches, field] = value

# Save the dataset
df.to_csv(DATA_FILE, index=False)

print("\n--- PIED PIPER RECORDS UPDATED ---")

for title in updates:
    matches = (
        (df["original_tale"] == "The Pied Piper of Hamelin") &
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
