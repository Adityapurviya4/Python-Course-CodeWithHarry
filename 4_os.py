# first step install os
import os

# Specify the directory path
path = "c:/Users/adity/AppData"

# Get the list of files and folders
contents = os.listdir(path)

# Print the contents
print("Contents of the directory:")
print(contents)