# We can access the Python Tuple items using indexes. 
#  Index value starts at 0 and ends at n-1, where n is the size. Using the Negative numbers as an index, it starts looking for elements from right to left.
#  if a class store 5 elements, then the index starts at 0 and ends with 4. To access the first value, use TupleName[0] and to access the fifth value, use TupleName[4]. 

x=(1,2,3,4,5,6,7,8,9)
#Positive Indexing
print(x[0])
print(x[4])
print(x[8])
print('====================\n')

#NEgative Indexing
print(x[-2])
print(x[-4])
print(x[-8])
print('====================\n')

MixedTuple=((1,2,3),[4,5,6],'Learn')
print(MixedTuple[0][0])
print(MixedTuple[1][0])
print(MixedTuple[2][0])
print(MixedTuple[2][4])