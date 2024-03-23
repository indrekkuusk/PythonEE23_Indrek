print("Hello world!")

variable1 = 15
variable2 = "String value wezassed frgte edsdrre as test test etest"
variable3 = 15.231234
variable4 = True

sum = variable1 + variable3

print(sum)

#integer(int), float, string(str), boolean(bool), None, undefined
int(variable3)
float(variable1)
print(type(variable1)) # Getting a type of a variable

len(variable2)
new_words = []
# variable2.split()
# print(len(variable2.split())

for word in variable2.split():
    new_words.append(word.strip('e')) # append list with stripped e from start and end of words
    # print(word.strip('e'))

new_text = ' '.join(new_words)    # converting list to text
print(new_text)


list_variable = [{},{},{}]
dictionary = {'key': [{"key": [{},{}]}]}

user_choice = bool(input("Choose what to do: a;sasdsa"))
print(user_choice)

# True False
if user_choice:
    print("This happens")

if user_choice:
    print("do true case things")
# elif user_choice == "potato":

else:
    print("Do whatever for not accounted cases")

iterable_text = "asasasdsass"

for letter in iterable_text:
    print(letter)

while True:

    number = int(input("asdasd"))
    if number < 5:
        break
while True:
    print("Potato")

def function_name(*args):
    sum = 0
    for arg in args:
        sum += arg

function_name(*args: 1,2,3,4,5,6,7,8,9)




