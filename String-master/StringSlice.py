#  the first integer value is the index position where the slicing start and the second is where the slicing end, but it does not include the content at this index position
x="Tutorial Gateway"
#USing two
a=x[2:13]
print(a)

#USing Second
b=x[:8]
print(b)

# Slice using First
c = x[4:] 
print(c)

# without using two 
d = x[:] 
print(d)

# Slice using Negative first
e = x[-3:] 
print(e)

# Slice using Negative second
f = x[:-2] 
print(f)