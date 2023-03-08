from datetime import datetime
a=datetime(2016, 10, 6, 0, 0, 0)
b=datetime(2016, 10, 1, 23, 59, 59)
print(a-b) #datetime.timedelta(4,1)
print((a-b).days) #4
print((a-b).total_seconds())