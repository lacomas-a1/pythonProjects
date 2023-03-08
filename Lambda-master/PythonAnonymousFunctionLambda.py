def new_func(n):
    return lambda a:a*n
number=new_func(2)
print(number(50))

# It calls new_func function where n = 2. It means, the method returns a: a * 2. Then, we assigned that value to the number (lobject)

# number = new_func(2)
# Next, we called that number with 50 (this is the argument value. It means, 50 : 50 * 2 => 100

# Calling this method with different values. First with 2, and then with 3.

def new_fun(n):
    return lambda a: a*n
num1=new_fun(4)
num2=new_fun(3)

print(num1(50))
print(num2(50))