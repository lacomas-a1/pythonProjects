# ext, we are adding, and multiplying three of them. If we have the default values, we do not have to pass values while calling it.

add=lambda x=10,y=20,z=30:x+y+z
print(add())

multi=lambda x=5,y=23,z=8:x*y*z
print(multi())

# Here, the first print statement overrides 10 with 12, 20 with 14 and 30 with 16. It means, x = 12, y = 14 and z = 16. In the second statement, x = 75, y = 126 and z = 30.

add = lambda x = 10, y = 20, z = 30 : x + y + z
print(add(12, 14, 16)) # 12 + 14 + 16
print(add(75, 126)) # 75 + 126 + 30
print(add(222)) # 222 + 20 + 30
print(add()) # 10 + 20 + 30


print("Multiplication Values")
multi = lambda x = 10, y = 20, z = 30 : x * y * z
print(multi(2, 4, 5)) # x = 2, y = 4, z = 5
print(multi(100, 22)) # x = 100, y = 22, z = 30
print(multi(9)) # x = 9, y = 20, z = 30
print(multi()) # 10 * 20 * 30