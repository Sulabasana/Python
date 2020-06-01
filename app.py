from tkinter import * 
import unidecode


window=Tk()

window.wm_title("Translator")
#Labels

l1=Label(window,text="Original Language")
l1.grid(row=2,column=0)

l2=Label(window,text="Dest language")
l2.grid(row=2,column=1)

l3=Label(window,text="Text to translate:")
l3.grid(row=4,column=0)

l4=Label(window,text="Translated text:")
l4.grid(row=4,column=1)

#Fields to provide the text
original_language=StringVar()
e1=Entry(window,textvariable=original_language, text="Original Language by default auto-detect")
e1.grid(row=3, column=0)

dest_language=StringVar()
e2=Entry(window,textvariable=dest_language)
e2.grid(row=3, column=1)

text_to_translate=StringVar()
e3=Entry(window,textvariable=text_to_translate)
e3.grid(row=5, column=0,rowspan=10)

translated_text=StringVar()
e4=Entry(window,textvariable=translated_text)
e4.grid(row=5, column=1,rowspan=10)

#Buttons
b1=Button(window,text="Open File", width=14, command="Open File")
b1.grid(row=1,column=3)

b2=Button(window,text="Translate", width=14, command="Translate")
b2.grid(row=2, column=3)

window.mainloop()