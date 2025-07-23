# Dictionary = A collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Nepal": "Kathmandu",
            "Russia": "Moscow"}
print(capitals)
# print(dir(capitals))
# print(help(capitals))
print(capitals.get("Nepal"))
print(capitals.get("Japan")) #if the dictionary is not present it will display none

if capitals.get("Japan"):
    print("The capital exist....")
else:
    print("The capitals doesn't exist..........")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
print(capitals)
capitals.update({"USA": "Washington D.C"})

capitals.pop("China") #To remove elements from the dictionary
print(capitals)

capitals.popitem() #Removes the latest element add to the dictionary
print(capitals)

# capitals.clear() #To remove all the elements of the dictionary
# print(capitals)

key = capitals.keys()
print(key)
#Keys can be used in a loop
for key in capitals.keys():
    print(key)

value = capitals.values()
print(value)

#Values can also be used in a loop
for value in capitals.values():
    print(value)

items = capitals.items()
print(items)
#items returns a dictionary objects which resemble a 2D list of Tuples

for key, value in capitals.items():
    print(f"{key}:{value}")