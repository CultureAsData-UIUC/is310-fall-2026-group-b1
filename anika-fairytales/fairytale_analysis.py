"""
IS 310 Culture As Data: Fairy-Tale Retellings Analysis
-----------------------------------------------------
Place this script in the same folder as fairytale_dataset.csv.

Run from PowerShell:
    py fairytale_analysis.py

Requirements:
    py -m pip install pandas matplotlib

The script reads the 62-book dataset, fills the known Fairytalez ranking
for each tale in the analysis copy, prints summary tables, and saves
CSV tables and PNG charts in an "analysis_output" folder.

It does not overwrite the original dataset.
"""

from pathlib import Path
import re
import pandas as pd
import matplotlib.pyplot as plt


# Locate the CSV beside this Python file.
PROJECT_FOLDER = Path(__file__).resolve().parent
INPUT_FILE = PROJECT_FOLDER / "fairytale_dataset.csv"
OUTPUT_FOLDER = PROJECT_FOLDER / "analysis_output"

# Fairytalez "Top 100 Most Popular Fairy Tales" ranks used in this project.
TALE_RANKS = {
    "Rapunzel": 2,
    "Cinderella": 3,
    "Baba Yaga": 20,
    "The Pied Piper of Hamelin": 79,
    "The Wild Swans": 85,
}

EXPECTED_COUNTS = {
    "Rapunzel": 15,
    "Cinderella": 15,
    "Baba Yaga": 12,
    "The Wild Swans": 10,
    "The Pied Piper of Hamelin": 10,
}


def clean_text(value):
    """Return a normalized string, or an empty string for missing values."""
    if pd.isna(value):
        return ""
    return str(value).strip()


def save_table(dataframe, filename):
    """Save a dataframe as a CSV in the output folder."""
    dataframe.to_csv(OUTPUT_FOLDER / filename, index=True)


