import re

text = "Visit us at http://example.com or https://www.example.org"

# Use regular expression to match URLs
pattern = r'\b(?:https?://)?(?:www\.)?\w+\.\w{2,}\b'
matches = re.findall(pattern, text)

# Print the matches
print(matches)

# In this code:
#
# The regular expression pattern r'\b(?:https?://)?(?:www\.)?\w+\.\w{2,}\b' is used to match URLs.
# \b represents a word boundary to ensure that the URL is matched as a whole word.
# (?:https?://)? matches the optional "http://" or "https://" protocol part of the URL.
# (?:www\.)? matches the optional "www." subdomain part of the URL.
# \w+\.\w{2,} matches the domain name and top-level domain (TLD) parts of the URL.
# \w+ matches one or more word characters (letters, digits, or underscores).
# \. matches the literal dot "." symbol.
# \w{2,} matches two or more word characters for the TLD.
# \b again represents a word boundary.
# re.findall() is used to find all occurrences of the pattern in the given text.
# The matched URLs are printed.