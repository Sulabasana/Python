# Copy value x times
with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)

#Read and Append. Append Bear1.txt to Bear2.txt
with open("bear1.txt", 'r') as b:
    content = b.read()
with open('bear2.txt', 'a') as b1:
    b1.write(content)

#Write First 90
with open('bear.txt', 'r') as b:
    content = b.read()
    countchar = content[:90]
with open('first.txt', 'w') as f:
    f.write(countchar)

#Function that gets a single string as character and filepath as parameters and returns number of occurence of that charaacter in that file
def foo(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)