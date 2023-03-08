class Counter:

    def __iter__(self):
        self.num=0
        return self

    def __next__(self):
        num = self.num

        self.num = num +1
        return num

for t in Counter():
    print(t)