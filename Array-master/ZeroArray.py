# Numpy creates an array of zeros.This function accepts the arguments to specify the shape.eg:
    #zeros(2) means a one-dimensional of two zero elements.print()
    #zero(2,3) means 2*3 matrix of zeros.
    #Zero(2,3,4) means of three-dimentional of zeros.

import numpy as np

print(np.zeros(3))
print(np.zeros((2,2)))

print(np.zeros((2,3)))
print(np.zeros((4,7)))
print(np.zeros((3,2,7)))