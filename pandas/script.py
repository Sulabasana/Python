#ipython
In [1]: import pandas

In [2]: df1=pandas.DataFrame([2,4,6],[10,20,30])

In [3]: df1
Out[3]:
    0
10  2
20  4
30  6

In [4]: df1=pandas.DataFrame([[2,4,6],[10,20,30]])

In [5]: df1
Out[5]:
    0   1   2
0   2   4   6
1  10  20  30

In [6]: df2=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"])

In [7]: df2
Out[7]:
   Price  Age  Value
0      2    4      6
1     10   20     30

In [8]: df3=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"],index=["First","Second"])

In [9]: df3
Out[9]:
        Price  Age  Value
First       2    4      6
Second     10   20     30

In [10]: df4=pandas.DataFrame([{"Name":"John","Surname":"Johns"},{"Name":"Jack","Surname":"Jacks"}])

In [11]: df4
Out[11]:
   Name Surname
0  John   Johns
1  Jack   Jacks

In [12]: type(df1)
Out[12]: pandas.core.frame.DataFrame