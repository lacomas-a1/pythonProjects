# The following Numpy ndarray objects help to find the information about an array.

# ndim: Returns the dimension. If it is a one-dimensional, then 1, two-dimensional = 2, etc.
# size: It displays or returns the number of elements or items.
# flags: Information about the memory layout.
# itemsize: Length in bytes.
# nbytes: Total number of bytes consumed it.

import numpy as np
a=np.array([10,50,100,150,250])
b=np.array([[26, 48, 91, 57, 120], [33, 95, 68, 109, 155],[111, 194, 7, 22, 124], [ 82, 119, 18, 156, 81], [38, 10, 151, 24, 14]])

print('Dimension=',a.ndim)
print('No of Elements=',a.size)
print('Memory Layout=',a.flags)
print('Lenght in Bytes=',a.itemsize)
print('Total Bytes Consumed=',a.nbytes)

print('\nDimension = ', b.ndim)
print('No of Elements = ', b.size)
print('Memory Layout = ', b.flags)
print('Length in Bytes = ', b.itemsize)
print('Total bytes consumed = ', b.nbytes)