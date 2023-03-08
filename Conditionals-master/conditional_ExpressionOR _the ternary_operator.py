# The ternary operator is used for inline conditional expressions. It is best used in simple, concise operations that are
# easily read.

n = 5
print("Greater than 2" if n > 2 else "Smaller than or equal to 2")

n = 5
print("Hello" if n > 10 else "Goodbye" if n > 5 else "Good day")