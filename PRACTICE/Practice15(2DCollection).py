# 2D collection  = A collection is the list of lists.
# Array = Arrays are the list of similar elements.
# Example ---> Food = [Food_type_1, Food_type_2, Food_type_3,]
from msvcrt import get_osfhandle

fruits = ["Apple", "Orange", "Banana", "Coconut"]
vegetables = ["Celery", "Carrots", "Potatoes", "Tomato"]
meats = ["Chicken", "Fish", "Turkey", "Steak"]

groceries = [fruits, vegetables, meats]

print(groceries[0][0])
print(groceries[2][3])           #Here all the elements are stored in a matrix form.
print(groceries[1][2])           #To display the elements of 2d lists you have to use 2 Arrays like [0][0].

print("\nList of food in matrix form.")
for collection in groceries:
    print(collection)


print("\nList of foods in vertical form.")
for collection in groceries:
    for food in collection:
        print(food)
