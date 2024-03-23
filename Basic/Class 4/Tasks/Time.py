#13. Time of day - Write a program to based on current time of day
# would return a word Morning, Day, Evening or Night.

# Expected Output:
# Input time in 24 hour format: 13
# Day
#The afternoon is the time between 1 to 5 pm,
# the Evening is the part between 5 to 7 pm, and Night is the time from 9 to 4 pm.
#hint: use datetime library. To get current time you will need to

from datetime import datetime
current_hour = datetime.now().hour
current_minute = datetime.now().minute
current_second = datetime.now().second
print(current_hour,":",current_minute,":",current_second)
if current_hour < 12:
        print("Morning")
if current_hour > 12 or current_hour < 17:
        print("Day")
# if current_hour == 17 or current_hour 17 < 23:
if current_hour == 17 < 19:
        print("Evening")
if current_hour == 21 < 4:
        print("Night")