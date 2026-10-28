import csv

# Erin Chon - IS 310 Milestone 2
# German Folklore and National Identity

tales = [
    [1, "The Frog King"],
    [15, "Hansel and Gretel"],
    [21, "Cinderella"],
    [26, "Little Red Riding Hood"],
    [50, "Sleeping Beauty"],
    [53, "Snow White"],
    [55, "Rumpelstiltskin"]
]

# Create the dataset
with open("grimm_folklore_dataset.csv", "w",
          newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "khm_number",
        "title",
        "tale_type",
        "documented_source",
        "source_region",
        "cross_cultural_connection",
        "origin_certainty",
        "origin_notes",
        "source_citation"
    ])

    for khm, title in tales:
        writer.writerow([
            khm,
            title,
            "not_yet_coded",
            "unknown",
            "unknown",
            "not_yet_researched",
            "unknown",
            "",
            ""
        ])

print("Dataset created successfully!")
print("Total tales:", len(tales))
