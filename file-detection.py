import os

path = "C:\\Users\\Admin\\Desktop\\Jenkins-Shared-Library"

if os.path.exists(path):
    print("Location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("File does not exist")