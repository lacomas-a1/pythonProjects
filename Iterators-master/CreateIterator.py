
# It is a simple class called Counter. First, we declared a maximum value within the __init__ method. The __iter__ method is to initialize the value of an iterable object. For now, we set the number to 0. It means Iter starts at 0.

# The __next__ method is to select the next element from an Object. Within this method, we used the If Else Statement to check whether the next number is greater than the maximum value or not. If True, StopIteration error raised. Otherwise, the number incremented.

class Counter:

    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        self.number=0
        return self

    def __next__(self):
        number=self.number

        if number > self.maximum:
            raise StopIteration
        else:
            self.number = number+1
            return number
numbers= Counter(10)
a=iter(numbers)
print(next(a))
print(next(a))
print(next(a))
# The above Python iterator code is displaying numbers from 0 to 2. It is because we used next(a) for three times only