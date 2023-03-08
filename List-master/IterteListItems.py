# A For Loop is the most common way to traverse the list items and it helps to iterate and print the items. This code works accurately to print items inside it. However, to alter the individual element, we need the index position.

Fruits = ['Apple', 'Orange', 'Grape', 'Banana']
for Fruit in Fruits:
    print(Fruit)


# It multiplies each item with 10. If we want to perform the calculation based on condition, then use If Statement inside the for loop.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for Number in range(len(x)):
    x[Number] = x[Number] * 10
print(x)

# Iterate Items

Fruits = ['apple', 'Mango', 'banana', 'orange', 'cherry','kiwi']

# Iterate Elements
for fruit in Fruits:
    print(fruit)

# Iterate Items using Index 
for i in range(len(Fruits)):
    print("Item at ", i, " = ", Fruits[i])