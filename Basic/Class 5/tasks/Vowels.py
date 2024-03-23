vowels = ['a', 'e', 'E', 'i', 'o', 'u']
text = "Macaroon macaroon tOotsie roll jElly-o cotton candy candy brownie pie jelly beans"
amount_of_vowels = 0

for char in text:
    if char.upper() in vowels:
        amount_of_vowels += 1

print(f"Number of vowels in text: {amount_of_vowels}")
