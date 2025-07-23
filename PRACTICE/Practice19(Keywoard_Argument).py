# Keyword Argument = An argument preceded by an identifier
#                    helps with readability
#                    order of argument doesn't matter
#                    1. Positional ,2. Default ,3. Keyword ,4. Arbitrary

def hello(greeting, title,fname,lname):
    print(f"{greeting} {title}{fname} {lname}")

#keyword argument follows positional arguments
hello("Hello","Mr.", "James", "Arthur")
hello("Hello", fname="Robin", title="Mr.", lname= "Hood")

