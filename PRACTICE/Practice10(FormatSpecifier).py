#Format Specifiers = {value:flags} format a value based on what flags are inserted
#They can be used by combining as well

#.(number)f = round to that many decimal places (fixed point)
#:(number) = allocate that many spaces
# :010 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = centre justify
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print("\nExample of [.(number)f]\n")
print(f"Price 1 is ${price1:.1f}")
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.1f}")

print("\nExample of [:(number)]\n")
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

print("\nExample of [:010]\n")
print(f"Price 1 is ${price1:010}") # 0(zero Padded)
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

print("\nExample of [:<]\n")
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

print("\nExample of [:>]\n")
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")


print("\nExample of [:^]\n")
print(f"Price 1 is ${price1:^}")
print(f"Price 2 is ${price2:^}")
print(f"Price 3 is ${price3:^}")


print("\nExample of [:+]\n")
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

print("\nExample of [:,]\n")
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")


print("\nExample of [: ]\n")
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")


print("\nExample of [:=]\n")
print(f"Price 1 is ${price1:=}")
print(f"Price 2 is ${price2:=}")
print(f"Price 3 is ${price3:=}")