#repr(x) calls x.__repr__(): a representation of x. eval will usually convert the result of this function back to the
#original object.
s = """w o"w"""
repr(s) #output: '\'w\\\'0"w''
str(s) #output: 'w\'o"w'
print(eval(repr(s))==s) #Output: True

print(eval(str(s))==s)#Give a syntaxError