collection =[('a','b','c'),('x','y','z'),('1','2','3')]
for item in collection:
    i1=item[0]
    i2=item[1]
    i3=item[2]
print(item)

# or something like this:
for item in collection:
    i1,i2,i3 = item
print(item)