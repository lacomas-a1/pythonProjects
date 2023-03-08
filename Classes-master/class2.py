#class method
class person:

    number_of_people = 0 #class attribute
    GRAVITY = -9.8
    def __init__(self, name):
        self.name =name
        person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = person("tim")
p2 = person("jill" )
print(person.number_of_people)
