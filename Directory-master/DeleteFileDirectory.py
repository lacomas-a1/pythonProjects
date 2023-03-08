# A remove function is to remove files from a folder. This example uses a sample inside the remove function to delete the CopyFile.txt.
# 

# import os
# print(os.getcwd())

# print(os.listdir())

# os.remove('copy.txt')
# print(os.listdir())

# the above is used to remove files

import os
print(os.getcwd())

print(os.listdir())

os.rmdir("NPython")
print(os.listdir())