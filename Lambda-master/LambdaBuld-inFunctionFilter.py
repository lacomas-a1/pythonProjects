# We use the built-in filter function to filter the sequence of list items. First, we declared a list of numbers from 1 to 15. Next, we used the filter method with this expression. This Python lambda filter expression checks whether a number is divisible by two or not. Next, the filter method returns all the True values.

# This filters method and returns the Even Number, and Odd Numbers. Refer to the List article

number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(number)

even_num=list(filter(lambda x: x% 2==0,number))
print(even_num)

odd_num=list(filter(lambda x: x%2 !=0,number))
print(odd_num)