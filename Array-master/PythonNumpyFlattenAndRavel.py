# Both Python Numpy Array flattens, and ravel functions flatten or converts any size to a single dimensional. Although both are the same, the ravel function holds the reference of an actual one. It means any changes made to ravel output also reflect the original. However, this is not the same as the flatten function.Both Python Numpy Array flattens, and ravel functions flatten or converts any size to a single dimensional. Although both are the same, the ravel function holds the reference of an actual one. It means any changes made to ravel output also reflect the original. However, this is not the same as the flatten function.

import numpy as np
arr1=np.array(np.random.randint(1,20,size=(3,6)))
print("-----------Arr-------\n",arr1)

x=arr1.flatten()
print("------Flatten----\n",x)

y=arr1.ravel()
print("-------Ravel-----\n",y)

arr2 = np.array(np.random.randint(10, 30, size = (2, 3, 4)))
print("-----2nd------\n", arr2)

a = arr2.flatten()
print("------flatten 2------\n", a)

b = arr2.ravel()
print("------ravel 2------\n", b)