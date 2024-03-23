# 10. Numeric - Write a Python program that accepts a string and calculates the number of digits and letters.
# Use this to help to understand if character is numeric: https://www.w3schools.com/python/ref_string_isnumeric.asp
#
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
#Digits 2

sample_string = "Python 3.2"
numbers = 0

for char in sample_string:
    if char.isnumeric():
        numbers += 1
    elif char.isalpha():
        letters += 1
print("Letters:", len(sample_string) - numbers)
print("Digits:", numbers)