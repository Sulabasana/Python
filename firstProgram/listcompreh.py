# Define a function that takes as a parameter a list that contains both numbers and strings and returns the list containing only the numbers. For example, if I&nbsp;called your function with foo([99, 'no data', 95, 94, 'no data'])  it should return [99, 95, 94]
def checklist(list):
   return [i for i in list if not isinstance(i,str)]


# Define a function that takes as a parameter a list that contains both numbers and strings and returns the list containing only the numbers. For example, if I&nbsp;called your function with foo([99, 'no data', 95, 94, 'no data'])  it should return [99,0, 95, 94,0]

def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst ] #jeżeli nie jest stringiem to wpisz to co jest a jak jest stringiem to zmień na 0

# <foo(['1.2', '2.6', '3.3']) return sum

def foo1(lst):
    return sum([float(i) for i in lst])