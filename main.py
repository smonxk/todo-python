def get_todos(filepath):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def save_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

user_prompt = "Type add, show, edit, complete or exit: "

while True:
    user_action = input(user_prompt).lower().strip()

    
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + "\n")

        save_todos("todos.txt", todos)
        
    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")
        
        for index, item in enumerate(todos):
            row = f"{index+1}. {item.strip("\n").capitalize()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            new_todo = input("Enter a new todo: ")
            
            todos = get_todos("todos.txt")
            
            todos[number - 1] = new_todo + "\n"
            
            save_todos("todos.txt", todos)
            
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:   
            projNumber = int(user_action[9:])

            todos = get_todos("todos.txt")
            
            deleted_todo = todos.pop(projNumber - 1)

            save_todos("todos.txt", todos)

            print(f"Todo {deleted_todo.strip("\n")} was removed from the list.")
        
        except ValueError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
