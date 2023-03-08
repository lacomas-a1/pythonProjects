# This command has several related yet distinct forms.
# del v
# If v is a variable, the command del v removes the variable from its scope. 

x=5
print(x)
del x
print(x)   # NameError: name 'x' is not defined

# Note that del is a binding occurrence, which means that unless explicitly stated otherwise (using nonlocal
# or global), del v will make v local to the current scope. If you intend to delete v in an outer scope, use
# nonlocal v or global v in the same scope of the del v statement
# # 
# del v.name
# This command triggers a call to v.__delattr__(name).
# The intention is to make the attribute name unavailable. 

class A:
    pass
a =A()
a.x = 7
del a.x
print(a.x)
del v[item]
x= {'a':1, 'b':2}
del x['a']
print(x) #out :{'b}:2
print(x['a']) # error: KeyError: 'a'
dev[a:b]
