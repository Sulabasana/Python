import os

# print the current directory
print("The current directory:", os.getcwd())

# running mkdir again with the same name raises FileExistsError, run this instead:
if not os.path.isdir("folder"):
     os.mkdir("folder")

# changing the current directory to 'folder'
os.chdir("folder")

# printing the current directory now
print("The current directory changing the directory to folder:", os.getcwd())

# go back a directory
os.chdir("..")

# make several nested directories
if not os.path.isdir("nested1/nested2/nested3"):
     os.makedirs("nested1/nested2/nested3")

# create a new text file
text_file = open("text.txt", "w")

# write to this file some text
text_file.write("This is a text file")

# rename text.txt to renamed-text.txt
os.rename("text.txt", "renamed-text.txt")