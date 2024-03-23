def greet(name):
    print(f"Welcome to potato eating registry{name}!")

def get_action():
    print()
    print("Options are")
    print("1 - Add new entry")
    print("2 - Display all entries")
    print("3 - Exit the program")
    user_input = input("Choose your action: ")
    return user_input

def get_entry_details():
    print()
    name = input("Plaese state you name:")
    age = input("Please state your age:")
    city = input("Here are you from:")
    amount_of_potatos = input("How many potatos did you down yesterday?: ")
    print(f"Thanks{name} you record of {amount_of_potatos} potatos eaten is now recorded!")
    return f"The participant name {name}, aged {age} years old, coming from {city} have destroyed {amount_of_potatos}"


def show_entries(entries):
    print()
    for entry in entries:
        print(entry)
# def show_entries(entries):
#     print()
#     #for entry in entries
#       #  print(entry)

# Mis see on? Comparing name to text
if __name__ == "__main__":
    greet("Some Random Text")
    show_entries(['text', 'text2'])
