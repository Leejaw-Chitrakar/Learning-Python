friends = 8
friends = friends + 1 #friends +=1
print(friends)

friends = friends - 2 #friends -=2
print(friends)

friends = friends * 4 #friends *=4
print(friends)

friends = friends / 2 #friends /=2
print(friends)

friends = friends ** 2 #friends **=2
print(friends)

friends = friends % 4 #friends %=4
print(friends)



print("\nPractice")
x = 3.14
y = -4
z = 5
resultx = round(x)
print(resultx)
resulty = abs(y)
print(resulty)
result =pow(4,3)
print(result)
result = max(x, y, z)
print(result)
result = min(x, y, z)
print(result)


print("\nPractic 2")

import math

x = 9.6

print(math.pi)
print(math.e)
result = math.sqrt(x)
print(result)
result = math.ceil(x)
print(result)
result = math.floor(x)
print(result)


print("\nPractic 3")
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius 
print(f"The circumference of the circle is {round(circumference, 2)}cm")



print("\nPractice 4")

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * pow(radius,2)

print(f"Area of the circle is {round(area,2)} cmsqr")


print("\nPractice 5")

import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side c = {c}")