def infinite_sequence(start, step):
    """A generator function to generate an infinite sequence of numbers."""
    current = start
    while True:
        yield current
        current += step

# Example usage
start_value = 42
step_value = 5

# Create a generator instance
sequence_generator = infinite_sequence(start_value, step_value)

# Generate and print the first 10 numbers from the sequence
for _ in range(10):
    print(next(sequence_generator))

# In this code:
#
# The infinite_sequence function is a generator function that takes two arguments: start (the start value of the sequence) and step (the increment value for each step).
# Inside the function, there's a while loop that continues indefinitely (while True).
# Within the loop, the function yields the current value of current, effectively producing it as an output of the generator.
# After yielding the value, the current value is incremented by step.
# You can create an instance of the generator by calling infinite_sequence(start, step).
# You can use the next() function to generate the next number in the sequence each time it's called.
# In the example usage, the generator is used to generate and print the first 10 numbers from the sequence. Since it's an infinite sequence, you can continue generating numbers as needed.




