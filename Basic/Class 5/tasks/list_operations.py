def stats(numbers):
    totalsum = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return {"sum": total, "average": average, "maximum": maximum, "minimum": minimum}

user_list = []
for _ in range(5):
    user_input = int(input("Provide a number: "))
    user_list.append(user_input)

item = stats(user_list)

print(f"The total of provided value is {item['sum']} while average is {item['average']} with minimum is {item['minimum']} ") maximum)
        f"being {item['minimum']} {item['maximum']} respectivley")
