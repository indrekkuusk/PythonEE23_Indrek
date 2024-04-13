import re
# Write a regex pattern to match any digit in a given string.
text = "I have 3 apples and 5 oranges"

#patternDigits = re.compile(r'\d')  # Find all digits

# Use regular expression to match the word "hello"
pattern = r'\d'
matches = re.findall(pattern, text)

# Print the matches
print(matches)

# Write a regex pattern to match email addresses in a given text.
text = "Contact us at email@example.com or support@example.org"

pattern = r'\d'