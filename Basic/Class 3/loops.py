# multiples ways to do this
# Basicly
#    instruction

# do:
# instructions
# while conditions

# for conditions:
#     instructions:

#while conditions
number = 0
while number <= 10:
        print(number)
        number += 1.5
while True:
    user_input = input("a - fora addition, s - far substratction, x to Quit")
    if user_input == 'a':
        print(f"2+2+={2 + 2}")
    elif user_input == 's':
        print(f"2-2={2 -2 }")
    elif user_input == 'x':
        print("Thank you for using our services")
        break
        # continue
    else:
        print("Text was wrong, try one possible options")
# for conditions
cars = ["VW", "Audi", "BMW"]
for car in cars:
    print(car)

for index, car in enumerate(cars):
    print(index, car)

some_text = "This is very cool text!"
["This", "is", "very",  "cool", "text!,"]
new_text =""

for char in some_text:
    if char =="o":
        new_text += char.upper()
    elif char in "xlT":
        new_text += "@"
    else:
        new_text += char
print(new_text)

for word in some_text.split( "i"):
    print(word.strip("!"))

variable = range(50, 101, 20)
print(list(variable))


for  number in range(2):
    print(cars[number])

# list comprehensive
numbers = []
for i in range(100):
    numbers.append(i)

numbers = [i for i in range(1000)]
print(numbers)



# print(number)
# print(1)
# print(2)
# print(3)
# print(4)