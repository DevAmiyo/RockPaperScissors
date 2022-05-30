import random

computer_score, player_score = 0, 0

while True:
    choices = ["Rock","Paper","Scissors"]

    computer_choice = random.choice(choices)
    player_choice = None

    while player_choice not in choices:
        player_choice = input("Rock, Paper, or Scissors?: ").lower().capitalize()

    if player_choice == computer_choice:
        print("Computer: ",computer_choice)
        print("Player: ",player_choice)
        print("Its a Tie!\n")
        computer_score += 1
        player_score += 1

    elif player_choice == "Rock":
        if computer_choice == "Paper":
            print("Computer: ", computer_choice)
            print("Player: ", player_choice)
            print("You lose!\n")
            computer_score += 1
        if computer_choice == "Scissors":
            print("Computer: ", computer_choice)
            print("Player: ", player_choice)
            print("You win!\n")
            player_score += 1

    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            print("Computer: ", computer_choice)
            print("Player: ", player_choice)
            print("You lose!\n")
            computer_score += 1
        if computer_choice == "Paper":
            print("Computer: ", computer_choice)
            print("Player: ", player_choice)
            print("You win!\n")
            player_score += 1

    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            print("Computer: ", computer_choice)
            print("Player: ", player_choice)
            print("You lose!\n")
            computer_score += 1
        if computer_choice == "Rock":
            print("Computer: ", computer_choice)
            print("Player: ", player_choice)
            print("You win!\n")
            player_score += 1

    if computer_score == 10 or player_score == 10:
        break

print("="*32)
print("{:^32}".format("S C O R E S"))
print("="*32)
print("Computer: ", computer_score)
print("Player: ", player_score)
if player_score == 10:
    print("Congratulations! You win!!")
elif player_score == computer_score:
    print("Wohoo!! It\'s a tie. Good game!")
else:
    print("Uh oh! You lost the game. Try again!")
