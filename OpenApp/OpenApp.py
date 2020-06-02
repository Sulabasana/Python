import tkinter as tk
from tkinter import filedialog, Text #filedialog to Files
import os #allows to run apps

root= tk.Tk() # Body, whole app will be attached here
apps = []
root.wm_title("Open Apps")

if os.path.isfile('save.txt'):
    with open('save.txt' , 'r' ) as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()] #removes empty spaces


def addApp():
    #remove existing items on dispaly list
    for widget in frame.winfo_children(): 
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(('executables', "*.exe"),("all files", "*.*")))
    
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

root.mainloop();

#generate file when we are closing app
with open ('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
