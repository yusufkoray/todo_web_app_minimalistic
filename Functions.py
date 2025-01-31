FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH): # filepath default argument is todos.txt
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos, filepath=FILEPATH):
    """
    This function takes an arguments of todos and filepath and write todos to the filepath.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos)

if __name__ == "__main__":
    print("Hello")
