Fruits = ['Apple', 'Orange', 'Banana', 'Kiwi', 'Grape', 'Blackberry']
x = [9, 4, -5, 0, 22, -1, 2, 14]

#Copying Using Copy()(Method)
New_Fruits=Fruits.copy()
print(New_Fruits)

#Removing all items Using Clear() method
New_Fruits.clear()
print(New_Fruits)

#Sorting Using Sort()Method
Fruits.sort()
x.sort()
print(Fruits)
print(x)

#Reverse using reverse() Method
Fruits.reverse()
x.reverse()
print(Fruits)
print(x)

# position of an item
print('The Index position of Banana = ', Fruits.index('Banana'))
print('The Index position of -1 = ', x.index(-1))

# Counting items using count() Method
y = [9, 4, 1, 4, 9, -1, 2, 4]
print('Number of Times 4 is repeated = ', y.count(4))
print('Number of Times 9 is repeated = ', y.count(9))