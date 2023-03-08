#And operator
# The and operator evaluates all expressions and returns the last expression if all expressions evaluate to True.
# Otherwise it returns the first value that evaluates to False:

print(1 and 2)

print( 1 and 0)

print(1 and "Helloworld")

print("" and "Pancakes")

#Or operator
# The or operator evaluates the expressions left to right and returns the first value that evaluates to True or the last
# value (if none are True).
print(1 or 2)

print(None or 1)

print(0 or [])

#Lazy evaluation
# When you use this approach, remember that the evaluation is lazy. Expressions that are not required to be
# evaluated to determine the result are not evaluated
def print_me():
    print('I am here!')
print(0 and print_me())

#Testing for multiple conditions
# A common mistake when checking for multiple conditions is to apply the logic incorrectly.
# This example is trying to check if two variables are each greater than 2. The statement is evaluated as - if (a) and
# (b > 2). This produces an unexpected result because bool(a) evaluates as True when a is not zero.

a= 1
b= 6
if a and b > 2:
    print("yes")
else:
    print("No")
    
# Each variable needs to be compared separately.
if a > 2 and b > 2:
    print("yes")
else:
    print("no")
    
# Another, similar, mistake is made when checking if a variable is one of multiple values. The statement in this
# example is evaluated as - if (a == 3) or (4) or (6). This produces an unexpected result because bool(4) and
# bool(6) each evaluate to True

a= 1
if a == 3 or 4 or 6:
    print("yes")
else:
    print("no")

# Again each comparison must be made separately
if a == 3 or a==4 or a ==6:
    print("yes")
else:
    print("no")
    
# Using the in operator is the canonical way to write this
if a in (3,4,6):
    print("yes")
else:
    print("no")
