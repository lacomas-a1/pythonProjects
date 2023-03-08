def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer
c= counter()
print(c())

# Basically nonlocal will allow you to assign to variables in an outer scope, but not a global scope. So you can't use
# nonlocal in our counter function because then it would try to assign to a global scope. Give it a try and you will
# quickly get a SyntaxError. Instead you must use nonlocal in a nested function.
# (Note that the functionality presented here is better implemented using generators.)