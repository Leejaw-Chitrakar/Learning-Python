#Python Calculator

operator = str(input("Enter an operator (+ - * /): "))
if operator == "+" or operator == "-" or operator == "*" or operator == "/": 
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    if operator == "+" :
        result = round(num1 + num2, 2)
    elif operator == "-":
        result = round(num1 - num2, 2)
    elif operator == "*":
        result = round(num1* num2, 2)
    else:
        result = round(num1 / num2, 2)
else:
    print(f"{operator} is not valid operator!!")
    result = f"not be determined due to invalid operator [ {operator} ] !!"

print(f"Your answer is {result}.")
