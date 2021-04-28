from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue", fg="white")
e.pack()
e.insert(0," Enter your Name: ")



# def myClick():
#     myLabel = Label(root, text="Look! I clicked a Button!!")
#     myLabel.pack()
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()


root.mainloop()