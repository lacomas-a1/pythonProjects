# The >> operator will perform a bitwise "right shift," where the left operand's value is moved right by the number of
# bits given by the right operand.
print(8 >> 2)
print(bin(8 >> 2))

# Performing a right bit shift of 1 is equivalent to integer division by 2:
print(36 >> 1)
print(15 >> 1)

# Performing a right bit shift of n is equivalent to integer division by 2**n:
print(48 >> 4)
print(59 >> 3)