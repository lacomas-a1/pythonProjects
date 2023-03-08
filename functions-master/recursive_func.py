#recursive function to find the factorial of an integer
#Factorial of a number is the product of all the integers from 1 to that number
def recur_fact(x):
    if x==1:
        return 1
    else:
        return (x * recur_fact(x-1))
num = int(input("Enter a number: "))
if num >=1:
    print("The factorial of", num, "is", recur_fact(num))