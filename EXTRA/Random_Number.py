import random

low = 1
high = 100
options = ("rock","paper","scissors")
cards = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]

# number = random.randint(low, high)
# print(number)

# option = random.choice(options)
# print(option)

random.shuffle(cards)
print(cards)