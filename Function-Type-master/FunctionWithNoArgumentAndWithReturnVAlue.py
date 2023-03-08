# In this type of function in Python, We won’t pass any arguments to the function while defining, declaring, or calling the function. When we call the Python function, this type of function returns some value.

#python Function with no arguments and with return value

def Multiplication():
    a=10
    b=25
    Multi=a*b
    return Multi
print("After calling the Mu;tiplication function:",Multiplication())
print(Multiplication())

# Within the Multiplication () function, We haven’t passed any arguments /parameters. Next, We declared the integer variables of Multi, a, b, and we assigned 10 to a, and 25 to b. In the next line, we Multiplied both a and b using an Arithmetic operator ( * ).

# a = 10
# b = 25
# Multi = a * b
# Lastly, the print statement is to print the output. Remember, we are using the print statement outside the defined function, and we are using the function name inside the print statement. (nothing but calling the function)

# print("After Calling the Multiplication Function: ", Multiplication())
# Here also, Whenever we call the Multiplication() function, it prints the same output because a and b have fixed values inside the function.