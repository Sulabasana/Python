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

# #Deleting Rows or Columns
# df1 = df1.drop('City',1)
# print(df1 )

# df1.drop(df1.columns[0:3],1)
# print(df1)

#adding column
len(df1.index)
# len(df7.index) is equal to 5 and belo we are adding only one item so there is an error
# df1["Continent"]="North America"
df1["Continent"]=df1.shape[0]*["North america"]
#shape in this case is (5,7) 5 rows 7 columns

#updating column
df1["Continent"]=df1["Country"] + "," + "North America"
print(df1)

df1_t = df1.T
df1_t["My Address"]=["My Citry","My Country",10,7,"My Shop", "My state", "My Continent"]

print(df1_t)

df1=df1_t.T 
print(df1)


