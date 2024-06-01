#1. Extracting TBT Values from Files
i
iimport os
import re


def extract_tbt_values(directory):
    tbt_values = []
    tbt_pattern = re.compile(r'TBT:\s*(.*)')

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):  # Assuming the files are json files
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    for line in f:
                        match = tbt_pattern.search(line)
                        if match:
                            tbt_values.append(match.group(1).strip())

    return tbt_values




def write_tbt_values(tbt_values, result_file):
    with open(result_file, 'w', encoding='utf-8') as f:
        for value in tbt_values:
            f.write(value + '\n')


# Usage
directory = 'C:/Users/Indrek/PycharmProjects/PythonEE23_Indrek/Tasks/01.06.2024/translations/'
result_file = 'c:/temp/TBT_file.txt'
tbt_values = extract_tbt_values(directory)
write_tbt_values(tbt_values, result_file)
