#Logical Operators = evaluate Multiple condition (or, and, not)
# or = at least one condition must be True
# and  both the condition must be True
# not = inverts the condition (not False, not True)


print("Example for or condition.\n")
temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor even is still scheduled")


print("\nExample for and condition.\n")

temp = 30
is_sunny = True

if temp >=28 and is_sunny:
    print("It is hot outside 🥵")
    print("It is SUNNY ☀")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀")
elif temp < 28 and temp > 0 and is_sunny: # we can also writ it like [28 > temp > 0 and is_sunny]
    print("It is WARM outside 😐")
    print("It is SUNNY ☀")


print("\nExample for not condition\n")

temp = 25
is_sunny = False

if temp >= 28 and not is_sunny:
    print("It is hot outside 🥵")
    print("It is CLOUDY ☁")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ☁")
elif temp < 28 and temp > 0 and not is_sunny: # we can also writ it like [28 > temp > 0 and not is_sunny]
    print("It is WARM outside 😐")
    print("It is CLOUDY ☁")