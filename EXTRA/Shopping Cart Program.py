#Shopping Cart

foods = []
prices = []
total = 0

while True :
    food = input("Enter a food to buy (q to quit):")
    if food == "q" or food == "Q":
        break
    else:
        price = float(input(f"Enter the Price of {food}: $ "))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end = " ")
for price in prices:
    total += price # Equivalent total = total + price

print(f"\nYour total is $ {total}")
