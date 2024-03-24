# Lambdas:
# Task 1:
# Write a program that uses the filter function to print words which are palindromes in the word list passed.
# A palindrome is an expression that sounds the same when read from both the left and the right side. For example, such words are palindromes: radar, level, rotor.
# my_list = ["rotor", "level", "radar", "mama"] (edited)

# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). For example, "racecar" and "madam" are palindromes.
# To check if a string is a palindrome, you can compare the original string with its reverse. If they are the same, then the string is a palindrome. Here's a Python function to check if a given string is a palindrome:

# You can use the filter() function along with a lambda function to filter out the palindromes from the given word list. Here's how you can do it:

def is_palindrome(word):
    return word == word[::-1]

my_list = ["rotor", "level", "radar", "mama"]

palindromes = filter(is_palindrome, my_list)

print("Palindromes:")
for palindrome in palindromes:
    print(palindrome)

# This code defines a function is_palindrome(word) that returns True if the given word is a palindrome and False otherwise.
# Then, it uses the filter() function to filter the words from the my_list that are palindromes. Finally, it prints the palindromes found.