def main():
    if not INPUT_FILE.exists():
        print(f"ERROR: Could not find {INPUT_FILE.name}.")
        print("Put fairytale_dataset.csv in the same folder as this script.")
        return

    OUTPUT_FOLDER.mkdir(exist_ok=True)

    df = pd.read_csv(INPUT_FILE)

    required_columns = [
        "original_tale",
        "book_title",
        "author",
        "publication_year",
        "setting",
        "character_changes",
        "protagonist_agency",
        "major_themes",
        "original_message",
        "adapted_message",
        "retelling_type",
    ]

    missing_columns = [column for column in required_columns if column not in df.columns]
    if missing_columns:
        print("ERROR: The dataset is missing required columns:")
        for column in missing_columns:
            print(f" - {column}")
        return

    # Normalize the tale names and fill ranks only in this in-memory copy.
    df["original_tale"] = df["original_tale"].map(clean_text)
    if "fairytalez_rank" not in df.columns:
        df["fairytalez_rank"] = pd.NA

    df["fairytalez_rank"] = df.apply(
        lambda row: TALE_RANKS.get(row["original_tale"], row["fairytalez_rank"]),
        axis=1,
    )

    # Convert publication years to numbers where possible.
    df["publication_year"] = pd.to_numeric(df["publication_year"], errors="coerce")

    # 1. Overall sample size and count by fairy tale.
    tale_counts = (
        df.groupby("original_tale")
        .size()
        .rename("book_count")
        .to_frame()
    )
    tale_counts["fairytalez_rank"] = tale_counts.index.map(TALE_RANKS)
    tale_counts["expected_target"] = tale_counts.index.map(EXPECTED_COUNTS)
    tale_counts["matches_target"] = (
        tale_counts["book_count"] == tale_counts["expected_target"]
    )
    tale_counts = tale_counts.sort_values("fairytalez_rank")
    save_table(tale_counts, "book_counts_by_tale.csv")

    # 2. Retelling type counts and percentages.
    type_counts = (
        df.groupby(["original_tale", "retelling_type"], dropna=False)
        .size()
        .unstack(fill_value=0)
    )
    type_counts["Total books"] = type_counts.sum(axis=1)
    type_counts = type_counts.reindex(tale_counts.index)
    save_table(type_counts, "retelling_types_by_tale.csv")

    overall_types = (
        df["retelling_type"]
        .fillna("Unclassified")
        .value_counts()
        .rename_axis("retelling_type")
        .to_frame("book_count")
    )
    overall_types["percentage"] = (
        overall_types["book_count"] / len(df) * 100
    ).round(1)
    save_table(overall_types, "overall_retelling_types.csv")

    # 3. Publication-year summary.
    year_summary = (
        df.groupby("original_tale")["publication_year"]
        .agg(["count", "min", "median", "max"])
        .rename(columns={
            "count": "books_with_year",
            "min": "earliest_year",
            "median": "median_year",
            "max": "latest_year",
        })
        .reindex(tale_counts.index)
    )
    save_table(year_summary, "publication_year_summary.csv")

    # 4. Count recurring theme terms. The themes field is interpretive text;
    # this simple split is a rough descriptive aid, not automated interpretation.
    theme_rows = []
    for _, row in df.iterrows():
        tale = row["original_tale"]
        themes = clean_text(row["major_themes"])
        if not themes:
            continue
        for term in re.split(r"[,;|]", themes):
            term = term.strip().lower()
            if term:
                theme_rows.append((tale, term))

    if theme_rows:
        theme_data = pd.DataFrame(theme_rows, columns=["original_tale", "theme"])
        theme_counts = (
            theme_data.groupby(["original_tale", "theme"])
            .size()
            .rename("mentions")
            .reset_index()
            .sort_values(["original_tale", "mentions"], ascending=[True, False])
        )
        theme_counts.to_csv(OUTPUT_FOLDER / "theme_terms_by_tale.csv", index=False)

        overall_themes = (
            theme_data["theme"].value_counts()
            .rename_axis("theme")
            .to_frame("mentions")
        )
        overall_themes.to_csv(OUTPUT_FOLDER / "overall_theme_terms.csv")

    # 5. Save a copy with the five known popularity ranks filled in.
    # The original fairytale_dataset.csv is never changed.
    df.to_csv(OUTPUT_FOLDER / "fairytale_dataset_with_ranks.csv", index=False)

    # 6. Chart: number of sampled books per fairy tale.
    chart_counts = tale_counts["book_count"].sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    chart_counts.plot(kind="bar")
    plt.title("Books in the Sample by Original Fairy Tale")
    plt.xlabel("Original fairy tale")
    plt.ylabel("Number of books")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_FOLDER / "books_by_fairy_tale.png", dpi=200)
    plt.close()

    # 7. Chart: overall retelling type distribution.
    plt.figure(figsize=(10, 6))
    overall_types["book_count"].sort_values(ascending=False).plot(kind="bar")
    plt.title("Retelling Types Across All Books")
    plt.xlabel("Retelling type")
    plt.ylabel("Number of books")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_FOLDER / "retelling_types.png", dpi=200)
    plt.close()

    # 8. Chart: stacked retelling types by tale.
    plot_types = type_counts.drop(columns=["Total books"], errors="ignore")
    plot_types.plot(kind="bar", stacked=True, figsize=(11, 7))
    plt.title("Retelling Types by Fairy Tale")
    plt.xlabel("Original fairy tale")
    plt.ylabel("Number of books")
    plt.xticks(rotation=25, ha="right")
    plt.legend(title="Retelling type", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(OUTPUT_FOLDER / "retelling_types_by_tale.png", dpi=200)
    plt.close()

    # Print a readable report in PowerShell.
    print("\n--- DATASET OVERVIEW ---")
    print(f"Total books: {len(df)}")
    print(f"Number of fairy tales: {df['original_tale'].nunique()}")
    print(f"Columns: {len(df.columns)}")

    print("\n--- BOOK COUNTS BY FAIRY TALE ---")
    print(tale_counts.to_string())

    print("\n--- RETELLING TYPES BY FAIRY TALE ---")
    print(type_counts.to_string())

    print("\n--- OVERALL RETELLING TYPE COUNTS ---")
    print(overall_types.to_string())

    print("\n--- PUBLICATION YEAR SUMMARY ---")
    print(year_summary.to_string())

    print("\n--- MISSING INFORMATION CHECK ---")
    fields_to_check = [
        "book_title", "author", "publication_year", "medium", "setting",
        "character_changes", "protagonist_agency", "major_themes",
        "original_message", "adapted_message", "source_url", "retelling_type",
    ]
    missing_total = 0
    for field in fields_to_check:
        missing_count = df[field].isna().sum()
        if df[field].dtype == "object":
            missing_count += (df[field].fillna("").astype(str).str.strip() == "").sum()
        if missing_count:
            missing_total += missing_count
            print(f"{field}: {missing_count} missing")
    if missing_total == 0:
        print("No missing information in the checked fields.")

    print("\n--- OUTPUT FILES ---")
    print(f"All analysis files were saved in: {OUTPUT_FOLDER}")
    print("Original dataset was not modified.")


if __name__ == "__main__":
    main()
