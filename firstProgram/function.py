# Implements a function that takes two string as parameters, concatenates them and returns the result
def concat(a,b):
    return a + b
#AVG funtion
def foo(*args):
    return sum(args)/len(args)
#Capitalize strings
def bar(*args):
    args = [x.upper() for x in args]
    return sorted(args)