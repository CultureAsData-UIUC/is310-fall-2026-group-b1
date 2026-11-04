
import pandas as pd
import shutil
from pathlib import Path
from datetime import datetime

CSV_FILE = Path("fairytale_dataset.csv")

# Each entry fills the research fields for an existing book.
# Format:
# setting, character_changes, protagonist_agency,
# major_themes, original_message, adapted_message, source_url

metadata = {
    # RAPUNZEL
    "Kingdom of Locks": (
        "Fantasy kingdom",
        "Aurelia is stolen as a baby and imprisoned in a tower. "
        "Her long hair stores her captor's magic.",
        "High; Aurelia questions her circumstances and works "
        "toward discovering the truth and gaining freedom.",
        "Freedom, identity, family, courage, and self-discovery",
        "Rapunzel traditionally explores captivity, isolation, "
        "and the possibility of escape.",
        "Personal strength and self-belief can help people "
        "challenge the circumstances imposed on them.",
        "https://deborahgracewhite.com/kingdomtales/"
    ),

    "Rapunzel": (
        "A traditional fairy-tale kingdom",
        "Rapunzel is raised by a witch and confined to a tower "
        "until a prince discovers her.",
        "Moderate; Rapunzel's life is controlled by the witch, "
        "but she participates in the events leading to her escape.",
        "Captivity, love, isolation, freedom, and courage",
        "The traditional story explores the consequences of "
        "confinement and the desire for freedom.",
        "Love and courage can provide a path toward freedom.",
        ""
    ),

    "Golden Curse": (
        "Fantasy kingdom",
        "Persinette Basile is a golden-haired princess affected "
        "by a family curse, forbidden magic, and a tournament.",
        "High; Persinette faces the curse and makes decisions "
        "about her future.",
        "Family, curses, identity, magic, love, and independence",
        "Rapunzel traditionally explores captivity and the "
        "consequences of controlling another person's life.",
        "A person can challenge inherited expectations and "
        "take control of their own destiny.",
        ""
    ),

    "Entangled": (
        "Fantasy world with magical creatures and shifters",
        "Elliana is imprisoned in a tower by a magical gargoyle "
        "and becomes involved in a story of witch's vengeance.",
        "High; Elliana participates in overcoming the dangers "
        "surrounding her imprisonment.",
        "Captivity, vengeance, magic, romance, and freedom",
        "The traditional Rapunzel story explores isolation "
        "and escape from captivity.",
        "Freedom requires confronting the forces that keep "
        "people trapped.",
        ""
    ),

    "The Abandoned Princess": (
        "Fantasy kingdom",
        "Daisy is trapped in a tower and becomes invisible "
        "to most people. Prince Xander helps her confront "
        "her captor's enchantments.",
        "High; Daisy seeks to reclaim her life and break "
        "the enchantments controlling her.",
        "Freedom, identity, courage, love, and self-discovery",
        "Rapunzel traditionally explores isolation and "
        "the desire to escape captivity.",
        "People can reclaim their independence and challenge "
        "the magic or circumstances that control them.",
        ""
    ),

    "Braids of Silver": (
        "Fantasy kingdom with magical Silver Blood characters",
        "Cosette is locked in a tower and encounters a stranger. "
        "Her story involves magical abilities and court conflict.",
        "High; Cosette becomes involved in decisions about "
        "her freedom and her place in the magical world.",
        "Captivity, magic, identity, romance, and belonging",
        "The traditional story explores isolation and "
        "the possibility of escape.",
        "People can find independence and belonging even "
        "after being isolated from the world.",
        ""
    ),

    "Tower of Thorns": (
        "Grimm Academy fantasy setting",
        "The Rapunzel story is reimagined through a magical "
        "academy setting and new characters.",
        "High; the protagonist must navigate the challenges "
        "of the academy and her fairy-tale circumstances.",
        "Magic, identity, independence, romance, and courage",
        "Rapunzel traditionally explores captivity and "
        "the desire for freedom.",
        "People can challenge restrictive circumstances "
        "and determine their own futures.",
        ""
    ),

    "Turret": (
        "Fantasy kingdom",
        "Gemma is imprisoned in a magical turret and develops "
        "a relationship with a guard named Quinn.",
        "High; Gemma's experiences and choices shape "
        "her path toward freedom.",
        "Captivity, trust, love, courage, and independence",
        "The traditional story explores isolation and escape.",
        "Trust and courage can help people overcome "
        "confinement and reclaim their lives.",
        ""
    ),

    "Rootbound": (
        "Fantasy world connected to the events of Tangled",
        "The story revisits Rapunzel and Eugene after she leaves "
        "the tower and loses her healing powers. It introduces "
        "new political conflicts.",
        "High; Rapunzel faces new challenges after her original "
        "story and must navigate political intrigue.",
        "Identity, power, independence, relationships, "
        "and political conflict",
        "Rapunzel's original story focuses on escape "
        "from captivity and gaining independence.",
        "Freedom is not the end of personal growth; "
        "people continue to face challenges after escaping "
        "their original circumstances.",
        ""
    ),

    "Golden": (
        "Fantasy kingdom",
        "A reimagining of Rapunzel that develops the traditional "
        "story through new characters and circumstances.",
        "High; the heroine's choices and experiences shape "
        "her journey beyond confinement.",
        "Love, freedom, identity, courage, and independence",
        "The traditional story explores isolation, captivity, "
        "and escape.",
        "Love and personal courage can help people "
        "find freedom and independence.",
        ""
    ),

    # CINDERELLA
    "The Glass Gate": (
        "A magical faerie kingdom",
        "Ella is an aspiring fashion designer who escapes "
        "her stepfamily's home and enters Faerie. She becomes "
        "the crown prince's fake girlfriend.",
        "High; Ella pursues her education and career goals "
        "while deciding whether to risk her feelings.",
        "Independence, ambition, romance, magic, sacrifice, "
        "and self-discovery",
        "Cinderella traditionally explores mistreatment, "
        "social inequality, and transformation.",
        "Personal ambition and independence can coexist "
        "with romance and love.",
        "https://books.google.com/books?id=EWKqzwEACAAJ"
    ),

    "Ellie and the Prince": (
        "A magical castle and fantasy kingdom",
        "Ellie works as Controller of Magical Creatures "
        "at Faraway Castle. She must work with Prince Omar "
        "to rescue a unicorn.",
        "High; Ellie uses her knowledge and abilities "
        "to protect magical creatures and solve problems.",
        "Responsibility, romance, courage, magical creatures, "
        "and cooperation",
        "Cinderella traditionally explores social inequality, "
        "mistreatment, and changes in social position.",
        "A person's value comes from their actions and abilities, "
        "rather than their social status.",
        ""
    ),

    "The Mystery Princess": (
        "Fantasy kingdom",
        "Daria is an overworked orphan and servant who becomes "
        "involved in danger and a relationship with Prince Percy.",
        "High; Daria must navigate danger and make choices "
        "about her future.",
        "Identity, class, love, courage, and independence",
        "Cinderella traditionally explores hardship, "
        "social inequality, and transformation.",
        "People can overcome restrictive social circumstances "
        "and discover their own worth.",
        ""
    ),

    "The Peasant's Dream": (
        "Historical-inspired fantasy kingdom",
        "Adela is a noblewoman disguised as a peasant, while "
        "Frederick is a poor woodcarver. Their positions "
        "reverse the traditional Cinderella arrangement.",
        "High; Adela makes choices about her identity "
        "and relationship despite social expectations.",
        "Class, identity, love, social expectations, "
        "and sacrifice",
        "Cinderella traditionally explores social class "
        "and the possibility of changing one's circumstances.",
        "Love and personal worth are not determined "
        "by wealth or social position.",
        ""
    ),

    "Kingdom of Cinders": (
        "Fantasy kingdom",
        "A Cinderella retelling that reimagines the heroine "
        "and traditional fairy-tale events in a fantasy setting.",
        "High; the heroine navigates the challenges "
        "of her circumstances and pursues her future.",
        "Love, family, identity, courage, and social class",
        "Cinderella traditionally explores mistreatment "
        "and social inequality.",
        "People can challenge the expectations and limitations "
        "placed on them.",
        ""
    ),

    "Pumpkins and Proms": (
        "Contemporary fantasy setting",
        "A Cinderella retelling that adapts the traditional "
        "ball and transformation elements.",
        "High; the heroine makes choices about her relationships "
        "and experiences.",
        "Romance, transformation, identity, and independence",
        "Cinderella traditionally explores transformation "
        "and the possibility of changing one's circumstances.",
        "A person's future can change through opportunity "
        "and their own choices.",
        ""
    ),

    "A Curse of Ash and Iron": (
        "Steampunk Philadelphia in 1876",
        "The Cinderella story is reimagined through a steampunk "
        "setting, with a heroine navigating social expectations "
        "and a changing technological world.",
        "High; the heroine must make choices about her "
        "circumstances and future.",
        "Class, technology, identity, romance, and independence",
        "Cinderella traditionally explores class inequality "
        "and transformation.",
        "People can challenge social restrictions and "
        "shape their own futures.",
        ""
    ),

    "Ever After": (
        "Historical France",
        "Danielle Cindersoot is mistreated by her stepmother, "
        "Baroness Rodmilla, and develops a relationship "
        "with Prince Henry.",
        "High; Danielle actively challenges injustice "
        "and makes choices about her future.",
        "Class, justice, love, courage, and independence",
        "Cinderella traditionally explores mistreatment, "
        "social inequality, and transformation.",
        "Kindness and courage matter more than social status, "
        "and people can challenge injustice.",
        ""
    ),

    # BABA YAGA
    "Egg & Spoon": (
        "Russian-inspired fantasy setting",
        "Elena and Ekaterina become involved in an adventure "
        "featuring Baba Yaga and her chicken-legged house.",
        "High; the young protagonists participate actively "
        "in the adventure and its challenges.",
        "Class, identity, folklore, magic, friendship, "
        "and adventure",
        "Baba Yaga folklore often explores encounters "
        "with powerful and unpredictable supernatural forces.",
        "Courage and resourcefulness help people navigate "
        "unfamiliar and dangerous situations.",
        ""
    ),

    "Baba Yaga's Assistant": (
        "Magical forest and Baba Yaga's chicken-legged house",
        "Masha applies to become Baba Yaga's assistant "
        "and must complete a series of unusual tests.",
        "High; Masha actively takes on challenges "
        "to prove herself.",
        "Courage, resourcefulness, independence, folklore, "
        "and personal growth",
        "Baba Yaga stories often test the courage "
        "and cleverness of people who encounter her.",
        "Resourcefulness and courage can help someone "
        "succeed in unfamiliar situations.",
        ""
    ),

    "Baba Yaga and Vasilisa the Brave": (
        "Russian folklore setting, including a dark forest "
        "and Baba Yaga's home",
        "Vasilisa is sent into the forest by her jealous "
        "stepmother and stepsisters to seek help from Baba Yaga.",
        "High; Vasilisa relies on courage, intelligence, "
        "and resourcefulness to survive her encounter.",
        "Courage, family conflict, resourcefulness, magic, "
        "and survival",
        "The traditional Vasilisa story explores courage "
        "and cleverness when facing dangerous forces.",
        "Inner strength and resourcefulness help people "
        "overcome cruelty and danger.",
        ""
    ),

    "Finding Baba Yaga": (
        "Contemporary setting with a magical forest "
        "and Baba Yaga's walking house",
        "Natasha escapes her controlling father and encounters "
        "Baba Yaga, beginning a journey of self-discovery.",
        "High; Natasha chooses to leave her restrictive home "
        "and pursue independence.",
        "Independence, identity, family, coming of age, "
        "and self-discovery",
        "Baba Yaga folklore often presents encounters "
        "with the witch as tests of character.",
        "Leaving controlling circumstances can be part "
        "of discovering one's identity and independence.",
        ""
    ),

    "The Witch and the Tsar": (
        "Historical Russia during the reign of Ivan the Terrible",
        "Baba Yaga becomes a central protagonist, portrayed "
        "as a healer and powerful supernatural figure "
        "protecting Anastasia and Russia.",
        "High; Baba Yaga uses her abilities to protect "
        "others and confront supernatural threats.",
        "Power, history, folklore, gender, identity, "
        "and resistance",
        "Traditional Baba Yaga stories portray a powerful "
        "and unpredictable supernatural figure.",
        "Power can be used to protect others and resist "
        "destructive forces.",
        ""
    ),

    "Baba Yaga Laid an Egg": (
        "Contemporary European settings, including Zagreb "
        "and other locations",
        "The novel uses Baba Yaga mythology through three "
        "connected narratives about women, aging, and identity.",
        "Varied; the women navigate personal challenges "
        "and reflect on their experiences and identities.",
        "Aging, femininity, identity, mythology, memory, "
        "and women's experiences",
        "Baba Yaga folklore connects the witch with age, "
        "female power, danger, and transformation.",
        "Mythology can be used to examine women's lives, "
        "aging, and social expectations.",
        ""
    ),

    "Thistlefoot": (
        "Modern-day United States, with connections "
        "to ancestral Russia",
        "Baba Yaga's legacy is explored through siblings "
        "Bellatine and Isaac and their inherited sentient "
        "chicken-legged house.",
        "High; the siblings confront their family's past "
        "and fight to protect their inheritance.",
        "Family, memory, ancestry, trauma, identity, "
        "and storytelling",
        "Baba Yaga folklore explores the power and danger "
        "of supernatural forces and encounters.",
        "People can confront inherited histories and reshape "
        "the legacy they pass on.",
        "https://www.goodreads.com/book/show/60018639-thistlefoot"
    ),

    # THE PIED PIPER OF HAMELIN
    "To Sway a Swindler": (
        "Fantasy kingdom",
        "The Pied Piper becomes As'ad, a con artist who uses "
        "rats to deceive towns. Rahma becomes his determined "
        "traveling companion.",
        "High; Rahma actively searches for her missing friend, "
        "and As'ad chooses to help her.",
        "Redemption, honesty, trust, friendship, "
        "and responsibility",
        "The Pied Piper warns about broken promises "
        "and their consequences.",
        "People can change their behavior and use their "
        "abilities to help others.",
        "https://www.goodreads.com/book/show/229001216-to-sway-a-swindler"
    ),

    "A Fable of Riddles and Redemption": (
        "Fantasy city in the world of Caelia",
        "Combines Pied Piper-inspired disappearances with "
        "Phantom of the Opera-inspired mystery and musical "
        "elements. Zorina and Herrick investigate the events.",
        "High; Zorina and Herrick investigate disappearances "
        "and work together to confront danger.",
        "Redemption, secrets, trust, memory, identity, "
        "and forgiveness",
        "The Pied Piper warns about broken promises; "
        "The Phantom explores alienation and obsession.",
        "People can confront their pasts, seek redemption, "
        "and build a better future.",
        "https://www.goodreads.com/book/show/252840151-a-fable-of-riddles-and-redemption"
    ),
}


