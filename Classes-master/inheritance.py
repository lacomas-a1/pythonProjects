#inheritance
class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am{self.name} and I am {self.age} years old")

class Cat(pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am{self.name} and I am {self.age} years old and I am {self.color}")

class Dog(pet):
    def speak(self):
        print("Bark")

p = pet(" Tim", 19)
p.show()
c = Cat(" Bill", 34 ," black")
c.show()
d = Dog(" Jill", 16)
d.show()
c.speak()
d.speak()
