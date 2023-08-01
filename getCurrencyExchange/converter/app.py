#import module
import PySimpleGUI as sg
import time
import os

currency = ["EUR", "GBP", "USD", "CHF"]
clock = sg.Text('', key='clock')
label = sg.Text("Select Currency")
list1 = sg.Combo(currency, size =[45,10])
# empty_field = 
convert_button = sg.Button("Convert")
add_to_excel = sg.Button("Add to Excel")
create_chart = sg.Button("Create Chart")

window = sg.Window("Select Currency",
                   layout=[[clock],
                            [label],
                            [list1, convert_button],
                            [add_to_excel, create_chart]],
                            
                    font=("Helvetica", 20))
window.read()
window.close()
# # Import module
# from tkinter import *
# from urllib.request import urlopen
# from bs4 import BeautifulSoup as bs
# from datetime import date
# # from newExchange import *
# import requests

# # Create object
# root = Tk()

# # Adjust size
# root.geometry( "200x200" )

# # Change the label text
# def show():
#     label.config(text = clicked.get())
#     linkURL = prepareURL(clicked.get())
#     openPage(linkURL)
#     print(openPage(linkURL))
#     print(reviews)
#     # writeToFile(reviews)
#     return clicked.get()
# # def show():
# #     label.config(text = clicked.get())
# # 	# print(prepareURL(clicked.get()))
# # 	linkURL = prepareURL(clicked.get())
# #     # prepareURL(clicked.get())
# #     openPage(linkURL)
# # Dropdown menu options
# options = [
# 	"EUR",
# 	"USD",
# 	"GBP",
# 	"CHF",
# ]

# # datatype of menu text
# clicked = StringVar()

# def prepareURL(currency):
#     # currencyEnd 
#     if(currency == "USD"):
#         return("https://www.biznesradar.pl/notowania/USD-DOLAR")
#     elif(currency == "GBP"):
#         return("https://www.biznesradar.pl/notowania/GBP-FUNT-SZTERLING")
#     elif(currency == "CHF"):
#         return("https://www.biznesradar.pl/notowania/CHF-FRANK-SZWAJCARSKI")
#     elif(currency == "EUR"):
#         return("https://www.biznesradar.pl/notowania/EURO")

# def openPage(ending):
#     # print(ending)
#     def scraper():
#         response = requests.get(ending)
#         # print(response)
#         soup = bs(response.content, 'html.parser')
#         rev_span = soup.findAll("span",attrs={"class","q_ch_act"})
#         # print(rev_span)
#         for i in range(len(rev_span)):
#             if i == 1:
#                 # print(rev_span[0])
#                 rev_span = rev_span[0].text
#         return("1 " + clicked.get() + " is " + rev_span + " PLN")
#     reviews = scraper()
#     return reviews

# def writeToFile(rateCurrnency):
#     today = date.today()
#     d1 = today.strftime("%d.%m.%Y")
#     print("Today's date:", d1)
#     print("Exchange rate is: ", rateCurrency)
#     rate=rateCurrency
#     with open('currencyRate.txt','a') as f:
#         f.write(f"{d1};{rate}\n")
# # print(prepareURL(clicked))
# # initial menu text
# clicked.set( "Select Currency" )

# # Create Dropdown menu
# drop = OptionMenu( root , clicked , *options )
# drop.pack()

# # Create button, it will change label text
# button1 = Button( root , text = "Get Value" , command = show ).pack()
# button2 = Button( root , text = "Generate Chart").pack()

# # Create Label
# label = Label( root , text = " " )
# label.pack()

# # Execute tkinter
# root.mainloop()
