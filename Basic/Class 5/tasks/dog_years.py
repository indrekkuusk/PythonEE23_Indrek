#11. Dog Years - Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years.
# After that, each dog year equals 4 human years.

human_years = int(input("How many human years should we convert:"))

dog_years = 0

for year in range(1, human_years):
    if year < 3:
        dog_years += 10.5
    else:
        dog_years += 4
print(dog_years)