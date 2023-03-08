# # 
# Generally, Python assigns a proper data type to an array that we create. However, the Python function also allows you to specify the data type of an array explicitly using dtype. Using this dtype object, either you can see the data type assigned to an array implicitly or can assign your own data type explicitly.

# List of available data types to create a Python ndarray.

# Data Type	Description	Data Type Code
# int8	Signed 8 bit integer type	i1
# uint8	Unsigned 8 bit integer type	u1
# int16, uint16	Signed and Unsigned 16 bit integer types	i2, u2
# int32, uint32	Signed & Unsigned 32 bit integer types	i4, u4
# int64, uint64	Signed & Unsigned 64-bit integer types	i8, u8
# float16	Half Precision floating point	f2
# float32	Single Precision floating point	f4 or f
# float64	Double Precision floating point	f8 or d
# float128	Extended Precision floating point	f16 or g
# complex64, complex128, complex256	Complex numbers represented by 32, 64, 128 etc	c8, c16, c32
# bool	Boolean True or False Type	?
# object	Object Type	O
# string_	String type. You have to specify the string length (no of characters). For example, 5 characters mean S5	S
# unicode_	Unicode Type. You have to specify the number of bytes. For example, 10 means U10.	U
# In this Python example, we are creating two ndarrays. First, we create an array of integers and mixed values (float and integer). 

import numpy as np
arr1=np.array([10,20,30,40,50])

print("Arr :",arr1)
print("Data Type:",arr1.dtype)

arr2=np.array([1,3.10,4.60,5,7.96])
print("Arr :",arr2)
print("Data Type:",arr2.dtype)
