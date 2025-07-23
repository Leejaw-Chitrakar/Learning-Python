#Display
print("Learning Python\n")

#String
first_name = "Leejaw"
last_name = "Chitrakar"
email = "helloguys@gmail.com"

print(first_name)
print(last_name)

#f stands for formate
print(f"Hello!! My name is {first_name} {last_name}") 
print(f"Yout email is {email}")

#Integer
age = 25
quantity = 5
num_of_students = 32

print(f"You are {age} old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} number of stundents\n")

#float
price = 10.99
gpa =3.25
distance = 14.5

print(f"Price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You travelled {distance} KM today\n")

#Boolean
#Boolean has only 2 values True or False
is_student = True
for_sale = False
is_online = True

print(f"Is he a student: {is_student}")

#Examples of if statement
if is_student:
    print("You are a student.\n")
else:
    print("You are not a student.\n")

if for_sale:
    print("That item is for sale\n")
else:
    print("That item is not available\n")

if is_online:
    print("You are Online.\n")
else:
    print("You are Offline.\n")



print("Practice starts here\n")
#Assigment (post different types of variables)

name = "Leo"
age = 18
gpa = 3.2 
is_studying = True
email = "leo.shrestha10@gmail.com"

print(f"Hello!!\nMy name is {name}, I'm {age} years old.\nI've achieved {gpa} GPA in my exam of class 12 and I'm currently studying Bsc.CSIT: {is_studying}.\nMy email is {email}")