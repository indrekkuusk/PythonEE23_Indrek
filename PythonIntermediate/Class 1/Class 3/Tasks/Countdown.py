# Create a generator function that counts down from a specified start value 21 to 0.
def countdown(start):
    """A generator function to count down from a specified start value to 0."""
    while start >= 0:
        yield start
        start -= 1

# Example usage
start_value = 21
for value in countdown(start_value):
    print(value)

# In this code:
#
# The countdown function is a generator function that takes a start value as an argument.
# Inside the function, there's a while loop that continues as long as the start value is greater than or equal to 0.
# Within the loop, the function yields the current value of start, effectively producing it as an output of the generator.
# After yielding the value, the start value is decremented by 1.
# You can use this generator function in a for loop to iterate over the countdown values from the specified start value to 0.
# In the example usage, start_value is set to 21, and then the countdown generator is used in a for loop to print each countdown value.