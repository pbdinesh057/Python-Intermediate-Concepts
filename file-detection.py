import os

# Define the path to check
path = "C:\\Users\\Admin\\Desktop\\Jenkins-Shared-Library"

# Check if the path exists
if os.path.exists(path):
    print("Location exists")  # Path exists
    # Check if the path is a file or directory
    if os.path.isfile(path):
        print("That is a file")  # It's a file
    elif os.path.isdir(path):
        print("That is a directory")  # It's a directory
else:
    print("File does not exist")  # Path doesn't exist
