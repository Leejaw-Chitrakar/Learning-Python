import random

option = ("rock","paper","scissor")

playing =True
while playing:
    player = None
    computer = random.choice(option)
    while player not in option:
        player = input("Enter a choice(rock,paper,scissor): ").lower()
        if player not in option:
            print("Invalid input!!!")
        else:
            print(f"Player: {player}")
            print(f"Computer: {computer}")
            if player == computer:
                print("It's a tie!!")
            elif player == "rock" and computer == "scissor":
                print("You win!!!")
            elif player == "paper" and computer == "rock":
                print("You win!!!")
            elif player == "scissor" and computer == "paper":
                print("You win!!!")
            else:
                print("you lose!!")
            if not input("play again? (y/n): ").lower() == "y":
                playing = False

print("Thank you for playing.")