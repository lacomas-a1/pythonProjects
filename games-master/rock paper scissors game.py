import random
win=0
while True:
    my_choice =input("Enter a choice(rock,paper,scissors) type 'Exit' to stop: ")
    game_choices =["rock","paper","scissors"]
    computer_choice = random.choice(game_choices)
    if my_choice == computer_choice:
        print(f"Both players selected{my_choice}.It's a Tie!")

    elif my_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors ! You win!")
            win += 1
        else:
            print("paper covers rock! You lose!")
    elif my_choice=="paper":
        if computer_choice == "rock":
            print("paper covers rock! You win!")
            win += 1
        else:
            print("scissors cuts paper! You lose!")
    elif my_choice=="scissors":
        if computer_choice == "paper":
            print("scissors cuts paper! You win!")
            win += 1
        else:
            print("rock smashes scissors! You lose!")
    elif my_choice == "Exit":
        print("You won", win ,"times")
        break
    else:
        print("invalid input")



