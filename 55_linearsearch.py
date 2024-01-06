pos = -1


def search(lst, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True

        i = i + 1

    return False


lst = [5, 8, 4, 6, 9, 2]
n = 9


if search(lst, n):
    print("Value Found at ", pos+1)
else:
    print("Value Not Found")
