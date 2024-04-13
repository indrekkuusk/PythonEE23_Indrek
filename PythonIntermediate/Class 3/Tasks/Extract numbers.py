# Task 1: Extract all numbers from the given text using regular expressions.
#
# i.e., for the "test43543lfdsfdsfl534543fdgl432fr" it will be:
# 43543
# 534543
# 432
#
# Task 1.1: Take the same text as in the exercise above and write a program using regular expressions that will remove all numbers from the text.

# # Base for Cheatsheet
# import re
#
# play_string = '''"test43543lfdsfdsfl534543fdgl432fr"
# '''
# patternDigits = re.compile(r'\d')
#
# result = re.findall(patternDigits, play_string)
# print(result)


import re

text = "test43543lfdsfdsfl534543fdgl432fr"

# Use regular expression to find all numbers
numbers = re.findall(r'\d+', text)

# Print the extracted numbers
print(numbers)

# In this code:
#
# re.findall(r'\d+', text) searches for all sequences of one or more digits (\d+) in the given text.
# re.findall() returns a list containing all the matched substrings.
# We print the list of extracted numbers.

# Use regular expression to remove all numbers
text_without_numbers = re.sub(r'\d+', '', text)

# Print the text without numbers
print(text_without_numbers)

# In this code:
#
# re.sub(r'\d+', '', text) uses a regular expression to find all sequences of one or more digits (\d+) in the given text and replaces them with an empty string ''.
# re.sub() returns the modified text with numbers removed.
# We print the modified text without numbers.



# patternText = re.compile(r'ac') # To find exact text
# patternAnyText = re.compile(r'.') # To find eny text
# patternDigits = re.compile(r'\d')  # Find all digits
# patternDigits = re.compile(r'\D')  # Find all nor digits
# patternCharacters = re.compile(r'\w') # Characters and _
# patternNotCharacters = re.compile(r'\w') # Not Characters and not _
# patternWhiteSpace = re.compile(r'\s') # White space and new line