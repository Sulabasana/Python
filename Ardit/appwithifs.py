# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%d.%m.%Y %H:%M:%S")
print("It is", now)

while True:
    # Get user input from user 
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

#Check if user action is add        
    if user_action.startswith('add'):
        todo = user_action[4:]        
        todos = functions.get_todos()     
        
        todos.append(todo)
          
        functions.write_todos(todos)
        
    #Check if user action is show
    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = functions.get_todos()
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            
            write_todos(todos)
        
            #  existing_todo = todos[number]
        except ValueError:
            print("Your command is not valid.")
            continue #wróci do początku

    elif user_action.startswith('complete'):
        try:
            number = int(input("Number of the todo to complete: "))

            todos = get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            
            write_todos(todos)
        
                
            message = f"Todo {todo_to_remove} was removed from the list"
        except IndexError:
            print("There is no item with this index")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")    
print('Bye!')