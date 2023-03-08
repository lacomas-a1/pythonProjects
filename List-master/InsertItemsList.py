# # 
# The available built in functions to insert new items into the existing one.

# Append(x): Adds item x at the end.
# Insert(i, x): it inserts the specified item x at position i.
# Extend(New_List): Adds all the elements in New_List at the end.

Fruits=['Apple', 'Orange', 'Grape', 'Banana']

# Adding items using append
Fruits.append('Blackberry')
print(Fruits)

# Inserting items using insert
Fruits.insert(2,'Kiwi')
print(Fruits)

# Extendingg using extend
Fruit_new=['berry','cherry']
Fruits.extend(Fruit_new)
print(Fruits)