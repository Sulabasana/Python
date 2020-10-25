import os
os.listdir()
import pandas

df1=pandas.read_csv('supermarkets.csv')
df2=pandas.read_json('supermarkets.json')
df3=pandas.read_excel('supermarkets.xlsx',sheet_name=0)
df4=pandas.read_csv('supermarkets-commas.txt')
df5=pandas.read_csv('supermarkets-semi-colons.txt',sep=";")
df6=pandas.read_json('supermarkets.json')
df7=pandas.read_csv('supermarkets-commas.txt', header= None) #dane w  pliku nei mają headera to pierwszy rząd nie będzie wzięty jako pierwszy"
df7.columns = ["ID", "address","City", "ZIP","Country","Name","Employees"] # nadajemy header columns

# print(df7)

df8= df7.set_index('ID')
print(df8)





