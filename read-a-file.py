import os

# Define the file path
path = "C:\\Users\\Admin\\Desktop\\all.pem"

try:
    # Attempt to open the file
    with open(path) as file:
        content = file.read()  # Read the file content
        print(content)  # Print the file content
except Exception as e:
    # Handle any exceptions that may occur
    print(e)  # Print the exception message
    print("File name is not found or wrongly given")  # Custom error message
# Note: The 'file' variable is not accessible outside the 'with' block
# print(file.closed)  # Uncommenting this would raise an error
