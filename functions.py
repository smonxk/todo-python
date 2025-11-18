def get_todos(filepath = "todos.txt"):
    """ Read a txt file and return the list of
     to-do items
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def save_todos(todos_arg, filepath = "todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)