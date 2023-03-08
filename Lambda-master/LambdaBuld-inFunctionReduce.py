# The Python lambda reduce function accepts two values and a list as arguments values. Using this reduce along with this.

from functools import reduce
number=[10,20,30,15,25,35,45]
print(number)

print("====================")
add_num=reduce((lambda x,y: x+y),number)
print(add_num)



# First, x = 10, y = 20. Or write it as ((((((10 + 20) + 30) + 15) + 25) + 35) + 45)

