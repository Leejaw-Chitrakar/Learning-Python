#Typecasting = Its is the process of conversing a variabl form one data type to another str(), int(), float(), bool().
name = "Leo Shrestha"
age = 18
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(type(gpa))

age = str(age)
print(type(age))

name = bool(name)
print(type(name)) #here is the name is empty then its displays false

age = float(age)
print(type(age))
