print("create an acount")
username=input("Enter your name:")
password=input("Enter your password:")
print("Account Created Successful")
print("Log in Now")
username2=input("Enter your name:")
password2=input("Enter your password:")
if username==username2 and password==password2:
    print("Log in Successful")
else:
    print("invalid credentials")