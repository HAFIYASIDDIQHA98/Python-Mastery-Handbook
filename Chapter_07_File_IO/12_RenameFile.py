import os

old_name = "old_name.txt"
new_name = "renamed_by_python.txt"

os.rename(old_name, new_name)
print(f"File {old_name} has been renamed to {new_name}")
