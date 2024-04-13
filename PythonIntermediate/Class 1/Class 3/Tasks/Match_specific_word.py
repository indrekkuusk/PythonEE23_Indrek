import re

text = "Say hello to the world"

# Use regular expression to match the word "hello"
pattern = r'\bhello\b'
matches = re.findall(pattern, text)

# Print the matches
print(matches)

# In this code:
#
# r'\bhello\b' is the regular expression pattern.
# \b represents a word boundary, ensuring that "hello" is matched as a whole word and not as part of another word.
# hello matches the literal word "hello".
# \b again represents a word boundary.
# re.findall() is used to find all occurrences of the pattern in the given text.
# The matched word "hello" is printed.