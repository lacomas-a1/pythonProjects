# Creating an array using ndarray slicing technique output
import numpy as np
arr1=np.array([10,50,100,150,250])
arr2=np.array([[26,48,91,57,120],[33,95,68,109,155],[111,194,7,22,124],[82,119,18,156,81],[38,10,151,24,14]])

arr3=arr1[2:7]
print(arr3)

arr4=arr1[3:]
print(arr4)

arr5=arr2[::-1,]
print(arr5)

arr6=arr2[::-1, ::-1]
print(arr6)
