# The Python Numpy Array module has a unique function used to find and return the unique values from a given 1D, 2D, and 3 or multi Dimensional.

import numpy as np

arr = np.random.randint(0, 5, size = 10)
print('Original = ', arr)

arr2=np.random.randint(10,100,size=(3,5))
print('\n--Two Dimensional Random Original--\n',arr2)

uniq2 = np.unique(arr2)
print('Unique Items=',uniq2)

arr3 = np.random.randint(15, 25, size = (2, 3, 8))
print('\n----Three Dimensional Random Original ----\n', arr3)

uniq3 = np.unique(arr3)
print('Unique Items = ', uniq3)