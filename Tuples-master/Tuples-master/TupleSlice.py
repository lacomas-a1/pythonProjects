#  Slice syntax, the first integer value is the index position where the slicing starts, and the second one is the index position where the slicing end.

# The slicing goes up to second integer value but not include the value at this index position. For instance, if we specify tuple_exmp[1:4], then slicing starts at index position 1 and ends at position 3 (not 4).

x=(1,2,3,4,5,6,7,8,9)
#Slicing using two indexes
a=x[2:6]
print(a)

# Slicing using First??
b=x[:6]
print(b)

# Using Second
c=x[2:]
print(c)

# Without using two
d=x[:]
print(d)

# Slicing using negative?
e=x[-3:]
print(e)

# Slice using Negative?
f=x[:-2]
print(f)

# Slicing analysis

# If no first index, then Python Slicing starts from the beginning
# If the second index not provided, Slicing starts from the first index and continue to the last
# Using the Negative numbers as the index, Slicing starts from right to left.
