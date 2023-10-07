def printvalue():
    name = 'akshay'
    print(name)  # akshay
    print(name[0])  # a
    print(name[5])  # y
    print(name[-1])  # y
    print(name[-6])  # a
    print(name[0:3])  # aks
    print(name[1:4])  # ksh
    print(name[3:])  # hay
    print(name[:3])  # aks
    print(name[3:10])  # hay
    print('patel ' + name[0:10])  # patel akshay
    print(len(name))  # 6

if __name__ == '__main__':
    printvalue()
