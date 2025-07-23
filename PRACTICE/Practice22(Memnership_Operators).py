# Membership Operators = Used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

# word = "apple"
#
# for char in word:
#     letter = input("Guess the letter in the secret word: ").lower()
#     if letter in word:
#         print(f"The is a {letter}")
#     else:
#         print(f"{letter} was not found")

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"The is a {letter}")

# students = {"spongebob","patric","sandy"}
#
# student = input("Enter the name of the student: ").lower()
# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found!!!")


# grades = {"sandy": "A",
#           "squidward": "B",
#           "spongebob": "C",
#           "partic": "D"}
#
# student = input("Enter the name of the student: ").lower()
#
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}.") #here student is a key to get grade
# else:
#     print(f"{student} was not found!!!")


#Email Validation
email = input("Enter your email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email!!!!")