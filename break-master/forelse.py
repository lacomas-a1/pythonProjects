#write a program to print the first number that is divisible by 5 for a list of numbers
nums=[12, 15, 20, 13, 17, 18,25]
for num in nums:
    if num % 5 ==0:
        print(num)
        break
else:
        print("not found")