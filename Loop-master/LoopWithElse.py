# Iterate over a list with value manipulation using map and lambda, i.e. apply lambda function on each element in the
# list:

for i in range(3):
    print(i)
else:
    print('done')

i=0
while i<3:
    print(i)
    i+=1
else:
    print('done')

# The else clause does not execute if the loop terminates some other way (through a break statement or by raising
# an exception):
for i in range(2):
    print(i)
    if i==1:
        break
else:
    print('done')


# The main use case for the for...else construct is a concise implementation of search as for instance
a=[1,2,3,4]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print('no exception')

# To make the else in this construct less confusing one can think of it as "if not break" or "if not found".