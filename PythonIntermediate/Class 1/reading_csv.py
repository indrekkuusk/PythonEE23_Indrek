import csv

with open ('csv_source.csv', 'r') as file:
# csv_reader = csv.DictReader(file)
    data = [row for row in csv.DictReader(file)]

# print(data)

with open('csv_source.csv', 'w', newline='') as output:
    headers = data[0].keys()
    # print(headers.keys)


# with open( 'csv_source.csv','w') as output:
    writer = csv.DictWriter(output, fieldnames=headers)
    # for row in data:
    #     writer.writerow(row)
    writer.writeheader()
    writer.writerow()

print(data)