def sum_or_triple(a, b, c):
    """Return the sum of three numbers or triple the sum if all three numbers are equal."""
    if a == b == c:
        return 3 * (a + b + c)
    else:
        return a + b + c

# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = sum_or_triple(num1, num2, num3)
print("Result:", result)