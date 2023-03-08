lst=['alpha','bravo','charlie','delta','echo']
# Iteration over the whole list
# To iterate over each element in the list, a for loop like below can be used:
for s in lst:
    print (s[:1])

# Often you need both the element and the index of that element. The enumerate keyword performs that task.
for idx, s in enumerate(lst):
    print("%s has an index of %d" %(s, idx))


# Iterate over sub-list:
for i in range(2,4):
    print("lst at %d contains %s" %(i,lst[i]))

# The list may also be sliced. The following slice notation goes from element at index 1 to the end with a step of 2.
# The two for loops give the same result.
for s in lst[1::2]:
    print(s)
for i in range(1, len(lst), 2):
    print(lst[i])