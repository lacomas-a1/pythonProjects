# Python class Object
# In Python, class objects supports both the attribute reference and instantiation. You can use either of them to call the class attributes. It is an example of both the instantiation and the attribute reference.

# The attribute reference uses CLName.Variable_name or CLName.function_name.
# For the instantiation, you have to create an instance or a copy of that Python class. To create an instance use instance_name = CLName(), to call the variable instance_name.variable_name and to call the method instance_name.method_name()
# Here, emp = Employee() is creating an instantiation, and emp.company inside print means calling class variable. Next, Employee.company is an example of attribute reference.

class Employee:
    company='Tutorial Gateway'

emp=Employee()
print(emp.company)

print(".................")
print(Employee.company)
    
    #  declared a variable company, and we defined a function with a self parameter that prints a welcome message. Next, we created an object emp1 for Employee. By using this object emp1, we are accessing the company variable, and func_message().
