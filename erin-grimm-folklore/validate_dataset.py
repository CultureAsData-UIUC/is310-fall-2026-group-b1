
import csv
from collections import Counter

# Open the Grimm folklore dataset
with open("grimm_folklore_dataset.csv",
          encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Count total stories
print("Total stories:", len(data))

# Check for duplicate KHM numbers
khm_numbers = [row["khm_number"] for row in data]
duplicates = len(khm_numbers) - len(set(khm_numbers))

print("Duplicate KHM numbers:", duplicates)

# Count researched historical sources
researched = sum(
    row["documented_source"] != "unknown"
    for row in data
)

print("Stories with documented sources:", researched)
print("Stories needing source research:", len(data) - researched)

# Examine evidence categories
certainty = Counter(
    row["source_evidence_status"] for row in data
)

print("\nEvidence categories:")
for category, count in certainty.items():
    print(category, ":", count)
