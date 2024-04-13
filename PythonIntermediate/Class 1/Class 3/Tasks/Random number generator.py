import random

def random_numbers(start, end, count):
    """A generator function to generate a sequence of random numbers within a specified range."""
    for _ in range(count):
        yield random.randint(start, end)

# Example usage
start_range = 1
end_range = 100
count = 12

for number in random_numbers(start_range, end_range, count):
    print(number)

# In this code:
#
# The random_numbers function is a generator function that takes three arguments: start (the start of the range), end (the end of the range), and count (the number of random numbers to generate).
# Inside the function, there's a for loop that iterates count times.
# Within the loop, the function yields a random integer between start and end, inclusive.
# You can use this generator function in a for loop to generate and iterate over the sequence of random numbers within the specified range.
# In the example usage, the generator function is used to generate 10 random numbers within the range 1 to 100, and each generated number is printed.