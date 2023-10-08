def printvalue():
    num = 5677  # variable with value
    id(num)  # get memory address of variable
    print(id(num))

    name = 'akshay'
    id(name)
    print(id(name))

    # declare two variables, assign value of one into another, check memory address
    a = 1410
    b = a
    print(id(a))
    print(id(b))
    # both variables memory address is same

    # declare one more variable with value 1410, check memory address
    c = 1410
    print(id(c))
    # memory address is same as a and b that means memory address is assigned to value and not the variable


if __name__ == '__main__':
    printvalue()
