# The rename function present in the os module helps us to rename existing files or even renaming folders

import os
print(os.getcwd())

print(os.listdir())

os.rename("NewPython", "NPython")
print(os.listdir())

# The rename function that we mentioned above also renames the folder