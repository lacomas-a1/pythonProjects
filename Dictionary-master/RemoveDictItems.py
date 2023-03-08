db={1:'apple',2:'Orange',3:'Kiwi',4:'Banana'}

# Remove using pop()
print("Removed: ",db.pop(3))
print("Remain: ", db)

# Remove using popitem()
print("\nRemoved: ",db.popitem())
print("Remain: ",db)

#popitems removes the last item in the list:

#Using del
del db[2]
print(db)

# remove using clear
db.clear()
print(db)

#Deleting all items
del db
print(db)