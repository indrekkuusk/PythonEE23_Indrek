import json

# Read the data from the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Calculate the average of the numbers on the right side
right_side_avg = sum(data['right_side']) / len(data['right_side'])

# Calculate the average of the numbers on the left side
left_side_avg = sum(data['left_side']) / len(data['left_side'])

# Calculate the average of both side averages
both_sides_avg = (right_side_avg + left_side_avg) / 2

# Print the results
print("rightside:", right_side_avg)
print("leftside:", left_side_avg)
print("bothsides:", both_sides_avg)