def read_large_file(file_path):
    """A generator function to read a large file line by line."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.rstrip('\n')

# Example usage
file_path = "large.txt"  # Replace "large_file.txt" with the path to your large file

for line in read_large_file(file_path):
    print(line)

# The read_large_file function is a generator function that takes the file path as an argument.
# Inside the function, it opens the file specified by the file path using a context manager (with open(file_path, 'r') as file:) to ensure that the file is properly closed after reading.
# It then iterates over each line in the file using a for loop and yields each line using the yield statement. The rstrip('\n') method is used to remove the newline character ('\n') from each line.
# When the generator is used in a for loop, it yields each line from the file one by one.
# You can replace "large_file.txt" with the path to your actual large file.
# In the example usage, the generator is used in a for loop to print each line from the large file. You can process each line as needed within the loop.