import csv
from collections import Counter

with open("grimm_folklore_dataset.csv",
          encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

print("Total stories:", len(data))

khm_numbers = [row["khm_number"] for row in data]
duplicates = len(khm_numbers) - len(set(khm_numbers))

print("Duplicate KHM numbers:", duplicates)

researched = sum(
    row["documented_source"] != "unknown"
    for row in data
)

print("Stories with documented sources:", researched)
print("Stories needing source research:", len(data) - researched)

certainty = Counter(
    row["origin_certainty"] for row in data
)

print("\nEvidence categories:")
for category, count in certainty.items():
    print(category, ":", count)
