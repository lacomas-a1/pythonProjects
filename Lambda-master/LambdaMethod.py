x = ['apple', 'Mango Fruit', 'Banana', 'oranges', 'cherry','kiwi']
print(x)

y=sorted(x,key=lambda a:len(a))
print(y)

z=sorted(x,key=lambda a:a.casefold())
print(z)