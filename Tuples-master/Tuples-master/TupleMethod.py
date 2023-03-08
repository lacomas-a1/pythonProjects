# The tuple() method helps to convert the String or Lists into Tuple.

# The min function helps us to find the Smallest or minimum item and the max function finds the Largest item or largest item.
# The Len method finds or calculates the Length or Number of items and the sorted method helps to sort the elements in ascending order. The index function returns the index position of a specified value.

# The sum function calculates the sum of all items inside the given one. And the count function counts the total number of times the specified value repeated.

FruitsTP=('Apple', 'Orange', 'Banana', 'Kiwi', 'Grape', 'Blackberry')
tp=(9,4,-5,0,22,-1,2,14)

#Finding Sum of all item in a  using Sum() Method
print('Sum of all items in a tp=',sum(tp))

#Calculating Length of a  using len() Method
print('Lenght of a FruitsTP=',len(FruitsTP))
print('Length of a tp=',len(tp))

#Finding Minimum item in a  using min() Method
print('Minimum items in a FruitsTP=',min(FruitsTP))
print('Minimum item in a tp=',min(tp))

#Finding Maximum item in a  using max() Method
print('Maximum item in a FruitsTP  = ', max(FruitsTP))
print('Maximum item in a tp  = ', max(tp))

# Using Sorted() Method
print('After Sorting FruitsTP=',sorted(FruitsTP))
print('After Sorting tp=',sorted(tp))

# Index position of an item in a  using index() Method
# print('The Index position of Banana=',FruitsTP('Banana'))
print('The Index position of -1=',tp.index(-1))

# Counting items in a  using count() Method
tp2=(9,4,1,4,9,-1,2,4)
print('Number of Times 4 is repeated=', tp2.count(4))
print('Number of Times 9 is repeatd =', tp2.count(9))

# Converting List?
tp3=[1,2,3,4,5]
print(tuple(tp3))