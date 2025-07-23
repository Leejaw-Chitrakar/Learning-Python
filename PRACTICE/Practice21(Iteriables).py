# Iterables = An object/collection that can return its element one at a time,
#             allowing it to be iterated over a loop

#tulpes are also iterables

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

print()

for num in reversed(numbers):
    print(num)

print()

for num in numbers:
    print(num,end=" ")

print()

fruits = {"apple","mango","orange","banana","coconut"}
#Sets can't be reversed
for fruit in fruits:
    print(fruit,end=" ")

print()

name = "Ram Kumar Shrestha"

for char in name:
    print(char,end=" ")

print()

my_dictionary = {"A": 1,"B": 2,"C": 3}

for key,value in my_dictionary.items():
    print(f"{key}: {value}")