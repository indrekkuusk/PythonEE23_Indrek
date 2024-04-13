# Base for Cheatsheet
import re

play_string = '''abcdefghijklmnopqurtuvwxyz
abcDefghijklmNopqurtuvwxyZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ]  | ( )
lietuva.com
ac
+370
}37060482010
+370.604.82.010
+370-604-82-010
+aaa-604-82-010
+ddd-604-82-010
-37060482010
111.999.6699
eima.blaz@gmail.com_'''


patternText = re.compile(r'ac') # To find exact text
patternAnyText = re.compile(r'.') # To find eny text
patternDigits = re.compile(r'\d')  # Find all digits
patternDigits = re.compile(r'\D')  # Find all nor digits
patternCharacters = re.compile(r'\w') # Characters and _
patternNotCharacters = re.compile(r'\w') # Not Characters and not _
patternWhiteSpace = re.compile(r'\s') # White space and new line

patternWordBoundry = re.compile(r'\bHa') # Occurences of Ha even if it is star of another work
patternNotWordBoundry = re.compile(r'\BHa') # Individual occurences of Ha
patternStartString = re.compile(r'^abc') # Starts with a string
patternEndWithString = re.compile(r' .com_') # Ends with a string

patterListOfOptions = re.compile(r'[+-]37060482010') # List of options
patterNotListOfOptions = re.compile(r'[^+-]37060482010') # List of options
patternGrouping = re.compile(r'\+(\d\d\d).(\d\d\d).(\d\d.\d\d)') # Grouping
patternGroupingWithOr = re.compile(r'\+(\d\d\d)|\w\w\w.(\d\d\d).(\d\d.\d\d)') # Grouping

patternZeroOrMore = re.compile(r'\+370*') #
patternOneOrMore = re.compile(r'\+370+') #
patternOptionCharacter = re.compile(r'ab?c') # Optional character
patternExactNumber = re.compile(r'\+(\d{3}).(\d{3}).(\d{2,4})')

# result = re.findall(patternExactNumber, play_string)
# print(result)
resutSearch = patternText.search(play_string)
print(resutSearch.group(0))

# Match the start of the text
resultMatch = patternText.match(play_string)
print(resutSearch)

# Find all occurances
resultFindAll = patternText.findall(play_string)