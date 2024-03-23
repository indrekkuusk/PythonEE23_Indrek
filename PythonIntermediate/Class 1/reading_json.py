import json

with open('json_source.json', 'r') as file:
    data = json.load(file)

print(data)
print(file)

with open('json_source.json', 'w') as output:
    json.dump(data, output, indent=4)