import csv
import json

# def csv_to_json(csv_file, json_file):
#     # Read data from the CSV file
#     with open(csv_file, 'r') as file:
#         csv_data = csv.DictReader(file)
#         # Convert CSV data to a list of dictionaries
#         data = [row for row in csv_data]
#
#     # Write data to the JSON file
#     with open(json_file, 'w') as file:
#         json.dump(data, file, indent=4)
#
# # Convert the CSV file to JSON
# csv_to_json('album.csv', 'album.json')

# with open("album.json", "r+") as f:
#     print(f)

f = open('album.json', 'r')
#To get everything in the file, just use read()

file_contents = f.read()
#And to print the contents, just do:

print (file_contents)
#"Don't forget to close the file when you're done.

#f.close()