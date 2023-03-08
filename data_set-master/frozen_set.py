#Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed
#once assigned
A= frozenset([1, 2, 3, 4, 5])
B= frozenset([4, 5, 6, 7, 8])
print(A.isdisjoint(B))
print(A.difference(B))
print(A|B)
print(A.add(3))