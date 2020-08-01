# with open("file.txt") as f:
#     data = f.read()
    
# data = data.replace(" ","").replace(",","").replace(".","").replace("-","")
# number_of_characters = len(data)
# print(f"This text contains: {number_of_characters} characters")


import os
import tkinter as tk
from tkinter import filedialog, Text

root= tk.Tk() # Body, whole app will be attached here
apps = []
root.wm_title("Open Apps")

def addApp():
    #remove existing items on dispaly list
    for widget in frame.winfo_children(): 
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(('textfiles', "*.txt"),("all files", "*.*")))
    
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)
        

canvas = tk.Canvas(root, height=700,width=700, bg="#263400")
canvas.pack() #attach canvas to root

frame = tk.Frame(root, bg="white") #another container
frame.place(relwidth=0.8, relheight=0.8, relx= 0.1, rely=0.1) #size and relx/y to center

openfile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263400", command=addApp)

openfile.pack() #add to root

runapps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263400", command=runApps)

runapps.pack()

for app in apps:
    label = tk.Label (frame, text=app)
    label.pack()
    

with open(app) as f:
        data = f.read()    
    data = data.replace(" ","").replace(",","").replace(".","").replace("-","")
    number_of_characters = len(data)
    print(f"This text contains: {number_of_characters} characters")



root.mainloop();





