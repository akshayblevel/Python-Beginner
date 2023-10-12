def printvalue():
    #  numeric - int | float | complex | bool

    num = 1410
    print(type(num))  # <class 'int'>

    num = 14.10
    print(type(num))  # <class 'float'>

    num = 6 + 9j
    print(type(num))  # <class 'complex'>

    # convert float to int
    num = 14.10
    print(int(num))  # 14

    # convert int to float
    num = 14
    print(float(num))  # 14.0

    # convert int values to complex
    num = 14
    num1 = 10
    print(complex(num, num1))  # (14+10j)

    result = num > num1
    print(type(result))  # <class 'bool'>

    # convert bool to int means True should be 1 and False should be 0
    print(int(True))  # 1
    print(int(False))  # 0

    s = {10, 20, 30, 40, 50}
    print(type(s))  # <class 'set'>

    print(range(10))  # range(0, 10)
    print(type(range(10)))  # <class 'range'>
    print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(range(2, 10, 2)))  # [2, 4, 6, 8]


if __name__ == '__main__':
    printvalue()
