import functions as fns
import FreeSimpleGUI as gui

label = gui.Text("Type your to-do")
input_box = gui.InputText(tooltip="Enter to-do", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=fns.get_todos(), key="todo_select", 
                       enable_events=True, size=[45,10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")

exit_button = gui.Button("Exit")


window = gui.Window("To-do app",
                    layout=[[label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica", 18))

while True:
    event, values = window.read()
    print(event, "event")
    print(values)
    match(event):
        case "Add":
            todos = fns.get_todos()
            new_todo = values["todo"]
            todos.append(new_todo.capitalize() + "\n")
            fns.save_todos(todos)
            window["todo_select"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todo_select"][0]
            new_todo = values["todo"] + "\n"

            todos = fns.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            fns.save_todos(todos)

            window["todo_select"].update(values=todos) #real-time update
        case "todo_select":
            window["todo"].update(value=values[event][0])
        case "Complete":
            todo_to_complete = values["todo_select"][0]
            todos = fns.get_todos()
            todos.remove(todo_to_complete)
            fns.save_todos(todos)
            window["todo_select"].update(values = todos)
            window["todo"].update(value = "")
        case "Exit":
            break
        case gui.WIN_CLOSED:
            break

window.close()