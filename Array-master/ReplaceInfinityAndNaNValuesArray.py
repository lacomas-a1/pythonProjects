# Replacing Not a Number and infinity values in a Python ndarray with exact numbers or values. Here, we declared 1D and 2D array with random values. Next, we replaced infinity and Nan with 11.56 and 29.16.

# 
import numpy as np
arr1=np.array([10,25,50,90,5,40,60,30,25], dtype='float')
print(arr1)

#Replace inf and nan with 11.56
x=np.isinf(arr1) | np.isnan(arr1)
arr1[x]=11.56 
print(arr1)

arr2=np.array([[9,7,np.nan,8,np.inf],[np.nan,3,7,np.inf,5],[8,np.inf,4,np.nan,1]], dtype='float')
print("\n--------------\n")
print(arr2)

# Replace inf and nan in arr2 with 29.16
y=np.isinf(arr2) | np.isnan(arr2)
arr2[y]=29.16
print("\n--------------------------\n")
print(arr2)