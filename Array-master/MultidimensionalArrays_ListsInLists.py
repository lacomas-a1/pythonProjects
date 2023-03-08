# A good way to visualize a 2d array is as a list of lists. Something like this:
lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst[0])
print(lst[1])
print(lst[2])

# You can then access the different elements in each of those lists the same way:
print(lst[0][0])
print(lst[0][1])

# You can also set values inside these lists the same way:
lst[0]=[10,11,12]
print(lst[0])

# Now the list is [[10,11,12],[4,5,6],[7,8,9]]. In this example we changed the whole first list to be a completely
# new list.
lst[1][2]=15
print(lst)