import os


def change_file_name(file_path, new_name):
    directory = os.path.dirname(file_path)
    new_path = os.path.join(directory, new_name)
    os.rename(file_path, new_path)


change_file_name("NewScript.txt", "NewScript2.py")
