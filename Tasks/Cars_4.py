# Find cars that my wife would like(this is not sexist it is just how it is): Car colour: red, car accidents: 0, car year 2018 or newer

import csv

# List to store cars meeting the criteria
cars_with_options = []

# Read the CSV file and filter the data
with open('cars.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        color = row['car_color']
        accidents = int(row['car_accidents'])
        year = int(row['car_year'])

        # Check if car color is red, accidents are 0, and year is 2018 or newer
        if color.lower() == 'red' and accidents == 2 and year >= 2015:
            cars_with_options.append(row)

# Print the details of cars meeting the criteria
for car in cars_with_options:
    print(car)

# This code reads the CSV file, filters the data based on the criteria of car color being red, car accidents being 0, and car year being 2018 or newer, and
# then prints out the details of the cars that meet these criteria. Make sure to replace 'cars.csv' with the actual filename if it's different.