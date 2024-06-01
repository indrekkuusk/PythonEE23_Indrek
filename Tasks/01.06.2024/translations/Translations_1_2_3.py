#1. Extracting TBT Values from Files

import os
import json
import re

def extract_tbt_values_from_json(directory):
    tbt_data = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        continue  # Skip files that are not valid JSON

                    # Process the JSON data to extract TBT values
                    tbt_entries = process_json(data)
                    if tbt_entries:
                        tbt_data[file] = tbt_entries

    return tbt_data

def process_json(data, prefix=''):
    tbt_entries = {}

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str) and 'TBT:' in value:
                # Extract the value after 'TBT:'
                tbt_value = re.search(r'TBT:\s*(.*)', value).group(1).strip()
                tbt_entries[prefix + key] = tbt_value
            elif isinstance(value, dict):
                nested_entries = process_json(value, prefix + key + '.')
                if nested_entries:
                    tbt_entries.update(nested_entries)
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    nested_entries = process_json(item, prefix + key + f'[{i}].')
                    if nested_entries:
                        tbt_entries.update(nested_entries)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            nested_entries = process_json(item, prefix + f'[{i}].')
            if nested_entries:
                tbt_entries.update(nested_entries)

    return tbt_entries

def write_tbt_values_to_file(tbt_data, result_file):
    with open(result_file, 'w', encoding='utf-8') as f:
        json.dump(tbt_data, f, indent=4)

# Usage
directory = 'C:/Users/Indrek/PycharmProjects/PythonEE23_Indrek/Tasks/01.06.2024/translations/'
result_file = 'c:/temp/TBT_file.txt'



tbt_data = extract_tbt_values_from_json(directory)
write_tbt_values_to_file(tbt_data, result_file)
