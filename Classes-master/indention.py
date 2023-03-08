class ExampleClass:
    # Every function belonging to a class must be indented equally
    def __init__(self,):
        name= "example"

    def someFunction(self, a):
        # Notice everything belonging to a function must be indented
        if a > 5:
            return True
        else:
            return False
#If a function is not indented to the same level it will not be considers as part of the parent class
def separateFunction(b):
    for i in b:
        if i==1:
            return  True
    return  False
print(separateFunction([2,3,5,6,1]))