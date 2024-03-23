# Create a user class
# initialize the fields of the user: id, name, age, city, potato
# create two methods:
#    register_user( id, name, age, city, potato):
#        responsible for returning formed user data.
#        collecting the data from userInput and storing it in the users list is not included to this method
# :
# print(f"The participant {self.name}, aged {self.age} years old, coming from {self.city} have "
#              f"destroyed {self.potato} potatoes yesterday.")
# Adjust the code so it would still work after these adjustments.

class Entry:

    def __init__(self,id, name='', age='', city='', potato=''):
        self.id = id
        self.name = name
        self.age = age
        self.city = city
        self.potato_count = potato_count

    def form_entry(self):
        return f"{self.id}, {self.name}, {self.age}, {self.city}, {self.potato_count}\n"

    def  get_user_data(self):
        print("Please provide following information")
        self.name = input("Please provide you name")
        self.age = input("Please provide your age")
        self.city = input("Please provide your city")
        self.potato_count = input("Potato count")

    def announcement(self):
        print(f"The participant {self.name}, aged {self.age}, years old, coming from {self.city}, has" f"destroyed {self.potato_count} potatoes yesterday")

print("Hello to the great annual Popato eating competition")

id_counter = 0
entries = []

while True:
    user_action = input("a - Add an entry\n"
                        "v - View the entries\n"
                        "x - Exit and Save\n")

    if user_action.lower() == "a":
        entry = Entry(id_counter)
        entry.get_user_data()
        entries.append(entry)
        id_counter += 1

    elif user_action.lower() == "v":
        for entry in entries:
            print(entry.announcement())


    elif user_action.lower() == "x":
        break
with open("entries.txt", "a")    as f:
    f.write("id,name,age,city,potato_count\n")
    for entry in entries:
        f.write(entry.form_entry())
