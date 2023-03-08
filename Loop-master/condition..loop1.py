#Loop with condition in the middle
# Take input from the user untill a vowel is entered

vowels = "aeiouAEIOU"
#infinite loop
while True:
    v =input("Enter a vowel: ")
    # condition in the middle
    if v in vowels:
        break
    print("Thats is not a vowel.Try again!")
print("Thank You!")
