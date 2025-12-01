import functions as fns
import FreeSimpleGUI as gui

label = gui.Text("Type your to-do")
input_box = gui.InputText(tooltip="Enter to-do", key="todo")
add_button = gui.Button("Add")


window = gui.Window("To-do app",
                    layout=[[label], [input_box, add_button]],
                    font=("Helvetica", 18))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match(event):
        case "Add":
            todos = fns.get_todos()
            new_todo = values["todo"]
            todos.append(new_todo.capitalize() + "\n")
            fns.save_todos(todos)
        case gui.WIN_CLOSED:
            break

window.close()