import re

text = "Contact us at email@example.com or support@example.org"

# Use regular expression to match email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
matches = re.findall(pattern, text)

# Print the matches
print(matches)

# In this code:
#
# The regular expression pattern r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' is used to match email addresses.
# \b represents a word boundary to ensure that the email address is matched as a whole word.
# [A-Za-z0-9._%+-]+ matches one or more characters that are letters, digits, dots, underscores, percentage signs, plus signs, or hyphens.
# @ matches the literal "@" symbol.
# [A-Za-z0-9.-]+ matches one or more characters that are letters, digits, dots, or hyphens.
# \. matches the literal dot "." symbol.
# [A-Z|a-z]{2,} matches two or more characters that are letters (upper or lower case) to represent the top-level domain (TLD).
# re.findall() is used to find all occurrences of the pattern in the given text.
# The matched email addresses are printed.