# the numpy function accepts the argument to specify thw shape or the number of items?
    # one(4) means a one dimentional of four is 1'
    #ones (2,4) means 2*4 matrix of ones
    # ones(2,3,4) means 3D=2*3*4 of 1'

import numpy as np
print(np.ones(5))
print(np.ones((3,3)))
print(np.ones((3,5)))
print(np.ones((3,2,9)))