import csv
import json
import os
import sys

# Define safe relative directories
base_dir = "ghostpost"
input_dir = os.path.join(base_dir, "data")
output_dir = os.path.join(base_dir, "output")

# File paths
input_csv = os.path.join(input_dir, "mangione_mail_catalog.csv")
output_json = os.path.join(output_dir, "mangione_mail_catalog_july.json")

# Ensure base directory and subdirectories exist
try:
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
except PermissionError as e:
    print(f"[!] Permission error while creating directories: {e}")
    sys.exit(3)

# Generate a CSV with headers and one row if it doesn't exist
if not os.path.isfile(input_csv):
    try:
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
                    "postmark_date": "",
                    "post_type": "",
                    "notes": "",
                    "no_postmark_signed_date": "*",
                    "no_postmark_month_only": "March",
                    "forwarded_from_huntington_sci": "TRUE",
                }
            )
        print(f"[+] CSV created: {input_csv}")
    except Exception as e:
        print(f"[!] Error creating CSV: {e}")
        sys.exit(2)

# Convert CSV to JSON
try:
    with open(input_csv, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
except Exception as e:
    print(f"[!] Error reading CSV: {e}")
    sys.exit(1)

# Write JSON
try:
    with open(output_json, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)
    print(f"[+] JSON written to: {output_json}")
except Exception as e:
    print(f"[!] Error writing JSON: {e}")
    sys.exit(1)
