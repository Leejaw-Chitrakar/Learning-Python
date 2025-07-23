# *arge = Allows you to pass multiple non-key arguments
# **kwargs = Allows you to pass multiple keyword arguments
#            *unpacking operator
#            1. Positional, 2. Default, 3. Keyword, 4. Arbitrary

# def add(*agrs):
#     total =0
#     for arg in agrs:
#         total += arg
#     return total
# print(add(1, 2, 3)) # it is used when the arguments are not fixed

def display_name(*agrs):
    for arg in agrs:
        print(arg,end=" ")

display_name("Ram", "Shrestha")
print()
display_name("Ram", "Kumar" ,"Shrestha")
print()

def display_address(**kwargs):
    # print(type(kwargs))
    for key,value in kwargs.items():
        print(f"{key:10}: {value}")
    pass

display_address(province = "Bagmati",
                distric = "Kathmandu",
                city = "Kathmandu",
                postalcode = "44600",
                Ward_no ="12")

print()
print("Shippling Label")

def shipping_label(*agrs,**kwargs):
    for arg in agrs:
        print(arg,end=" ")
    print()

    if "house_no" in kwargs:
        print(f"{kwargs.get('city')} {kwargs.get('house_no')}")
    else:
        print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('city')} {kwargs.get('postalcode')} {kwargs.get('ward_no')}")
shipping_label("Dr.","spongebox","squrepants","III",
               province = "Bagmati",
               district="Bhaktpur",
               city="Bhaktpur",
               postalcode ="44800",
               house_no = "#106",
               ward_no="06")