# 
# Python ndarray shape object is useful to display the array shape precisely, and dimensions.

# If it is one dimensional, it returns the number of items.
# If it is two dimensional, returns the rows, columns. Generally, Python assigns a proper data type to the one that we create. However, the Python array function also allows you to specify the data type explicitly using dtype. Using this dtype object, either you can see the data type assigned to it implicitly or can assign your own data type explicitly.

import numpy as np
arr1=np.array([10,50,100,150,250])
arr2 = np.array([[26, 48, 91, 57, 120], [33, 95, 68, 109, 155],
                [111, 194, 7, 22, 124], [ 82, 119, 18, 156, 81],
                [ 38, 10, 151, 24, 14]])
arr3 = np.array([[12, 11, 0, 9, 7], [10, 4, 11, 6, 9],
                [9, 2, 10, 9, 11], [ 5, 14, 0, 11, 8]])

print("Arr 1. :",arr1)
print("Arr 1 Shape:",arr1.shape)


print("Arr 2. :",arr2)
print("Arr 2 Shape:",arr2.shape)


print("Arr 3. :",arr3)
print("Arr 3 Shape:",arr3.shape)