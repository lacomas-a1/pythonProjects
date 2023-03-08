# Both these keywords are used to gain write access to variables which are not local to the current functions.
# The global keyword declares that a name should be treated as a global variable.
foo = 0 #global foo
def f1():
    foo = 1 # a new foo local in f1
    def f2():
        foo = 2 # a new foo local in f2
        def f3():
            foo = 3 
            print(foo)
            foo =30  #modifies local foo in f3 only
        def f4():
            global foo
            print(foo)
            foo = 100
print(foo)


                #(Python 3 only)
# The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest
# enclosing scope excluding globals.

            #Python 3.x Version ≥ 3.0
def f1():
    def f2():
        foo = 2 # a new foo local in f2
        
        def f3():
            nonlocal foo
            print(foo)  # foo from f2, which is the nearest enclosing scope
            foo = 20
print(foo)
