numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) #declearing a tuple
num=sum = 0
count = 0
for x in numbers:
    num_sum = num_sum + x
    count = count + 1
    if count == 5:
        break
print("sum of first ", count, "interger is: ", num_sum)