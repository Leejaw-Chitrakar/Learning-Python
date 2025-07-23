# Indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"
#                0123456789012345678 (indicator for simplicity)

print(credit_number[3])
print(credit_number[:4]) #If you want from the start you don't have to mention the start.
print(credit_number[4:9])
print(credit_number[5:]) #If you want till the end you don't have to mention the end.
print(credit_number[-1]) #Negative index is user to count from behind.
print(credit_number[::3]) #It will count every 3rd character starting with 1[It's index is 0 remember].

print("\nPractice 1\n")
print("Display Last 4 digit of the credit card")

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")


print("\nPractice 2\n")
print("Reverse the number")

credit_number = credit_number[::-1]
print(credit_number)