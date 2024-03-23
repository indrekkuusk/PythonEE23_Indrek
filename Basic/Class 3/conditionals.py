#String if statement
if "this" in "This text is this":
    print ("It is in there.")

number = 3

if number > 2:
    number-=1

# elif usage example"
elif number < 2:
    number += 5

else:
    print("You are your own")


#elif condition:
    instruction
print(number)

number2 = int(input())
if number2 > 5:
    print("Do this")
elif number2 <= 5:
    print("Do another")

#multiple conditions in one if line
#if number2 >= 5 and (number2 <=1 or number2 == "Some text"):
if number2 >= 5 and not (number2 <= 1 or number2 == "Some text"):
    print("Do this1")
elif number2 <=1:
    print("Do this2")
else:
    print("Do another")

# Examples of And or
# c1  = True and True #True
# c2  = True and False #False
# c1  = False and True #True

word1 = 2==2
c1 = False or not False

user_input = int(input("What is your age"))
if user_input >= 18:
    print("Here have some fun")
else:
    print("nah brah alaealine")

print("Success case oled vanem ku 18") if user_input >= 18 else print("Fail case")

