# we show the different ways to create a class in python. As you can see, either you can use c_name Employee, c_name(), or c_name(object). The last option with the object is the latest one to create a class in python. If you look close to object creation, we used the same approach to create the object for all those three.

class Employee:
    def __init__(self):
        print('Msg from Employee: Welcome to Tutorial Gateway')

class Students:
    def __init__(self):
        print('Msg from Students: HEllo World')

class Person:
    def __init__(self):
        print('Msg from Person: Welcome to Programming')

emp=Employee()
std=Students()
per=Person()