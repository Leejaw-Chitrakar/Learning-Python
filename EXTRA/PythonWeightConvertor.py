#Python Weight Convertor

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds (K/L): ")

if unit == "K" or unit == "L":
    if unit == "K":
        weight = weight *2.205
        unit = "Lbs."
    else:
        weight = weight /2.205
        unit = "Kgs."
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} was invalid!!")