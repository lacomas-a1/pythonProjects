d={'a':1,'b':2,'c':3}

for key in d:
    print(key)

for key in d:
    print(d[key])

for key in d:
    print(key,d[key])

print([key for key in d])

for key,value in d.values():
    print(key,value)

for i,j in d.items():
    print(i,j)