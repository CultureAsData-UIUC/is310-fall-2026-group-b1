
import pandas as pd
import os

# ==========================================
# FAIRY TALE RETELLING DATASET
# ==========================================

DATA_FILE = "fairytale_dataset.csv"
COUNTS_FILE = "fairytale_retelling_counts.csv"
VISIBILITY_FILE = "fairytale_visibility_comparison.csv"

COLUMNS = [
    "adaptation_id",
    "original_tale",
    "fairytalez_rank",
    "book_title",
    "author",
    "publication_year",
    "medium",
    "setting",
    "character_changes",
    "protagonist_agency",
    "major_themes",
    "original_message",
    "adapted_message",
    "source_url",
    "retelling_type"
]

RETELLING_TYPES = [
    "Direct retelling",
    "Loose retelling",
    "Folklore-inspired",
    "Multi-tale adaptation",
    "Continuation",
    "Uncertain"
]


# ==========================================
# LOAD AND SAVE DATA
# ==========================================

def load_data():

    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE, dtype=str).fillna("")

        # Add any new columns without deleting old data.
        for column in COLUMNS:
            if column not in df.columns:
                df[column] = ""

        # Keep the expected column order.
        df = df[COLUMNS]

        # Existing books without classifications remain uncertain.
        df["retelling_type"] = df["retelling_type"].replace(
            "", "Uncertain"
        )

        return df

    return pd.DataFrame(columns=COLUMNS)


def save_data(df):

    df.to_csv(DATA_FILE, index=False, encoding="utf-8")

    print("\nDataset saved successfully!")


# ==========================================
# GENERATE ADAPTATION IDS
# ==========================================

def generate_id(df):

    if df.empty:
        return "A001"

    ids = pd.to_numeric(
        df["adaptation_id"].str.replace("A", "", regex=False),
        errors="coerce"
    )

    next_id = int(ids.max()) + 1 if ids.notna().any() else 1

    return f"A{next_id:03d}"


# ==========================================
# ADD A BOOK
# ==========================================

def add_book(df):

    print("\n--- ADD A BOOK ADAPTATION ---")

    new_book = {}

    new_book["adaptation_id"] = generate_id(df)

    new_book["original_tale"] = input(
        "Original fairy tale: "
    ).strip()

    new_book["fairytalez_rank"] = input(
        "Fairytalez popularity rank (leave blank if unknown): "
    ).strip()

    new_book["book_title"] = input(
        "Book title: "
    ).strip()

    new_book["author"] = input(
        "Author: "
    ).strip()

    new_book["publication_year"] = input(
        "Publication year: "
    ).strip()

    new_book["medium"] = input(
        "Medium (novel, picture book, etc.): "
    ).strip()

    new_book["setting"] = input(
        "Setting of the adaptation: "
    ).strip()

    new_book["character_changes"] = input(
        "Changes to characters: "
    ).strip()

    new_book["protagonist_agency"] = input(
        "How much agency does the protagonist have?: "
    ).strip()

    new_book["major_themes"] = input(
        "Major themes (separate with commas): "
    ).strip()

    new_book["original_message"] = input(
        "Message of the original fairy tale: "
    ).strip()

    new_book["adapted_message"] = input(
        "Message of the adaptation: "
    ).strip()

    new_book["source_url"] = input(
        "Goodreads or other source URL: "
    ).strip()

    print("\nRetelling categories:")

    for i, category in enumerate(RETELLING_TYPES, start=1):
        print(f"{i}. {category}")

    while True:
        choice = input("Choose a category (1-5): ").strip()

        if choice in ["1", "2", "3", "4", "5", "6"]:
            new_book["retelling_type"] = RETELLING_TYPES[
                int(choice) - 1
            ]
            break

        print("Please enter a number from 1 to 6.")

    # Check for possible duplicates.
    if not df.empty:

        duplicate = df[
            (df["book_title"].str.lower() == new_book["book_title"].lower())
            &
            (df["author"].str.lower() == new_book["author"].lower())
        ]

        if not duplicate.empty:

            print("\nWARNING: This title and author already exist.")

            confirm = input(
                "Add it anyway? (y/n): "
            ).strip().lower()

            if confirm != "y":
                print("Book not added.")
                return df

    new_row = pd.DataFrame([new_book])

    df = pd.concat([df, new_row], ignore_index=True)

    save_data(df)

    print(
        f"\nAdded {new_book['book_title']} "
        f"with ID {new_book['adaptation_id']}."
    )

    return df


# ==========================================
# VIEW ALL BOOKS
# ==========================================

def view_books(df):

    print("\n--- CURRENT DATASET ---")

    if df.empty:
        print("No books have been entered yet.")
        return

    print(
        df[
            [
                "adaptation_id",
                "original_tale",
                "book_title",
                "author",
                "publication_year",
                "retelling_type"
            ]
        ].to_string(index=False)
    )


