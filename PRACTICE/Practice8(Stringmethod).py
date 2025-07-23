#Srting Method

# name = str(input("Enter your name: "))
# name = "leejawchitrakar"
#         012345678901234 (indicator for simplicity)
name = str(input("Enter your name: "))
result = len(name)  #len() function is use to find the length of a variable.
print(result)

result = name.find("c")  #variable_name.find() functions is use to find specific values in the variable.
print(result)  #here it shows 7 cuz initially it counts from 0.

result = name.rfind("a")  #variable_name.rfind() functions is use to find specific values in the variable in reverse.
print(result)  #here it 7 shows  cuz initially it counts from 0.

result = name.find("q")
print(result)  #If there aren't any specific to find then it will return -1.

name = name.capitalize()
print(name)  #Just first letter is capitalized.

name = name.upper()
print(name)  #All the latter are uppercased / user variable_name.lower() for lowercase.

name = name.isdigit()
print(name)  #checks weather variable has digits or not. It shows True only when the variable contains digits only.

name = name.isalpha()
print(name)


print("\nExample 1\n")
phone_number = input("Enter your phone #: ")

result = phone_number.count("-")
print(result) #variable_name.count() function is use to count specific values in a variable.

phone_number = phone_number.replace("-"," ")
print(phone_number)


#print(help(str)) shows list of diff string methods