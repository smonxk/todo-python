import functions as fns
import FreeSimpleGUI as gui

label = gui.Text("Type your to-do")
input_box = gui.InputText(tooltip="Enter to-do")
add_button = gui.Button("Add")


window = gui.Window("To-do app", layout=[[label], [input_box, add_button]])
window.read()
window.close()