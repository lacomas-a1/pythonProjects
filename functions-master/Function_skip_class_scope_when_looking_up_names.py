# Classes have a local scope during definition, but functions inside the class do not use that scope when looking up
# names. Because lambdas are functions, and comprehensions are implemented using function scope, this can lead
# to some surprising behavior.
a ='global'
class Fred:
    a = 'class' # class scope
    b = (a for i in range(10)) #Function scope
    c = [a for i in range(10)]  #Function scope
    d = a # Class scope
    e = lambda: a #Function scope
    f = lambda a=a: a #default argument uses class scope
    
    @staticmethod #or @classmethod, or regular instance method
    def g(): #function scope
        return a
    
print(Fred.a)   #Class
print(next(Fred.b))  #global
print(Fred.c[0]) #class in Python 2, global in Python 3
print(Fred.d) #class
print(Fred.e()) #global
print(Fred.f()) #class
print(Fred.g()) #global

# Users unfamiliar with how this scope works might expect b, c, and e to print class.

# From PEP 227:
# Names in class scope are not accessible. Names are resolved in the innermost enclosing function scope.
# If a class definition occurs in a chain of nested scopes, the resolution process skips class definitions