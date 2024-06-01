# Find all the cars that are purchased since 2015/01/01 and had no car accidents

import csv
from datetime import datetime

# Define the start date for filtering
start_date = datetime(2015, 1, 1)

# List to store cars that meet the criteria
cars_meeting_criteria = []

# Read the CSV file and filter the data
with open('cars.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert purchase date string to datetime object
        purchase_date = datetime.strptime(row['car_purchase_date'], '%m/%d/%Y')

        # Check if purchased since 2015/01/01 and had no accidents
        if purchase_date >= start_date and int(row['car_accidents']) == 0:
            cars_meeting_criteria.append(row)

# Print the details of cars meeting the criteria
for car in cars_meeting_criteria:
    print(car)

# This code reads the CSV file, converts the purchase date string to a datetime object, and then filters the data based on the criteria of being purchased
# since 2015/01/01 and having zero car accidents. Finally, it prints out the details of the cars that meet these criteria.
# Make sure to replace 'cars.csv' with the actual filename if it's different.