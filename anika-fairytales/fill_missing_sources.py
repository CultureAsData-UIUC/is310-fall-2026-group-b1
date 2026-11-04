
import pandas as pd
import shutil
from pathlib import Path
from datetime import datetime

CSV_FILE = Path("fairytale_dataset.csv")

# Verified Goodreads book pages
sources = {
    "Rapunzel":
        "https://www.goodreads.com/book/show/402115.Rapunzel",

    "Golden Curse":
        "https://www.goodreads.com/book/show/42142283-golden-curse",

    "Entangled":
        "https://www.goodreads.com/book/show/40379261-entangled",

    "The Abandoned Princess":
        "https://www.goodreads.com/book/show/201249898-the-abandoned-princess",

    "Braids of Silver":
        "https://www.goodreads.com/book/show/203582921-braids-of-silver",

    "Tower of Thorns":
        "https://www.goodreads.com/book/show/98182314-tower-of-thorns",

    "Turret":
        "https://www.goodreads.com/book/show/59990136-turret",

    "Rootbound":
        "https://www.goodreads.com/book/show/223363643-rootbound",

    "Golden":
        "https://www.goodreads.com/book/show/9683606-golden",

    "Ellie and the Prince":
        "https://www.goodreads.com/book/show/46151157-ellie-and-the-prince",

    "The Mystery Princess":
        "https://www.goodreads.com/book/show/53420360-the-mystery-princess",

    "The Peasant's Dream":
        "https://www.goodreads.com/book/show/50263935-the-peasant-s-dream",

    "Kingdom of Cinders":
        "https://www.goodreads.com/book/show/60030920",

    "Pumpkins and Proms":
        "https://www.goodreads.com/book/show/52371300-pumpkins-and-proms",

    "A Curse of Ash and Iron":
        "https://www.goodreads.com/book/show/123252137-a-curse-of-ash-and-iron",

    "Ever After":
        "https://www.goodreads.com/book/show/15325458-ever-after",

    "Egg & Spoon":
        "https://www.goodreads.com/book/show/20708810",

    "Baba Yaga's Assistant":
        "https://www.goodreads.com/book/show/48644108-baba-yaga-s-assistant",

    "Baba Yaga and Vasilisa the Brave":
        "https://www.goodreads.com/book/show/81807.Baba_Yaga_and_Vasilisa_the_Brave",

    "Finding Baba Yaga":
        "https://www.goodreads.com/book/show/38884174-Finding-Baba-Yaga",

    "The Witch and the Tsar":
        "https://www.goodreads.com/book/show/137978871-the-witch-and-the-tsar",

    "Baba Yaga Laid an Egg":
        "https://www.goodreads.com/book/show/9305472-baba-yaga-laid-an-egg",
}

# Publication years that were missing
years = {
    "Ellie and the Prince": 2018,
    "The Mystery Princess": 2021,
    "The Peasant's Dream": 2020,
}

def blank(value):
    return pd.isna(value) or str(value).strip() == ""

def main():
    if not CSV_FILE.exists():
        print("ERROR: Dataset file not found.")
        return

    data = pd.read_csv(CSV_FILE)

    for column in ["book_title", "source_url", "publication_year"]:
        if column not in data.columns:
            data[column] = ""

    # Create backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = Path(f"fairytale_dataset_before_sources_{timestamp}.csv")
    shutil.copy2(CSV_FILE, backup)

    urls_added = 0
    years_added = 0
    corrections = 0
    not_found = []

    for title, url in sources.items():
        matches = (
            data["book_title"].astype(str).str.strip().str.casefold()
            == title.casefold()
        )

        if not matches.any():
            not_found.append(title)
            continue

        for index in data.index[matches]:
            if blank(data.at[index, "source_url"]):
                data.at[index, "source_url"] = url
                urls_added += 1

    # Fill missing publication years
    for title, year in years.items():
        matches = (
            data["book_title"].astype(str).str.strip().str.casefold()
            == title.casefold()
        )

        if not matches.any():
            if title not in not_found:
                not_found.append(title)
            continue

        for index in data.index[matches]:
            if blank(data.at[index, "publication_year"]):
                data.at[index, "publication_year"] = year
                years_added += 1

    # Correct Golden Curse: Goodreads lists first publication in 2018.
    matches = (
        data["book_title"].astype(str).str.strip().str.casefold()
        == "golden curse"
    )

    for index in data.index[matches]:
        if str(data.at[index, "publication_year"]).strip() == "2019":
            data.at[index, "publication_year"] = 2018
            corrections += 1

    data.to_csv(CSV_FILE, index=False)

    print("\n--- SOURCE AND YEAR UPDATE COMPLETE ---")
    print(f"Source URLs added: {urls_added}")
    print(f"Publication years added: {years_added}")
    print(f"Publication years corrected: {corrections}")
    print(f"Backup created: {backup}")

    if not_found:
        print("\nTitles not found:")
        for title in not_found:
            print("-", title)

    print("\nDataset saved successfully!")

if __name__ == "__main__":
    main()
