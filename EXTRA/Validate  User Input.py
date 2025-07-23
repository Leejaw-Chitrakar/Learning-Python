# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")
no_space = username.find(" ")
no_digit = username.isalpha()

if len(username) > 12:
    print("Your username can't be more than 12 characters!!")
elif not no_space == -1:
    print("Your username can't contain any spaces!!")
elif not no_digit == True:
    print("Your username can't contain any digits!!")
else:
    print(f"Welcome {username}")