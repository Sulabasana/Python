while True:
    # Get user input from user 
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    match user_action:
        #Check if user action is add        
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)
            
            file=open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        #Check if user action is show
        case 'show' | 'display':
            file = open("todos.txt", 'r')
            todos = file.readlines()
            file.close()

            new_todos = []

            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)
            # for index, item in enumerate(new_todos):
                # item = item.title()
                # row = f"{index + 1}.{item}"
                # print(row)

                # or 
                # new_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                item = item.title()
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edt: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            #  existing_todo = todos[number]
            print(existing_todo)
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
            
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")
print('Bye!')