x=[1,2,3,4,5,6,7,8,9]
# Slicing using two indexes?
a=x[2:6]
print(a)

# Slicing using First
b = x[:6] 
print(b)

# Slicing using Second
c = x[2:] 
print(c)

# Slicing without using two
d = x[:] 
print(d)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing using Negative first
e = x[-3:] 
print(e)

# Slicing using Negative Second
f = x[:-2] 
print(f)

# Slicing using Negative first and second
g = x[-7:-2] 
print(g)

# Assigning new values
x[1:3] = ['t','g']
print(x)

# From the above slicing

# Omit the first index means the Slicing start from the beginning.
# Omit the second, slicing start from the first index and continue to the last.
# Use the Negative values to Slice the elements from right to left.