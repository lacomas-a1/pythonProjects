import numpy as np
list1=[1,20,40,0,40,0]

arr1=np.array(list1,dtype='S')
print("Arr1: ", arr1)
print("Arr1 Data Type:",arr1.dtype)

arr2 = np.array(list1, dtype = 'bool')
print("Arr2           : ", arr2)
print("Arr2 Data Type : ", arr2.dtype)

arr3 = np.array([1, 10, 'e', 'o', 9, 'Hi', 7], dtype = 'object')
print("Arr3           : ", arr3)
print("Arr3 Data Type : ", arr3.dtype)