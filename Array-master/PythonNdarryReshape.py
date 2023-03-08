# Numpy Array reshape function helps to reshape or change the size as per your requirement. Here, First, we are changing single dimensional to two-dimensional. Next, we changed the shape to 4 * 3, and 2 * 6.

import numpy as np
arr1=np.array([10,20,30,40,50,60,70,80])
print("Arr :",arr1)

x=arr1.reshape(2,4)
print("------------New 2*4-------\n",x)

y = arr1.reshape(4, 2)
print("------New 4 * 2------\n", y)

arr2=np.array(np.random.randint(1,9, size=(3,4)))
print("-----Arr2------\n",arr2)

a=arr2.reshape(4,3)
print("-------New Arr2 4*3------\n",a)

b = arr2.reshape(2, 6)
print("------New Arr2 2 * 6------\n", b)

