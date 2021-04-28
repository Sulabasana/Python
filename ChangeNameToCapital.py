from tkinter import *
root = Tk()

# userName = input("Please provide name \n")
# print(f'You enetered {userName}')

userName = Entry(root, width=50)
userName.pack()
userName.insert(0," Enter the name SAG ")
print(userName)


def capitalize():
    capitalized = userName.title()
    print(f"Name is \n {capitalized}")
    return capitalized

myButton = Button(root, text="Change letter to capitalized!", command=capitalize)
myButton.pack()



root.mainloop()
