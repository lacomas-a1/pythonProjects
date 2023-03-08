# While you create your own iter, you should always be careful with Infinity loops. If you forget to raise the error, then you end up in infinity loops. It is a simple example of an infinity iterator. It is the same as above, but we removed the If statement.

class Counter:

    def __iter__(self):
        self.number=0
        return self

    def __next__(self):
        number =self.number

        self.number=number + 1
        return number

numbers=Counter()
a=iter(numbers)

print(next(a))
print(next(a))
print(next(a))

# Although the above example is an infinite iter, you might not have noticed it. It is because we used the next() for three times only