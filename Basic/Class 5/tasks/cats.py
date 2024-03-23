#1. Cats -
# Write a program that will correctly display the sentence "Alice has x cats" depending on the number of cats, it can show:
# Alice has 1 cat, Alice has 2 cats, Alice has 10 cats. use user input to get amount of cats.
# ** After number 20 entered, the output should be "Alice has a cat shelter"


# cats = int(input("Please provide number of cats: "))
# input("Enter :)")
# if cats <= 20:
#     print("Alice has", cats, "cats")
# if cats >= 20:
#     print("Alice has a cat shelter")

amount_of_cats = int(input("How many cats?:"))

if amount_of_cats == 1:
    print(f"Alice has {amount_of_cats} cat")
elif    1 < amount_of_cats < 20:
    print(f"Alice has {amount_of_cats} cat")
elif     amount_of_cats >=20:
    print("Alice has a cat shelter")
else:
    print(f"Someone stole {amount_of_cats * -1} cats")

