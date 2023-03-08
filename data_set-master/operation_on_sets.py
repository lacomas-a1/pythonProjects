#with other sets
#intersection
a={1, 2, 3, 4, 5}
b={3, 4, 5, 6}
print(a.intersection(b))
print(a & b)
print(a.union(b))
print(a|b)
print(a.difference(b))
print(a-b)
print(a.symmetric_difference(b))
print(a ^ b)
print(a.issuperset(b))
print(a >= b) #superset check
print(a.issubset(b))
print(a <= b)   #subset check
print(a.isdisjoint(b))  #disjoint check

#with single elements
#Existence check
print( 2 in {1, 2, 3})
print (4 not in {1, 2, 3})
print( 4 in {1, 2, 3})

#Add and Remove
s={1, 2, 3}
s.add(4)
s.discard(3)
s.discard(5)
s.remove(2)
s.update({3, 4})
print (s)
