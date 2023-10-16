def printvalue():
    x = 14
    y = 10

    x, y = y, x

    print('x = ' + str(x))
    print('y = ' + str(y))


if __name__ == '__main__':
    printvalue()
