#Nested Loop = A Loop within another loop (other, inner)
#              outer loop:
#                  inner loop:

print("\nExample Display from 1 to 10 in 3 rows.\n")

for x in range(3):
    for y in range(1, 11):
        print(y, end=" ")  # end function is user to display the numbers in single line
    print()


print("\nExample Display a rectangle.\n")

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")  # end function is user to display the numbers in single line
    print()