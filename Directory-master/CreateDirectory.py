import os
print(os.getcwd())

os.mkdir('NewPython')
print(os.listdir())


# Let me provide the full path so that I can create a folder in a different location. Here, we first created a folder. Next, we changed the current working folder using the chdir method. Next, listing the documents and folders inside that it using listdir.

import os
print(os.getcwd())

os.mkdir('/home/lacomas/Documents/NewPython')
os.chdir('/home/lacomas/Documents')
print(os.listdir())