# ==========================================
# CHECK MISSING INFORMATION
# ==========================================


def check_missing(df):

    print("\n--- MISSING INFORMATION CHECK ---")

    if df.empty:
        print("No records to check.")
        return

    fields_to_check = [
        "author",
        "publication_year",
        "medium",
        "setting",
        "character_changes",
        "protagonist_agency",
        "major_themes",
        "original_message",
        "adapted_message",
        "source_url",
        "retelling_type"
    ]

    missing_records = []

    for _, row in df.iterrows():

        missing_fields = [
            field for field in fields_to_check
            if pd.isna(row[field]) or str(row[field]).strip() == ""
        ]

        if missing_fields:
            missing_records.append({
                "book_title": row["book_title"],
                "missing_fields": ", ".join(missing_fields)
            })

    if missing_records:
        results = pd.DataFrame(missing_records)
        print(results.to_string(index=False))

    else:
        print("No missing information!")

    print(
        "\nBooks needing additional information:",
        len(missing_records)
    )

# ==========================================
# CHECK DUPLICATES
# ==========================================

def check_duplicates(df):

    print("\n--- DUPLICATE CHECK ---")

    if df.empty:
        print("No records to check.")
        return

    duplicates = df[
        df.duplicated(
            subset=["book_title", "author"],
            keep=False
        )
    ]

    if duplicates.empty:
        print("No duplicate title-author combinations found.")

    else:
        print("Possible duplicates found:")

        print(
            duplicates[
                ["book_title", "author", "original_tale"]
            ].to_string(index=False)
        )

    print(
        "\nNote: Different editions should be checked manually. "
        "Do not count the same adaptation twice."
    )


# ==========================================
# COUNT RETELLINGS BY FAIRY TALE
# ==========================================

def count_retellings(df):

    print("\n--- BOOK COUNTS BY FAIRY TALE ---")

    if df.empty:
        print("No records to count.")
        return

    counts = pd.crosstab(
        df["original_tale"],
        df["retelling_type"]
    )

    # Include categories even if there are no records in them.
    counts = counts.reindex(
        columns=RETELLING_TYPES,
        fill_value=0
    )

    counts["Total books"] = counts.sum(axis=1)

    print(counts.to_string())

    counts.to_csv(COUNTS_FILE)

    print(f"\nResults saved to {COUNTS_FILE}")


# ==========================================
# FAIRY TALE VISIBILITY CATEGORIES
# ==========================================

def get_visibility(rank):

    try:
        rank = int(rank)
    except (ValueError, TypeError):
        return "Unknown"

    if 1 <= rank <= 15:
        return "High visibility"

    elif 16 <= rank <= 50:
        return "Medium visibility"

    elif 51 <= rank <= 100:
        return "Lower visibility"

    return "Unknown"


# ==========================================
# COMPARE VISIBILITY AND RETELLING TYPES
# ==========================================

def compare_visibility(df):

    print("\n--- FAIRY TALE VISIBILITY COMPARISON ---")

    if df.empty:
        print("No records to compare.")
        return

    df = df.copy()

    df["visibility_category"] = df[
        "fairytalez_rank"
    ].apply(get_visibility)

    comparison = pd.crosstab(
        df["visibility_category"],
        df["retelling_type"]
    )

    comparison = comparison.reindex(
        index=[
            "High visibility",
            "Medium visibility",
            "Lower visibility"
        ],
        columns=RETELLING_TYPES,
        fill_value=0
    )

    comparison["Total books"] = comparison.sum(axis=1)

    print(comparison.to_string())

    comparison.to_csv(VISIBILITY_FILE)

    print(f"\nResults saved to {VISIBILITY_FILE}")

    print(
        "\nNote: Fairytalez popularity rankings measure website "
        "visibility, not the total number of adaptations worldwide."
    )


# ==========================================
# MAIN MENU
# ==========================================

def main():

    df = load_data()

    print("======================================")
    print("      FAIRY TALE RETELLING DATASET")
    print("======================================")

    while True:

        print("\nMAIN MENU")
        print("1. Add a book adaptation")
        print("2. View all books")
        print("3. Check missing information")
        print("4. Check duplicate books")
        print("5. Count books by fairy tale")
        print("6. Compare popularity and retelling types")
        print("7. Save and exit")

        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            df = add_book(df)

        elif choice == "2":
            view_books(df)

        elif choice == "3":
            check_missing(df)

        elif choice == "4":
            check_duplicates(df)

        elif choice == "5":
            count_retellings(df)

        elif choice == "6":
            compare_visibility(df)

        elif choice == "7":
            save_data(df)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 7.")


# ==========================================
# RUN PROGRAM
# ==========================================

if __name__ == "__main__":
    main()
