#Conditional expressions = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

print("Example 1 (Positive or negative)\n")
num = 5
print( "positive" if num > 0 else "Negative")

print("\nExample 2 odd or even\n")

num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is an {result} number.")

print("\nExample 3 maximum and minimum\n")

a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b

print(f"The maximum number is {max_num}.")
print(f"The minimum number is {min_num}.")


print("\nExample 4 Status Checker.\n")

age = 13
status = "Adult" if age >= 18 else "Child"

print(f"Your are a {status}.")


print("\nExample 5 Weather checker.\n")

temp = 30
weather = "HOT" if temp > 20 else "COLD"

print(f"The weather is {weather}")

print("\nExample 6 .\n")

user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)