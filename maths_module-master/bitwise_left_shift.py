# The << operator will perform a bitwise "left shift," where the left operand's value is moved left by the number of bits
# given by the right operand.
print(2 << 2)
print(bin(2 << 2))

# Performing a left bit shift of 1 is equivalent to multiplication by 2:
print(7 << 1)

# Performing a left bit shift of n is equivalent to multiplication by 2**n:
print(3 << 4)