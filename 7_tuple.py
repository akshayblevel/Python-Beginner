def printvalue():

    # tuple
    tup = (10, 20, 30, 40, 50, 60)
    print(tup)  # (10, 20, 30, 40, 50, 60)
    print(tup[1])  # 20
    # tup[1] = 25  # tuple value can not be changed

    # set - unique values | index not supported
    s = {10, 20, 30, 30, 20, 10}
    print(s)  # {10, 20, 30}
    s.add(40)
    print(s)  # {40, 10, 20, 30}


if __name__ == '__main__':
    printvalue()
