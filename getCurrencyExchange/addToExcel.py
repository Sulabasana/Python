# import pandas
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


fileCur = 'EURRate.txt'
dateList = []
valueList = []
curList = []
with open(fileCur,'r') as f:
    r = f.readlines()
# print(r)

# Get First 3 character of a string in python
firstChars = fileCur[0:3]

print('First 3 character : ', firstChars)


# here ; and / are our two markers 
# in which string can be found.
# Podziel na Daty i wartości 

def dates():
    for i in r:
        subStr = i.split(';')[0]
        dateList.append(subStr)
    return(dateList)

# print(dates())
dateList = dates()
 
def values():
    for i in r:
        # print(i)
        subStr = i.split(' ')[3]
        # changeDots = subStr.replace('.', ',')
        # print(changeDots)
        # valueList.append(changeDots)
        valueList.append(subStr)
    
   
    return(valueList)
# print(values())

curValue = values()

rowCount = len(curValue)

for x in range(rowCount):
    curList.append(firstChars)
# print(len(curList))

df = pd.DataFrame({'Name': curList,'Date': dateList,'Value': curValue})

# # create a Pandas Excel writer object using XlsxWriter as the engine
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

# # write data to the excel sheet
df.to_excel(writer, sheet_name=firstChars, index=False)

# get workbook
workbook = writer.book

# get sheet for conditional formatting
worksheet = writer.sheets[firstChars]

# create chart object
chart = workbook.add_chart({'type': 'line'})

# configure the series of the chart from the dataframe data
#przerobić trzeba  kropke na przecinek
chart.add_series({'values': '=EUR!$C$2:$C$50'})

# insert chart into the worksheet
worksheet.insert_chart('E2', chart)

# # close file
writer.close()
