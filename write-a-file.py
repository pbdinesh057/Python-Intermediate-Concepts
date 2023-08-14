text = "Have a Nice Day!!\nSee you"

# Open 'text.txt' in write mode ('w')
# This will create the file if it doesn't exist, or overwrite it if it does
with open('text.txt', 'w') as file:
    file.write(text)  # Write the content of 'text' to the file

text = "\nI am Dinesh"

# Open 'text.txt' in append mode ('a')
# This will open the file in append mode, preserving existing content and adding new content at the end
with open('text.txt', 'a') as file:
    file.write(text)  # Append the content of 'text' to the file

#Just added to display content
path = "C:\\Users\\Admin\\PycharmProjects\\Second-Set\\text.txt"
with open(path) as file:
    print(file.read())