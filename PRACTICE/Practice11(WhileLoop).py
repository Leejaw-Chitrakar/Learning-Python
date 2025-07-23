# #While Loop = execute some code WHILE some condition remains True

print("\nExample 1 Name\n")

name = input("Enter your name: ")

while name == "":
    print("You did not entered your name!!")
    name = input("Enter your name: ") #This line helps user to escape the loop.
else:
    print(f"Hello {name}")


print("\nExample 2 Age\n")
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be 0 or below!!")
    age = input("Enter your age: ")
else:
    print(f"You're {age} years old.")

print("\nExample 3 Food\n")

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")
else:
    print("Bye")

print("\nExample 4 \n")

num = int(input("Enter a number between 1 to 10: "))

while num < 1 or num >10:
    print(f"{num} is not valid!!")
    num = int(input("Enter a number between 1 to 10: "))
else:
    print(f"Your number is {num}")