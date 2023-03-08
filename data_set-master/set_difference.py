#Difference of A and B (A - B) is a set of elements that are only in A but not in B.
#. Difference is performed using - operator.
A= {1, 2, 3, 4, 5}
B= {4, 5, 6, 7, 8}
print(A-B)
print(B-A)
print(A.difference(B))
print(B.difference(A))