# By default, all the Python classes in real-time have an __init__() function. Use this function to assign values to the properties of an object. When you create an object of a Python class, it automatically calls the __init__() function. You don’t have to call it.
# 
# 

class Employee:
    company='Tutorial Gateway'

    def __init__(self):
        print("HellO World")

    def func_message(self):
        print("Welcome to Python Programming")

emp=Employee()  #CREATEED AN INSTANCE 

print(emp.company)
emp.func_message()
