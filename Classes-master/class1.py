class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +last + '@company.com'
    def fullname(self):
        return '{} {}'.format(emp1.first,emp1.last)



emp1 = Employee('corey', 'schafer', 500000)
emp2 = Employee('test', 'user', 700000)

print(emp1)
print(emp2)


print(emp1.email)
print(emp2.email)

print(emp1.fullname())