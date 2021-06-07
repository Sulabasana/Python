import pyperclip
userName = input("Please provide a name: \n")
print(f'You entered {userName}')
capitalized = userName.title()
print(f'The name is \n{capitalized}')

pyperclip.copy(capitalized)

# space = userName.split(' ')
# print(space)

# for word in space:
#     # print(word)
#     capitalized = word.capitalize()
#     # print(capitalized)
#     mySeparator = ""
#     joined = mySeparator.join(capitalized)
#     print(joined)
    

    
# # print(joined)    
# # capitalized = word.capitalize()
# # print(capitalized)