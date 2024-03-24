# Task 2:
# Write a decorator that will show how many miliseconds(or smaller units of time) it took for the function to run. (Use Task 1 code but adjust it.)

# You can create a decorator in Python to calculate the execution time of a function in milliseconds (or smaller units of time).
# Here's how you can do it:

import functools
import time


def execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Get the current time before calling the function
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Get the current time after calling the function
        execution_time_ms = (end_time - start_time) * 1000  # Calculate execution time in milliseconds
        print(f"Execution time of {func.__name__}: {execution_time_ms:.2f} milliseconds")
        return result

    return wrapper


# Example usage
@execution_time
def my_function():
    # Simulate some work
    time.sleep(0.5)


my_function()

# In this decorator execution_time, time.time() is used to get the current time in seconds before and after calling the function.
# The difference between these times is calculated to determine the execution time of the function in seconds.
# This time is then converted to milliseconds by multiplying by 1000. The execution time is printed with two decimal places for clarity.
# You can apply this decorator @execution_time to any function you want to measure the execution time for.