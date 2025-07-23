#Themperature Convertor

temp = float(input("Enter the Temperature: "))
unit = input("Enter the unit (C/F): ")

if unit == "C" or unit == "c" or unit == "F" or unit == "f":
    if unit == "C":
        unit = "Fahrenheit"
        temp = round((9 * temp) /5 +32, 1)
    else:
        unit = "Celsius"
        temp = round((temp - 32) * 5/9, 1)
    print(f"{temp} {unit}")
else:
    print(f"{unit} is an invalid unit of measurement!!")