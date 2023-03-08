# me that we defined in our previous example. Here, first, we create an object of Employee and displaying the employee name, age, gender, and the message from the func_message() method. Please refer static methods article.
# Next, we used the del keyword to delete the object emp1 (del Object_name). It deletes the instance emp1 that we created earlier. In the last statement, we called the func_message() method with an emp1 object to check whether the object still exists or not. As you see, it was throwing an error name ’emp1′ is not defined. It means, we deleted the emp1 object by the del statement.

class Employee:
    company='Tutorial Gateway'

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def func_message():
        print(self.name + ' is learning Programming')

emp=Employee('John', 32, 'Male')
print(emp.name)
print(emp.age)
print(emp.gender)
emp.func_message()

del emp
# emp.func_message()