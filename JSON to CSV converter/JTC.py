import json
import csv
import os

INPUT_FILE = "data.json"
OUTPUT_FILE = "converted_data.csv"

def load_json_data(filename):
    if not os.path.exists(filename):
        print("JSON file not found")
        return []
    
    with open(filename, 'r', encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            print("Invalid JSON format")


def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert")
        return
    
    field_name = list(data[0].keys())

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=field_name)
        writer.writeheader()
        for record in data:
            writer.writerow(record)

    print(f"Converted {len(data)} records to {output_file}")


def main():
    print("Converting JSON to CSV...")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

main()