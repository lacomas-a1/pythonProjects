# This Python class example is the same as above. However, this time we modified the func_message(self) function definition. It accepts the name (instance variable) and attaches to the message that we print as an output. Let me call this message from two instances emp1 and emp2.

class Employee:
    company='Tutorial Gateway'

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def func_message(self):
        print(self.name + ' is learning programming')


emp=Employee('jack', 43, 'Male')
print(emp.company)
print(emp.name)
print(emp.age)
print(emp.gender)
emp.func_message()


print()
print("................")
emp1=Employee('jane', 33, 'Female')
print(emp1.company)
print(emp1.name)
print(emp1.age)
print(emp1.gender)
emp1.func_message()
