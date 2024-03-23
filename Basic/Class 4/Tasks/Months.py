# 12. Days - Write a Python program to convert a month name to a number of days.
#
# Expected Output:
# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December
#
# Input the name of Month: February
# No. of days: 28/29 days

import json

months_dict = {
     "name": "January, February, March, April, May, June, July, August, September, October, November, December",
     "days": "31, 28/29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31",

    # "city": "Vilnius",
    #months": ["January, February, March, April, May, June, July, August, September, October, November, December"],

}


January = 31
February = 29
March = 31
May = 31
June = 30
July = 31
August = 31
September = 30
October = 31
November = 30
December = 31

# print("This is an amazing calculator that can only add for now ")
# number1 = int(input("Please provide number 1: "))
#
# total = number1 + number2

#months_dict['name'].append('days')
print(months_dict.get('name'))
print(months_dict.get('days'))
