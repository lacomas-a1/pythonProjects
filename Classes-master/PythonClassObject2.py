
# Within the last twn this Python class example, we declared a variable company, and we defined a function with a self parameter that prints a welcome message. Next, we created an object emp1 for Employee. By using this object emp1, we are accessing the company variable, and func_message().
# o statements, we used the attribute reference to access the variable value and the function result. By using attribute reference, you can print the variable value. However, Employee.func_message returns the function object but not the actual function result. So, you should remember this concept while working with attribute references in a python class.

class Employee:
    company='Tutorial Gateway'

    def func_message(self):
        print("Welcome to Python Programming")

emp=Employee()
print(emp.company)
emp.func_message()

print("....................")
print(Employee.company)
print(Employee.func_message)