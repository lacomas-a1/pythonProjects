# break and continue only operate on a single level of loop. The following example will only break out of the inner
# for loop, not the outer while loop:
while True:
    for i in range(1, 5):
        if i==2:
            break
        print(i)