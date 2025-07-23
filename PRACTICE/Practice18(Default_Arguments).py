# Default arguments = A default value for certain parameter
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduce # of arguments
#                     1. Positional ,2. Default ,3. Keyword ,4. Arbitrary

# def net_price(list_price,discount = 0, tax = 0.05):
#     return list_price * (1 -discount) * (1 + tax)
#
# #print(net_price(5000))
# Even if there is a default value it can be modified without changing it
# print(net_price(1500,0.1))

import time

def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!!")
S = int(input("Enter the starting time: "))
E = int(input("Enter the ending time: "))
count(E,S)