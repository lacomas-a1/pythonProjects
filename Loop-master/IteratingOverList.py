for x in ['one','two','three','four']:
    print(x)

# enumerate will generate tuples, which are unpacked into index (an integer) and item (the actual value from the list).
# The above loop will print

for index, item in enumerate(['one','two','three','four']):
    print(index, '::', item)

# Iterate over a list with value manipulation using map and lambda, i.e. apply lambda function on each element in the
# list:
x = map(lambda e: e.upper(), ['one','two','three','four'])
print(x)