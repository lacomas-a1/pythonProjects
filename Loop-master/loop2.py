#program the add natural numbers ...upto n where n is provided by the user
n = int(input("Enter n:"))
sum = 0
i = 1
while i <= n:
    sum =sum + i
    i = i+1         #update counter
print("The sum is: ",sum)