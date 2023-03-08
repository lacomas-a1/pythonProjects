# the Python next() method returns one item at a time. So, for n number of items, you have to use n next() statements. Here, we used the next() for one time. So, it returns the first character from a string.

String='tutorialgateway'
for x in String:
    print(x,end='')

print("\n***Output***")
itr=iter(String)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
