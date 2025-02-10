import json
import csv
from datetime import datetime

# Load JSON file
json_file_path = "stock_data.json"
date_str = datetime.now().strftime("%Y-%m-%d")
csv_file_path = f"stock_data_{date_str}.csv"

with open(json_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract keys from the first record to use as CSV headers
all_keys = set()
for record in data.values():
    all_keys.update(record.keys())
all_keys = sorted(all_keys)  # Sort keys for consistency

# Write CSV file
with open(csv_file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["ticker"] + all_keys)
    writer.writeheader()
    
    for key, record in data.items():
        row = {"ticker": key, **record}
        writer.writerow(row)

print(f"CSV file saved at {csv_file_path}")