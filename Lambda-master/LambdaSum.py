# We are using the Python lambda expression to add 5 to the given argument value. It accepts one value because we specified one argument after the keyword. After the colon, it is an expression or the functionality it has to perform when we call this anonymous function.
num=lambda a:a+5
print(num(10))

# e are using two arguments to perform addition or find the sum of two numbers. It means we have to assign two values while calling this expression.

# 
add=lambda a,b:a+b
print(add(10,20))

add=lambda x,y: x + y
print(add(10,20))

print("\n Result from a Function")
def add_func(x,y):
    return x + y
print(add_func(10, 20))