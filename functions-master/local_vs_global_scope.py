# The explanation is that local scope includes all variables defined in the current function and global scope includes
# variables defined outside of the current function.
foo = 1 #global
def func():
    bar = 2 #local
    print(foo)
    print(bar)
print(foo)

# One can inspect which variables are in which scope. Built-in functions locals() and globals() return the whole
# scopes as dictionaries.
foo = 1 #global
def func():
    bar = 2 
    print(globals().keys()) #print all variables name in global scope
    print(locals().keys())  #print all variables names in local scope
print(globals().keys()) #print all variables name in global scope


# What happens with name clashes?
foo = 1 #global
def func():
    foo = 2 #creates a new variable foo in local scope, global foo is not affected
    
    print(foo)
    #global variable foo still exits, unchanged
    print(globals()['foo']) #print 1
    print(locals()['foo'])  #print 2
    
# To modify a global variable, use keyword global:
foo = 1
def func():
    global foo
    foo = 2 #this modifies the global foo, rather than creating a local variable
    print(foo)
    
    
# The scope is defined for the whole body of the function!
foo =1 #global
def func():
    
 # This function has a local variable foo, because it is defined down below.
 # So, foo is local from this point. Global foo is hidden.
    print(foo) # # raises UnboundLocalError, because local foo is not yet initialized
    foo = 7
    print(foo)
    

# Likewise, the opposite:
foo = 1
def func():
 # In this function, foo is a global variable from the beginning
 foo = 7 # global foo is modified
 print(foo) # 7
 print(globals()['foo']) # 7
 global foo # this could be anywhere within the function
 print(foo) #