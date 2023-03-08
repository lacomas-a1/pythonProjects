#Loop with condition at the bottom

# Roll a dice untill user chooses to exit
# import random module
import random
while True:
    input("Press enter to roll the dice")
    # get a number between 1 to 6
    num = random.randint(1,6)
    print("You got", num)
    option = input("Roll again?(y/n)")
    #condition
    if option == "n":
        break
