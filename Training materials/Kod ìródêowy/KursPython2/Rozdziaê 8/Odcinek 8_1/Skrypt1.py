import os

print("Get current working directory:", os.getcwd())
print(os.path.dirname(__file__) + " + " + os.path.basename(__file__))
print(os.path.abspath(__file__))


def dir(path):
    # Check if path exists
    if not os.path.exists(path):
        print(f"Path {path} does not exist.")
        return

    # Get the list of files and folders in the path
    items = os.listdir(path)

    # Iterate over and display items
    for item in items:
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path):
            # Display file name and file size in bytes
            print(f"File Name: {item} ({os.path.getsize(item_path)} bytes)")
        elif os.path.isdir(item_path):
            print(f"Folder Name: {item}")


path = os.path.abspath("../..")
print(path)

dir(path)


def tree(path, indent=''):
    if not os.path.isdir(path):
        return

    files = os.listdir(path)

    for file in sorted(files):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            print(f"{indent}├── {file}")
            tree(file_path, indent + "│   ")
        else:
            print(f"{indent}└── {file} ({os.path.getsize(file_path)} B)")


path = os.path.abspath("../..")
tree(path)
