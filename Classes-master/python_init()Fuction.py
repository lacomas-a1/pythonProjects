# e use the __init__() function to add values to the properties in a Python class. Here, we used name, age, gender in the function, and assigned those values in the next line. It means, when you create an object of employee, you have to provide the name, age, and gender (while creating the object itself).

# For instance, if you create an object emp1 = Employee() without the argument values, then the following error raised. TypeError: __init__() missing 3 required positional arguments: ‘name’, ‘age’, and ‘gender’

class Employee:
    company='Tutorial Gateway'

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def func_message(self):
        print('Welcome to Python Progrmming')

emp=Employee('jack', 56, 'male')

print(emp.company)
emp.func_message()
print(emp.name)
print(emp.age)
print(emp.gender)



class Employee:
    company = 'Tutorial Gateway'

    def __init__(self, n, a, gen):
        self.name = n
        self.age = a
        self.gender = gen

    def func_message(self):
        print('Welcome to Python Programming')

emp1 = Employee('Johnson', 29, 'Male')
 
print(emp1.company)
emp1.func_message()
print(emp1.name)
print(emp1.age)
print(emp1.gender)
