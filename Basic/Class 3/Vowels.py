#3. Vowels - Write a program that will determine the number of vowels in a given string.
# vowels = ['a', 'e', 'i', 'o', 'u'] Using text generators like this: https://cupcakeipsum.com/
# Get a text and just assign it to a string variable in the program.

text = "Ice cream danish brownie wafer marzipan liquorice. Apple pie cupcake chocolate cake fruitcake biscuit cookie lollipop. Carrot cake candy chocolate bar biscuit biscuit oat cake icing gingerbread pastry. Fruitcake halvah donut soufflé cotton candy candy canes cheesecake danish danish."
#vowels =[aeiouAEIOU]
#vowel_count = len((r'[aeiouAEIOU]', text))
#    if char in text['a', 'e', 'i', 'o', 'u']
#     text.count['a', 'e', 'i', 'o', 'u'],
# vowel_count = len(text.find(r'[aeiouAEIOU]', text))

print(f"Index of letter 'a'  in the text is {text.index('a')}")
print(f"Index of letter 'e'  in the text is {text.index('e')}")
print(f"Index of letter 'i'  in the text is {text.index('i')}")
print(f"Index of letter 'o'  in the text is {text.index('o')}")
print(f"Index of letter 'u'  in the text is {text.index('u')}")

vowel_count =  {text.index('a')} + {text.index('e')}
#+{text.index('e')}+{text.index('i')}+{text.index('o')}+{text.index('u')})
print(vowel_count)
#Get number of Vowels from text  [aeiouAEIOU]
#now the checking of char in "text" works just as well when checking if char in ['a', 'e', 'i', 'o', 'u']

# What is the amount of certain letters in this text
#print(f"Amount of 'Vowels' in the text is {vowel_count}")


# # Length of the string
# length = len(example_text)
# print(length)
#
# # What is the index of this character(first one)
# print(f"Index of letter 'y'  in the text is {example_text.index('y')}")
#
# # What is the amount of certain letters in this text
# print(f"Amount of 'B' in the text is {example_text.count('B')}")
