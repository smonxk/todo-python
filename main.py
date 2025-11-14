user_prompt = "Type add, show, edit, complete or exit: "

while True:
    user_action = input(user_prompt).lower().strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            for index, item in enumerate(todos):
                row = f"{index+1}. {item.strip("\n").capitalize()}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            new_todo = input("Enter a new todo: ")
            
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            todos[number - 1] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
            
        case "complete":
            projNumber = int(input("Number of the todo to complete: "))
            

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            deleted_todo = todos.pop(projNumber - 1)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print(f"Todo {deleted_todo.strip("\n")} was removed from the list.")

        case "exit":
            break
