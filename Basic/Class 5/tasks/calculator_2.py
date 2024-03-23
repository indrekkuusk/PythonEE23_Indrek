#Calculator 2.0 - Create a calculator that would ask user for first number, action, second number, than do the action,
# display the result, ask user if he would like to do more actions: if yes, start the program again. if no,
# terminate the program. (Calculator should handle at least +-/*)
print("Hello, Welcome to  Calculator 2.0")

while True:
    number_one = float(input("Please provide first number:"))
    number_two = float(input("Please provide second number:"))
    action = input("Select the action to do: \n"
                       "a - Add \n"
                       "s - Subtract \n"
                       "d - Divide \n"
                       "m - Multiply \n"
                       ":")
    if action == 'a':
        print(f"The Sum of these numbers is", number_one + number_two)
    elif action == 's':
        print(f"The Sum of these numbers is", number_one - number_two)

    elif action == 'd':
        print(f"The division of these numbers is", number_one / number_two)

    elif action == 'm':
        print(f"Multiplication of these numbers is", number_one * number_two)

    is_again = input("Would You like to do one more? Y or N:")
    if is_again == "Y":
            continue
    break