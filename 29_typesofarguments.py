
def addition(x, y):     # formal arguments
    z = x + y
    print(z)


addition(14, 10)  # actual arguments (Position, Keyword, Default, Variable Length)


def employee(name, age=18):
    print(name)
    print(age)


# Position
employee('Akshay', 42)  # maintain position that is first name and then age

# Keyword
employee(age=42, name='Akshay')

# Default
employee('Akshay')
employee('Akshay', 28)


# Variable Length
def add(x, *y):     # * means multiple arguments
    z = x
    for i in y:
        z = z + i
    print(z)  # 124


add(14, 10, 19, 81)


def person(name, **data):   # ** means multiple arguments with arguments
    print(name)
    for i, j in data.items():
        print(i, j)


person('Akshay', age=42, city='Hyderabad', mob=9898989898)
# Akshay
# age 42
# city Hyderabad
# mob 9898989898
