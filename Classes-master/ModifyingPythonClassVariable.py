#  First, we declared a company variable and a function that prints a welcome message. Next, we created three instances emp1, emp2, and emp3 of the Employee.
# Next, we used Object_name.Variabel_name = New_Name to change the name of the company for emp2 and emp3 objects. It changes the company names for both these instances. Next, we are printing the company variable from all these three instances.

class Employee:
    company='Tutorial Gateway'

    def func_message(self):
        print('Welcome to Programming')

emp=Employee()
emp1=Employee()
emp2=Employee()

emp1.company='python'
emp2.company='Apple'

emp.func_message()

print(emp.company)
print(emp1.company)
print(emp2.company)
