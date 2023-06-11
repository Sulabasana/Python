# import pandas
import pandas as pd
fileCur = 'EURRate.txt'
with open(fileCur,'r') as f:
    r = f.readlines()
# print(r)

# Get First 3 character of a string in python
first_chars = fileCur[0:3]

print('First 3 character : ', first_chars)


# here ; and / are our two markers 
# in which string can be found.
# Podziel na Daty i wartości 
 
def dates():
    for i in r:
        subStr = i.split(';')[0]
        newList += subStr
    return(newList)

print(dates())
# df = pd.DataFrame({"Name": [first_chars],"Date": [data z for lupa wyżej] "Value":[r]})


# # dataframe with Name and Age columns
# df = pd.DataFrame({'Name': ['A', 'B', 'C', 'D'], 'Age': [10, 0, 30, 50]})

# # create a Pandas Excel writer object using XlsxWriter as the engine
# writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

# # write data to the excel sheet
# df.to_excel(writer, sheet_name='Sheet1', index=False)

# # close file
# writer.close()
