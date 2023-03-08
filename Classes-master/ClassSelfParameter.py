# The Python self parameter is nothing but a reference to the current instance of a class. We have to use this Python class self parameter as the first parameter, which helps us to access the variables.
# If you don’t like the keyword self, then use any word as a self parameter. However, it has to be the first parameter. In this Python class example, we used suresh instead of self in the third method.

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def func_message(self):
        print(self.name + 'is learning Programming')

    def fun_msg(suresh):
        print('Tutorial Welcome ' + suresh.name)

emp=Employee('John', 35)
emp.func_message()
emp.fun_msg()
