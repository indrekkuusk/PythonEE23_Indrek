import re

def count_vowels_lines_chars(filename):
    vowel_count = 0
    line_count = 0
    char_count = 0

    with open(filename, 'r') as file:
        for line in file:
            vowel_count += len(re.findall(r'[aeiouAEIOU]', line))
            line_count += 1
            char_count += len(line)

    return vowel_count, line_count, char_count


# Provide the path of the text file
filename = 'sample_document.txt'

# Call the function to count vowels lines and characters
vowels, lines, characters = count_vowels_lines_chars(filename)

print("Vowels: {}".format(vowels))
print("Lines: {}".format(lines))
print("Characters: {}".format(characters))