import os
import shutil
try:
    os.remove('test.txt')

except Exception as e:
    print("File not Found\n")
    print(e)
###########################################
# os.remove(path) deletes a file
# os.rmdir(path) deletes the empty directory
# shutil.rmtree(path) deletes files inside a folder recurssively
###########################################

file_to_delete = 'file_to_delete.txt'

try:
    # Delete the specified file
    os.remove(file_to_delete)
    print("File '{file_to_delete}' has been deleted.")
except FileNotFoundError:
    print("File '{file_to_delete}' not found.")
except Exception as e:
    print("An error occurred: {e}")

###################################
# If you want to delete directories, you should use the shutil.rmtree() function from the shutil module.

import shutil

directory_to_delete = 'directory_to_delete'

try:
    # Delete the specified directory and its contents
    shutil.rmtree(directory_to_delete)
    print("Directory '{directory_to_delete}' has been deleted.")
except FileNotFoundError:
    print("Directory '{directory_to_delete}' not found.")
except Exception as e:
    print("An error occurred: {e}")
