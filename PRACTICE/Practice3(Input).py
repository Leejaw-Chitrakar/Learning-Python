#input() = A functions that prompts the user to enter data and Returns the enteres data as a string.

name = input("What is your name?")
age = input("How old are you?") #also age = int(input("How old are you?")) this works

age = int(age) #Converted in to int so we can use arthamatics
age = age + 1

print(f"Hello {name}!")
print("Happy Birthday")
print(f"You are {age} years old!\n")


print("Practice 1\n")
#Calculate the area of rectangel
l = float(input("length = "))
b = float(input("Breadth = "))
area = l * b
print(f"Area of rectangle is {area} sq units.\n")


print("Practice 2\n")

item = input("Whta item would you like to buy?\n")
price = float(input("How much is the item?\n"))
quantity = int(input("How many would you like to buy?\n"))
total = price * quantity
print(f"Total cost of {quantity} {item} is Rs.{total}")