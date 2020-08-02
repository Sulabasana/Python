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
os.makedirs("nested1/nested2/nested3")