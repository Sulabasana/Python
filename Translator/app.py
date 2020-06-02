from tkinter import *
from tkinter import filedialog, Text
import unidecode
import os


def addApp():
    #remove existing items on display list
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(('text', "*.txt"),("all files", "*.*")))
    
    print(filename)
    with open(filename, 'r', encoding="utf-8")as f:
        transl = f.read()
        print(transl)
        return(transl)

     
window=Tk()

window.wm_title("Translator")
#Labels

l1=Label(window,text="Original Language")
l1.grid(row=1,column=0)

l2=Label(window,text="Dest language")
l2.grid(row=1,column=1)

l3=Label(window,text="Text to translate:")
l3.grid(row=3,column=0)

l4=Label(window,text="Translated text:")
l4.grid(row=3,column=1)

#Fields to provide the text
original_language=StringVar()
e1=Entry(window,textvariable=original_language)
e1.grid(row=2, column=0)

dest_language=StringVar()
e2=Entry(window,textvariable=dest_language)
e2.grid(row=2, column=1)

text_to_translate=StringVar()
e3=Entry(window,textvariable=text_to_translate)
e3.grid(row=5, column=0)

translated_text=StringVar()
e4=Entry(window,textvariable=translated_text)
e4.grid(row=5, column=1)

#Buttons
b1=Button(window,text="Open From File", width=14, command=addApp)
b1.grid(row=1,column=3)

b2=Button(window,text="Translate", width=14, command="Translate")
b2.grid(row=2, column=3)

window.mainloop()