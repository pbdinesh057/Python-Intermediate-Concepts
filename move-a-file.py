import os

source = "test.txt"
destination = "folder\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print("File has been moved")
except Exception as e:
    print(e)

