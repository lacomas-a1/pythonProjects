# we show how to delete an object property. Here, emp1 = Employee(‘John’, 25, ‘Male’) creates an instance emp1 for Employee. Next, we are printing the name, age, gender, and the message from the func_message() method.

#  we used the del keyword to delete the emp1 object property called name (del instance_name.property_name). Within the last statement, we again printed the name property of the emp1 object that we deleted. As you can see, it displays an error ‘Employee’ object has no attribute’ name’. It means we successfully deleted the object property. Similarly, you can delete age by del emp1.age and gender by del emp1.gender.

class Employee:
    company='Tutorial Gateway'

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def func_message(self):
        print(self.name + ' is learning Python')

emp=Employee('Mike', 31, 'Male')
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

# Remember, deleting an instance property doesn’t affect the other instance property. This Python class example is the same as above. However, this time we created two Instances emp1 and emp2 for the Employee. Next, we deleted the name property of the emp1 object using the del keyword. Next, we are printing the name of emp2 instance and emp1 instance.

# emp2.name returns the name as Nancy but, emp1.name is throwing an error because we deleted it.