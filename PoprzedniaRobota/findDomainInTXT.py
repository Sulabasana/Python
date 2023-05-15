import tkinter as tk   # from tkinter import Tk 
from tkinter.filedialog import askopenfilename
import time

#prepare for
timestr = time.strftime("%d%m%Y_%H%M%S") 
filename = askopenfilename()

def FindMahle():
    string1 = '@mahle.com'
    string2 = "Email accepted"
    string3 = "INBOUND"
    # opening a text file
    with open(filename, 'r') as file1:
                
        # index = 0
        
        # Loop through the file line by line
        for line in file1:
            # index += 1 
            completeDate = ""
            completeName = ""
            #remove line with email accepted
            if string2 in line:
                continue
            # checking string is present in line or not
            elif string1 in line:
                completeName += line
                completeName += ";"
                print(completeName)
                openFile(completeName)
            # checking date
            elif string3 in line:
                #remove INBOUND and space from begining 
                removeExtra = line.split(string3)[1]
                removeExtra = removeExtra.strip()
                #add each line to string
                # completeDate += removeExtra
                # print(completeDate) 
                # openFile(completeDate)  

fileOutput = "Result_" + timestr + '.txt'

def openFile(yourData):
    with open(fileOutput, 'a') as file2:
            file2.write(yourData)
            

FindMahle()