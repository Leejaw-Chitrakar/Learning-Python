# if = Do Some code only IF some condition is True Else do something else

print("1st Example")

age = int(input("Enter your age: "))
if age > 100:
    print("You are too old to sign up!!")
elif age >= 18:
    print("You are not signed up.")
elif age < 0:
    print("invalid input!!")
else:
    print("You must be 18  or 18+ to sign up!!")


print("\n2nd Example")

name = str(input("Enter your name:"))

if name == "":
    print("Please enter your name!!")
else:
    print(f"Hello {name}!!")

print("\n3rd Example")

respond = input("Would you line food? (Y/N):\n")

if respond == "":
    print("Invalid input!")
elif respond == "y" or respond == "Y":
    print("Have some food!")
elif respond == "n" or respond == "N":
    print("No food for you!")
else:
    print("Invalid input!!")


print("\n4th Example")

online = True

if online:
    print("This user is online!!")
else:
    print("This user is offline!!")

    