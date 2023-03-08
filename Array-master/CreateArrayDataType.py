# We can use this property to create an array of our own data types.
import numpy as np
list1=[10,20,30,40,50]
arr1=np.array(list1,dtype='int')

print(arr1)
print("Arr      :",arr1)
print("Data Type:",arr1.dtype)

arr2 = np.array(list1, dtype = 'float')
print("Arr2      : ", arr2)
print("Data Type : ", arr2.dtype)

arr3 = np.array(list1, dtype = 'float16')
print("Arr3      : ", arr3)
print("Data Type : ", arr3.dtype)