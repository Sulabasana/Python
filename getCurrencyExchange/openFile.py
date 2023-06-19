import tkinter as tk
import os
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Select file')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=r'C:\Users\piotr\Github\Python\Python\getCurrencyExchange',
        filetypes=filetypes)
    # showinfo(
    #     title='Selected File',
    #     message=filename.split('/')[len(filename.split('/'))-1]
    # )
    fileNext = filename.split('/')[len(filename.split('/'))-1]
    return fileNext
    # root.quit()

# quitApp = quitWind()
# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

fileName = select_file()

open_button.pack(expand=True)


# run the application
root.mainloop()