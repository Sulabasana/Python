import pandas
import os
# print(os.listdir())

df1 = pandas.read_json("supermarkets.json")
df1 = df1.set_index("Address")
# print(df1)
# df1 = df1.loc["735 Dolores St":"332 Hill St","Country":"Id"]
# print(df1)

# df1 = df1.loc[:,"Country"]
# print(df1)

# df1 = df1.iloc[1:4,1:4] #From Dolores to 3995(4 is not included) and from country to Id
# print(df1)
#df1.ix[3,4]

#Deleting Rows or Columns
# df1 = df1.drop('City',1)
# print(df1 )

df1.drop(df1.columns[0:3],1)
print(df1)

#updating colmn

