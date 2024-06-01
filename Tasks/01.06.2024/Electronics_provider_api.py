import json
import csv

def clean_data(data):
    cleaned_data = []

    for item in data:
        # Remove items with extra_field as null
        if item.get("extra_field") is None:
            continue

        # Convert price to float if it's a string
        if isinstance(item.get("price"), str):
            item["price"] = float(item["price"])

        # Remove items with stock or warranty as null
        if item.get("stock") is None or item.get("warranty") is None:
            continue

        cleaned_data.append(item)

    return cleaned_data

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    cleaned_data = clean_data(data["data"])

    # Extract keys for CSV header
    if cleaned_data:
        keys = cleaned_data[0].keys()

        with open(csv_file, 'w', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(cleaned_data)

if __name__ == "__main__":
    json_file = 'c:/temp/electronics_products.json'
    csv_file = 'c:/temp/cleaned_electronics_products.csv'
    json_to_csv(json_file, csv_file)
    print(f"Data cleaned and saved to {csv_file}")
