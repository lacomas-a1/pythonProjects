#This function greets all the person in the names tuple.
def greet(*names):
    for name in names:
        print("Hello", name)
greet("Monica", "Luke", "Steve")