# In Python, variables inside functions are considered local if and only if they appear in the left side of an assignment
# statement, or some other binding occurrence; otherwise such a binding is looked up in enclosing functions, up to
# the global scope. This is true even if the assignment statement is never executed.

x='Hi'
def read_x():
    print (x)  # x is just referenced, therefore assumed global
print(read_x())

# def read_y():  # here y is just referenced, therefore assumed global
#     print(y)
# print(read_y()) # NameError: global name 'y' is not defined

def read_y():
    y= 'Hey'   # y appears in an assignment, therefore it's local
    print(y)    # will find the local y
print(read_y())

# def read_x_local_fall():
#     if False:
#         x = 'Hey'  # x appears in an assignment, therefore it's local
#     print(x)   # will look for the _local_ z, which is not assigned, and will not be found
# print(read_x_local_fall()) # UnboundLocalError: local variable 'x' referenced before assignment

# Normally, an assignment inside a scope will shadow any outer variables of the same name:
x= 'Hi'
def change_local_x():
    x='Bye'
    print(x)
print(change_local_x())
print(x)

# Declaring a name global means that, for the rest of the scope, any assignments to the name will happen at the
# module's top level:
x='Hi'
def change_global_x():
    global x
    x = 'Bye'
    print(x)
print(change_global_x())
print(x)

# The global keyword means that assignments will happen at the module's top level, not at the program's top level.
# Other modules will still need the usual dotted access to variables within the module.

# /*To summarize: in order to know whether a variable x is local to a function, you should read the entire function:
# 1. if you've found global x, then x is a global variable
# 2. If you've found nonlocal x, then x belongs to an enclosing function, and is neither local nor global
# 3. If you've found x = 5 or for x in range(3) or some other binding, then x is a local variable
# 4. Otherwise x belongs to some enclosing scope (function scope, global scope, or builtins)*/