def is_blank(value):
    return pd.isna(value) or str(value).strip() == ""


def main():
    if not CSV_FILE.exists():
        print("ERROR: fairytale_dataset.csv not found.")
        print("Check that you are in the correct folder.")
        return

    data = pd.read_csv(CSV_FILE)

    required_columns = [
        "book_title",
        "publication_year",
        "setting",
        "character_changes",
        "protagonist_agency",
        "major_themes",
        "original_message",
        "adapted_message",
        "source_url",
    ]

    for column in required_columns:
        if column not in data.columns:
            data[column] = ""

    # Back up the dataset before making changes.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = Path(f"fairytale_dataset_before_fill_{timestamp}.csv")
    shutil.copy2(CSV_FILE, backup)

    updated_count = 0
    not_found = []
    already_filled = []

    for title, values in metadata.items():
        matches = (
            data["book_title"].astype(str).str.strip().str.casefold()
            == title.casefold()
        )

        if not matches.any():
            not_found.append(title)
            continue

        row_index = data.index[matches][0]

        fields = [
            "setting",
            "character_changes",
            "protagonist_agency",
            "major_themes",
            "original_message",
            "adapted_message",
            "source_url",
        ]

        changed = False

        for field, value in zip(fields, values):
            if value and is_blank(data.at[row_index, field]):
                data.at[row_index, field] = value
                changed = True

        # Fill the Glass Gate year only if it is blank.
        if title == "The Glass Gate":
            if is_blank(data.at[row_index, "publication_year"]):
                data.at[row_index, "publication_year"] = 2022
                changed = True

        if changed:
            updated_count += 1
        else:
            already_filled.append(title)

    data.to_csv(CSV_FILE, index=False)

    print("\n--- METADATA FILL COMPLETE ---")
    print(f"Books updated: {updated_count}")
    print(f"Backup created: {backup}")

    if not_found:
        print("\nBooks not found in CSV:")
        for title in not_found:
            print("-", title)

    if already_filled:
        print("\nAlready had all supplied information:")
        for title in already_filled:
            print("-", title)

    print("\nCSV saved successfully.")


if __name__ == "__main__":
    main()
