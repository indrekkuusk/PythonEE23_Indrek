# 9. EvenOdd - Write a Python program to count the number of even and odd numbers in a series of numbers:
#
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
print(f"Even: {even}, Odd: {len(numbers) - even}")
