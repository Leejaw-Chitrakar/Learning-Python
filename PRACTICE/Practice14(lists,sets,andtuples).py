#Collection = single "Variable" used to store multiple values
#   List = [] ordered and changeable, Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
from traceback import print_tb

print("\nExample for list\n")
fruits = ["Apple","Orange","Banana","Mango","Pineapple"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[0:3])
print(fruits[::2])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)
#print(dir(fruits))
#use print(help(var_name)) for more information abt diff kinds of list.

print("Apple" in fruits)
print("Watermelon" in fruits)

fruits[0] = "Watermelon" # This line changes the first element of the list "fruits".
for fruit in fruits:
    print(fruit)


fruits.append("Pear") #This line add an element to the list "fruits"
print(fruits)

fruits.remove("Orange") #This line removes an element to the list "fruits"
print(fruits)

fruits.insert(1, "Guava") #This line add element as a specific position in a list.
print(fruits)

fruits.sort() #Yo line ni bujyna vhny coding xordeyou yarrr😆😆
print(fruits)

fruits.reverse()#This functions us used to display in reverse order.
print(fruits)

#To clear the list use var_name.clear() function.
# fruits.clear()
# print(fruits)

print(fruits.index("Banana"))

print(fruits.count("Banana")) #var_name.count() function is use to count the sem elements in a list.

print(len(fruits))

print("Example of Set")
fruits = {"Apple","Orange","Banana","Mango","Pineapple"}
#it shows the result in unordered form.
print(fruits)
#Here all the functions are sem as of list and same goes for tuple.