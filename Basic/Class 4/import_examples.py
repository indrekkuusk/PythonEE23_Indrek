#register users -


import main_functions as fns

entries = []
host_name = input("What is your name?")
fns.greet(host_name)

while True:
    user_action = fns.get_action()
    if user_action == '1':
        entries.append(fns.get_entry_details())
    elif user_action == '2':
        fns.show_entries(entries)
    elif user_action == '3':
        print("Thank You for using our services! Bye! .-)")
        break


# #Option 3 is cool sometimes
# from main_functions import get_action, greet
# get_action()
#
# # Option 4 is cool sometimes
# from main_functions import *
# get_action()
# greet()
# get_entry_details()