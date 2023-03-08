#the scope of a variable inside a function.
def my_func():
    x=10
    print("values inside function: ",x)

x=20
my_func()
print("value outside function: ",x)