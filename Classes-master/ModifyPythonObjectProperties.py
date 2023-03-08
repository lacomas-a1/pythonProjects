# irst, we created an instance emp1 of the Employee with the required fields. Next, we are printing the available values as an output.
# Here, emp1.name = ‘John’ (object_name.property_name = New_Value) statement updates the existing emp1 name (Mike) to John. Let me check the same by printing the emp1 name one more time.


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

