import os

# Select the directory whose content you want to list 
directory_path = 'D:/'

# Use the os module to list the directory content 
contents = os.listdir("D:")

# Print the contents of the directory 
print(contents)
print(type(contents))
