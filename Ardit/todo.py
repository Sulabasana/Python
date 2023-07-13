while True:
    # Get user input from user 
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    match user_action:
        #Check if user action is add        
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            
            with open("todos.txt", "r") as file:
                todos = file.readlines()     
            
            todos.append(todo)
            
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            
        #Check if user action is show
        case 'show' | 'display':
            with open("todos.txt", "r") as file:
                todos = file.readlines()  


            for index, item in enumerate(todos):
                item = item.strip("\n")
                item = item.title()
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edt: "))
            number = number - 1
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
            #  existing_todo = todos[number]
            
        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
                
            message = f"Todo {todo_to_remove} was removed from the list"
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")
print('Bye!')