import csv
import json

# Convert CSV to JSON
try:
    with open(
        r"C:\Users\reddr\OneDrive\Documents\GitHub\GhostPost\mangione_mail_catalog.csv",
        "r",
        encoding="utf-8",
    ) as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
        print(f"Loaded {len(data)} rows from the CSV.")

except FileNotFoundError:
    print("The file mangione_mail_catalog.csv was not found.")
    exit(1)
except csv.Error as e:
    print(f"An error occurred while reading the CSV file: {e}")
    exit(1)

try:
    with open(
        r"C:\Users\reddr\OneDrive\Documents\GitHub\GhostPost\mangione_mail_catalog.json",
        "w",
        encoding="utf-8",
    ) as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)
        print(f"Successfully converted {len(data)} records to JSON.")
        print("Output saved to mangione_mail_catalog.json")
except IOError:
    print("An error occurred while writing the JSON file.")
    exit(1)
