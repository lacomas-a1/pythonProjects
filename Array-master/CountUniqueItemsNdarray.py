import numpy as np

arr=np.random.randint(0,5,size=10)
print('Original=',arr)

uniq,cnt=np.unique(arr,return_counts=True)
print('Unique Items=',uniq)
print('Count Items=',cnt)

arr2=np.random.randint(10,100,size=(3,5))
print('\n--Two Dimensional random Original--\n',arr2)

uniq2, cnt2 = np.unique(arr2, return_counts = True)
print('Unique Items = ', uniq2)
print('Count Items = ', cnt2)

arr3 = np.random.randint(15, 25, size = (2, 3, 8))
print('\n----Three Dimensional Random Original ----\n', arr3)

uniq3, cnt3 = np.unique(arr3, return_counts = True)
print('Unique Items = ', uniq3)
print('Count Items = ', cnt3)

# Count the total number of times each item repeated in a Numpy array. For this, you have to use the unique function with the return_counts parameter. If we set this parameter value to True, then it counts items.