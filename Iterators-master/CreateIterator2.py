# In this program, we used for loop to iterate the Counter class where the maximum value is 10. This prints the values from 0 to 10. __iter__() starts at 0, and __next__() print elements up to 10.

class Counter:

    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        number = self.number

        if number > self.maximum:
            raise StopIteration
        else:
            self.number = number + 1
            return number

for t in Counter(10):
    print(t)
