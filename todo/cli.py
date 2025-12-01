import functions as fns
import time as tm



user_prompt = "Type add, show, edit, complete or exit: "
date = tm.strftime("%d %b, %Y %H:%M:%S")
print("It is: ", date)

while True:
    user_action = input(user_prompt).lower().strip()

    
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = fns.get_todos()

        todos.append(todo + "\n")

        fns.save_todos(todos)
        
    elif user_action.startswith("show"):
        todos = fns.get_todos()
        
        for index, item in enumerate(todos):
            row = f"{index+1}. {item.strip("\n").capitalize()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            new_todo = input("Enter a new todo: ")
            
            todos = fns.get_todos()
            
            todos[number - 1] = new_todo + "\n"
            
            fns.save_todos(todos)
            
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:   
            projNumber = int(user_action[9:])

            todos = fns.get_todos()
            
            deleted_todo = todos.pop(projNumber - 1)

            fns.save_todos(todos)

            print(f"Todo {deleted_todo.strip("\n")} was removed from the list.")
        
        except ValueError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
