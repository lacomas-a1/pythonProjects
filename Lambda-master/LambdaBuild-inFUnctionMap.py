# Unlike filter, map function takes each list item and returns both the True and False values. In this Python lambda map example, we used map method to return the boolean value. It checks each individual value is divisible by 2 equals to 0. If true, it returns True. Otherwise, it returns false.
number=[1,2,3,4,5,6,7,8,9,10]
print(number)

new_num=list(map(lambda x: x%2==0,number))
print(new_num)

# This time, we are performing multiplication using this Python lambda map function. It takes one individual list item at a time and performs the multiplication
number=[1,2,3,4,5,6,7,8,9,10]
print(number)

double_num=list(map(lambda x: x*2,number))
print(double_num)

square_num=list(map(lambda x: x**2,number))
print(square_num)

# By using the map function, you can also perform calculations on multiple lists. For instance, this example performs addition, subtraction, and multiplication of two lists. It takes one value from both the list in the same position and performs the calculation.
num1=[10,20,30]
num2=[15,25,35]
print(num1)
print(num2)
print()

mul_num =list(map(lambda X,Y: X*Y,num1,num2))
print(mul_num)