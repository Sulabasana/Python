# user_prompt = "Enter a todo: "

# todos = []
# while True:
#     todo = input(user_prompt)
#     print(todo.capitalize())
#     print(todo.title())
#     todos.append(todo)
#     print(todos)

# dir(str)
# help(str.capitaize)

todos = []
while True:
    user_action = input("Type add or show: ")
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break 

print('Bye!')