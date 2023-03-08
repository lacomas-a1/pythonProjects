#Symmetric Difference of A and B is a set of element in both A and B except those common in
#both.. Symmetric difference is performed using ^ operator
A= {1, 2, 3, 4, 5}
B= {4, 5, 6, 7, 8}
print(A^B)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))