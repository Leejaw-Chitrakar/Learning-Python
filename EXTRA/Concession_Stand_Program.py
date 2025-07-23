# Concession Stand Program

menu = {"momo": 80,
        "chowmin":70,
        "pizza": 350,
        "samosha": 25,
        "coke": 75,
        "lays": 55,
        "hot dog": 175}
cart = []
total = 0

print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:15}: Rs.{value:.2f}") #Here key: 15 is used to align the Price

print("--------------------------")

while True:
    food = input("Select an item (q to quit): ").lower() #lower() fn is used to take all input in lower form
    if food =="q":
        break
    elif menu.get(food) is not None: #Here is not is used to display nothing if the menu does not contain the item
        cart.append(food)

print("-----------BILL-----------")
for food in cart:
    total = total + menu.get(food) #can also be written as total += menu.get(food)
    print(food,end =", ")

print()
print(f"Total is Rs.{total:.2f}")