# with open("file.txt") as f:
#     data = f.read()
    
# data = data.replace(" ","").replace(",","").replace(".","").replace("-","")
# number_of_characters = len(data)
# print(f"This text contains: {number_of_characters} characters")


import os
import tkinter as tk
from tkinter import filedialog, Text


with open("file.txt") as f:
    data = f.read()
    
data = data.replace(" ","").replace(",","").replace(".","").replace("-","")
number_of_characters = len(data)
print(f"This text contains: {number_of_characters} characters")





