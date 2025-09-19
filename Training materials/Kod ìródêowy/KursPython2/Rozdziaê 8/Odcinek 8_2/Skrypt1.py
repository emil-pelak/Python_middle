import os
import shutil

new_directory = "new_directory"
os.makedirs(new_directory, exist_ok=True)

file_path = "new_directory/NewScript.py"
with open(file_path, 'w') as file:
    file.write("print('Hello World!')")

# Move a file
os.rename("new_directory/NewScript.py", os.getcwd() + "/NewScript.py")
os.rename(os.getcwd() + "/NewScript.py",
          "new_directory/NewScript_ChangedName.py")

# Create a new directory
new_dir_2 = "new_directory_2"
os.makedirs(new_dir_2)

# Move a directory
os.rename("new_directory", "new_directory_2/new_directory_3")

# Copy file
source_file = "new_directory_2/new_directory_3/NewScript_ChangedName.py"
destination_file = "NewScript_Copy.py"
shutil.copy2(source_file, destination_file)

# Copy directory
source_dir = "new_directory_2"
destination_dir = "new_directory_2_copy"
shutil.copytree(source_dir, destination_dir)

file_path = "NewScript_Copy.py"
os.remove(file_path)

dir1_path = "new_directory_2"
shutil.rmtree(dir1_path)

dir2_path = "new_directory_2_copy"
shutil.rmtree(dir2_path)
