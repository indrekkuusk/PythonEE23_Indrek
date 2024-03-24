# Task 1:
# Write a decorator that will show the hour, minute and second before calling the code of the decorated function and
# after calling the code of the decorated function.

# You can create a decorator in Python to show the current hour, minute, and second before and after calling the code of the decorated function.
# Here's how you can do it:

import functools
import datetime


def show_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Show current time before calling the function
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Time before calling {func.__name__}: {current_time}")

        # Call the function
        result = func(*args, **kwargs)

        # Show current time after calling the function
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Time after calling {func.__name__}: {current_time}")

        return result

    return wrapper


# Example usage
@show_time
def my_function():
    print("Executing my function...")


my_function()

# This decorator show_time wraps around the decorated function. Before calling the decorated function, it prints the current time.
# After calling the decorated function, it prints the current time again. The functools.wraps(func) decorator is used to preserve the metadata of the original
# function.
# You can apply this decorator @show_time to any function you want to track the time before and after its execution.