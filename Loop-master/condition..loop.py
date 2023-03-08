#program to illustrate a loop with a while at the top
n = int(input("Enter a number: "))
sum = 0 #intialize sum and counter
i = 1
while i <= n:
    sum =sum + i
    i +=1 # update counter
print("The sum is: ", sum)