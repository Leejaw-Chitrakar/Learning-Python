#For Loops = executes a block of code for a fixed number of times.
#            you can iterate ove a range, strange, sequences, etc.

print("\nExample 1 Display from 1 to 10\n")
for x in range(1, 11): #Begin at 1 and stop when we reach 11 [Note: 11 will not be displayed]
    print(x)

print("\nExample 2 display Backward\n")
for x in reversed(range(1, 11)):
    print(x)

for x in range(1, 11, 2): #Here it displays ever 2nd number[Note: initially 0 is first.]
    print(x)
#1 2 3 4 5 6 7 8 9 10
#0 1 2 3 4 5 6 7 8 9  (indicator for simplicity)

print("\nExample 3 display Card number\n")

credit_card = "1234_5678_9012-3456"

for x in credit_card:
    print(x)


print("\nExample 4 Count from 1 to 50 but skip the number 13 and stop at 45\n")

for x in range(1, 51): #This lines displays till 50 from 1
    if x == 13: # This line skips the number 13
        continue #This line continues the count
    elif x == 46: #This line stopes the count and display till 45
        break
    print(x)
