# Find the lucky finds, where car milage is below 150 000 and the price is less than 10 000

import csv

# List to store lucky finds
lucky_finds = []

# Read the CSV file and filter the data
with open('cars.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        mileage = int(row['car_mileage'])
        price = float(row['car_price'])

        # Check if car mileage is below 150,000 and price is less than $10,000
        if mileage < 150000 and price < 10000:
            lucky_finds.append(row)

# Print the details of lucky finds
for car in lucky_finds:
    print(car)

# This code reads the CSV file, filters the data based on the criteria of car mileage below 150,000 and price less than $10,000, and then prints out the details of
# the lucky finds. Make sure to replace 'cars.csv' with the actual filename if it's different.