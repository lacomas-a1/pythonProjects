number=[10,20,30,40,50]
itr=iter(number)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())

#  we used the __next__() special method. If you observe the last statement, we are trying to return the next element that doesn’t exist. That’s why Iter is calling StopIteration. we used the __next__() special method. If you observe the last statement, we are trying to return the next element that doesn’t exist. That’s why Iter is calling StopIteration.