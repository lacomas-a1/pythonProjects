import numpy as np
arr1=np.array([10,50,100,150,250])
arr2=np.array([[26,48,91,57,120],[33,95,68,109,155],[111,194,7,22,124],[82,119,18,156,81],[38,10,151,24,14]])

print(arr1[::-1])
#Reverse the row position only
print(arr2[::-1,])
#Reverse both the row and column position
print(arr2[::-1,::-1])