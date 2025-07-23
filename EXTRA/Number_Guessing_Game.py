import random

low = 1
high = 100
guess = 5
num = random.randint( low, high)
print("---------------------------")
print("Python Number Guessing Game")
print("---------------------------")
print(f"Guess the number from {low} to {high}")
print(f"You have {guess+1} guesses")
# print(num) #uncomment it to test the code
while True:
    number = input("Guess the number: ")
    if number.isdigit():
        number = int(number)
        if number < low or number > high:
            print("That number is out of range!!!")
            print(f"Enter the number between {low} to {high}!!!")
        elif number < num:
            if guess == 0:
                print(f"Guess = {guess}")
                print(f"you failed to guess, The number was {num}")
                break
            else:
                print("Too low Try again")
                print(f"Guess = {guess}")
                guess -= 1
        elif number > num:
            if guess == 0:
                print(f"Guess = {guess}")
                print(f"you failed to guess, The number was {num}")
                break
            else:
                print("Too high Try again")
                print(f"Guess= {guess}")
                guess -= 1
        else:
            print(f"You guessed the number!!! it was {num}")
            break
    else:
        print(f"Enter a valid number between {low} to {high}!!!")