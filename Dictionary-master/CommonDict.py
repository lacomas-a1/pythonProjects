da={1:10,2:20,3:30,4:40,5:50}
print(da)

length=len(da)
print("Length:", length)
print()

db={'name':'kelvin','age':24}
print(db)
print("\nlenght:",len(db))

total=sum(da.values())
print("\nSum:",total)

key_total=sum(da.keys())
print("\nSum:",key_total)

min_value=min(da.values())
print("\nMinimum:",min_value)

min_key=min(da.keys())
print("\nMin Key:",min_key)

max_value=max(da.values())
print("\nMaximum:",max_value)

max_key=max(da.keys())
print("\nMax Key:",max_key)