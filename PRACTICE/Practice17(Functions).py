# #function = A block of reusable code place () after the function name to invoke it
#
# def hbd(name,age):
#     # position of parameters is important
#     print(f"Happy birthday, {name}!!!")
#     print(f"You're {age} years old!!!")
#     print()
#
# hbd("Shyam",12)
# hbd("Ram",15)
# hbd("Rita",20)
#
# def display_invoice(username, amount, due_date):
#     print(f"Hello {username},")
#     print(f"Your bill of Rs.{amount:.2f} is due: {due_date}")
#
#
# display_invoice("Rohan",5045,"05/01")
# print()
#
# #Return = It is a statement used ti end a function
# #         and send a result back to the caller
#
#
# def add(a,b):
#     res = a+b
#     return res
#
# def sub(a,b):
#     res = a-b
#     return res
#
# def mul(a,b):
#     res = a*b
#     return res
#
# def div(a,b):
#     res = a/b
#     return res
#
# print(f"Addition is {add(1,2)}")
# print(f"Subtraction is {sub(1,2)}")
# print(f"Multiplication is {mul(1,2)}")
# print(f"Division is {div(1,2)}")


def create_name(f_name,l_name):
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()
    return f_name + " " + l_name

full_name = create_name("leejaw","chitrakar")

print(full_name)