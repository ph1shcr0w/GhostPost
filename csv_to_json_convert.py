import csv
import json
import os

# Define safe relative directories
input_dir = os.path.join("ghostpost", "data")
output_dir = os.path.join("ghostpost", "output")

# File paths
input_csv = os.path.join(input_dir, "mangione_mail_catalog.csv")
output_json = os.path.join(output_dir, "mangione_mail_catalog_july.json")

# Ensure directories exist
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Generate a  CSV if it doesn't exist
if not os.path.isfile(input_csv):
    with open(input_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "first_initial",
                "last_initial",
                "zip_suffix",
                "postmark_date",
                "post_type",
                "notes",
                "no_postmark_signed_date",
                "no_postmark_month_only",
                "forwarded_from_huntington_sci",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "first_initial": "K",
                "last_initial": "M",
                "zip_suffix": "17",
                "postmark_date": "2025-03-04",
                "post_type": "LETTER",
                "notes": "Includes red ink sketch.",
                "no_postmark_signed_date": "*",
                "no_postmark_month_only": "March",
                "forwarded_from_huntington_sci": "TRUE",
            }
        )

# Convert CSV to JSON
try:
    with open(input_csv, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
except Exception as e:
    print(f"[!] Error reading CSV: {e}")
    exit(1)

# Write JSON
try:
    with open(output_json, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)
    print(f"[+] JSON written to: {output_json}")
except Exception as e:
    print(f"[!] Error writing JSON: {e}")
    exit(1)
