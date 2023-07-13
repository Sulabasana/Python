password = input("Enter new password: ")

result = {}
#Check len
if len(password) >= 8:
    result['length'] = True
else:
    result["length"] = False

#check digit
digit = False
for i in password:
    if i.isdigit():
        digit = True

result['digits'] = digit
#Check uppercase
upper = False
for i in password:
    if i.isupper():
        upper = True
result["upper-case"] = upper

if all(result.values()) == True:
# if all(result):
    print("Strong password")
else:
    print("Weak password")

print(result)
# print(all(result))