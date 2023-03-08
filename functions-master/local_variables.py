# If a name is bound inside a function, it is by default accessible only within the function
# def foo():
#     a=5
#     print(a)
# print(a)  # NameError: name 'a' is not defined

# Control flow constructs have no impact on the scope (with the exception of except), but accessing variable that was
# not assigned yet is an error

def foo():
    if True:
        a=5
    print(a)
    
b=3
def bar():
    if False:
        b=5
    print(b) # UnboundLocalError: local variable 'b' referenced before assignment
