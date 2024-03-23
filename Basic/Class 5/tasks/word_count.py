import json

text = "Fruitcake icing donut jelly beans gummies. Croissant liquorice croissant chocolate lollipop jelly-o carrot cake. Marshmallow jujubes cheesecake caramels cake jujubes dragée.Pudding muffin sugar plum toffee cookie cotton candy cupcake cupcake jelly beans. Cake lemon drops danish chocolate cake gingerbread chocolate cake. Marzipan wafer pudding jelly-o sweet roll marzipan. Bear claw caramels cake gummi bears cotton candy muffin brownie tart apple pie."

words_counter = {}

words_list = text.split()

for word in words_list:
    if words_counter.get(word.strip(".")):
        words_counter[word.strip(".")] += 1
        print("In")
    else:
        words_counter[word.strip(".")] = 1
        print("Not in")
print(json.dumps(words_counter, indent=7))

        