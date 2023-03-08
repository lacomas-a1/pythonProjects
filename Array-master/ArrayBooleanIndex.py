# The boolean index in Python Numpy ndarray object is an important part to notice. You can use this boolean index to check whether each item in an array with a condition.
# First, x = arr1 > 40 returns an array of boolean true and false based on the condition (arr1 > 40). I mean, if a value is greater than 40 True otherwise, False. Next, arr1[x] returns an array of a sequence whose value is greater than 40. The same applies to multi-Dimensional arrays.

import numpy as np
arr1=np.array([10,20,50,90,5,40,60,30,25])
x=arr1>40
print(arr1)
print("Bool index:",x)
print(arr1[x])

y=arr1<40
print("\nBool index:",y)
print(arr1[y])

arr2=np.array(np.random.randint(1,10, size=(3,8)))
z=arr2>4
print("\n----Arr2-----\n",arr2)
print("\n----Bool index-----\n",z)
print("\n----Arr2 of z-----\n",arr2[z])