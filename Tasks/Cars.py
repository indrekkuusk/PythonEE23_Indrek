# Read the file, Create 4 buckets of data of the given information.
#
#     For each Make+Model find the latest year and to this bucket only collect All latest cars for each make+model that is present in the file.


import csv

# Define a dictionary to store the latest year for each make and model combination
latest_year_by_make_model = {}

# Read the CSV file and populate the dictionary
with open('cars.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        make_model = (row['car_make'], row['car_model'])
        year = int(row['car_year'])

        # Update the latest year for each make and model combination
        if make_model not in latest_year_by_make_model or year > latest_year_by_make_model[make_model]:
            latest_year_by_make_model[make_model] = year

# Now, let's collect all the cars with the latest year for each make and model
latest_cars = []
with open('cars.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        make_model = (row['car_make'], row['car_model'])
        year = int(row['car_year'])

        # If the car has the latest year for its make and model, add it to the list
        if year == latest_year_by_make_model[make_model]:
            latest_cars.append(row)

# Print the latest cars for each make and model
for car in latest_cars:
    print(car)


# This code reads the CSV file, identifies the latest year for each make and model combination, and then collects all the cars with the latest year for each make
# and model. Finally, it prints out the details of these latest cars. Make sure to replace 'cars.csv' with the actual filename if it's different.
