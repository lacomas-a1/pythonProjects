# , let me use the negative values as the start and end positions.

import numpy as np
arr1=np.array([10,25,50,75,100,125,150,200,250])
arr2=np.array([[26,48,91,57,120],[33,95,68,109,155],[111,194,7,22,124],[82,119,18,156,81],[38,10,151,24,14]])

print(arr1[:3])
print(arr1[:-4])
print(arr1[-4:])
print(arr2[:-2,:-1])
print(arr2[:-3,:-1])
print(arr2[:-3])
print(arr2[:,:-3])
