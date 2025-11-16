user_prompt = "Type add, show, edit, complete or exit: "

while True:
    user_action = input(user_prompt).lower().strip()

    
    if user_action.startswith("add"):
        todo = user_action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        
        for index, item in enumerate(todos):
            row = f"{index+1}. {item.strip("\n").capitalize()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            new_todo = input("Enter a new todo: ")
            
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            todos[number - 1] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:   
            projNumber = int(user_action[9:])
            

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            deleted_todo = todos.pop(projNumber - 1)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print(f"Todo {deleted_todo.strip("\n")} was removed from the list.")
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
