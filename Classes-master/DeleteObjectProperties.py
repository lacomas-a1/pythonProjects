
class Employee:
    company='Tutorial Gateway'

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def func_message(self):
        print(self.name + ' is learning Python')

emp=Employee('Mike', 31, 'Male')
emp1=Employee('Nancy', 25, 'Female')
print(emp.name)
print(emp.age)
print(emp.gender)
emp.func_message()

emp.name='Jane'
emp.gender='Female'
print(emp.name)
print(emp.gender)
emp.func_message()

del emp.name
print(emp.name)
print(emp1.name)

# Remember, deleting an instance property doesn’t affect the other instance property. This Python class example is the same as above. However, this time we created two Instances emp1 and emp2 for the Employee. Next, we deleted the name property of the emp1 object using the del keyword. Next, we are printing the name of emp2 instance and emp1 instance.

# emp2.name returns the name as Nancy but, emp1.name is throwing an error because we deleted it.