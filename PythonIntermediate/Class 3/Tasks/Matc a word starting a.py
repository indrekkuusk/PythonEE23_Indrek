
# Write a regex pattern to match words starting with the letter "a" or "A" in a given string.
import re

text = "Apples are awesome and so are bananas"

# Use regular expression to match words starting with "a" or "A"
pattern = r'\b[Aa]\w+\b'
matches = re.findall(pattern, text)

# Print the matches
print(matches)

# In this code:
#
# The regular expression pattern r'\b[Aa]\w+\b' is used to match words starting with "a" or "A".
# \b represents a word boundary to ensure that the word is matched as a whole word.
# [Aa] matches either the letter "a" or "A".
# \w+ matches one or more word characters (letters, digits, or underscores).
# \b again represents a word boundary.
# re.findall() is used to find all occurrences of the pattern in the given text.
# The matched words starting with "a" or "A" are printed.




