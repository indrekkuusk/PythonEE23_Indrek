#1. Cats -
# Write a program that will correctly display the sentence "Alice has x cats" depending on the number of cats, it can show:
# Alice has 1 cat, Alice has 2 cats, Alice has 10 cats. use user input to get amount of cats.
# ** After number 20 entered, the output should be "Alice has a cat shelter"


cats = int(input("Please provide number of cats: "))
input("Enter :)")
if cats <= 20:
    print("Alice has", cats, "cats")
if cats >= 20:
    print("Alice has a cat shelter")




# +#input("Enter :)")
# +
# +area = lenght * width
# +print(area, "Area of Rectangle")
# \ No newline at end of file
#
# # + method
# print("Hello " + title + " " + name + ", nice to meet you!")
#
# # printf
# print("Hello %s %s, nice to meet you!" % (title, name))
#
# # str.format()
# print("Hello {} {}, nice to meet you!".format(title, name))
# print("Hello {name} {title}, nice to meet you!".format(title=title, name=name))
# print("Hello {0} {1}, nice to meet you!".format(title, name))
#
# # f-string
# print(f"Hello {title} {name}, nice to meet you!")
#
# # rounding
# number = 109.18794186161168156185
# print(f"{number:.3f}")
# print(f"{round(number, 3)}")
#
# +# text = input("Provide the text to search in: ")
# +# query = input("Provide the text to search for: ")
#
# x = int(input("Please provide number x: "))
# +y = int(input("Please provide number y: "))
# +z = int(input("Please provide number z: "))
# +
# +#input("Enter :)")
# +# total = number1 + number2
# +#
# +# print("Total of these two numbers is:", total)
# +
# +#text = input("Provide the text to search in: ")
# +#query = input("Provide the text to search for: ")
# +total = (x+y+z)*(x**2+y**2+z**2-x*y-y*z-x*z)
# +total2 = x*2 + y*2 + z*2 - 3*x*y*z
# +print(total, "Result of equation 1")
# +print(total2, "Result of equation 2")
#
# # Compare
# print(2 > 1)  # More Than
# print(2 < 1)  # Less Than
# print(2 < 2)
# print(2 <= 2)  # Less or Equal Than
# print(2 >= 2)  # More or Equal Than
# print(a == 2)  # Equal
# # Logical
# print("this" in "This text is this")
# print("this" not in "This text is this")