def function_name(*args):
    sum = 0
    for arg in args:
        sum += arg


function_name(*args: 1, 2, 3, 4, 5, 6, 7, 8, 9)

with open("test1.txt") as f:
    with open("test2.txt", "r+", encoding='') as f2:
        print(f, f2)

