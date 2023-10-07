def printvalue():

    # dictionary

    data = {1: 'akshay', 2: 'kumar', 4: 'patel'}
    print(data)  # {1: 'akshay', 2: 'kumar', 4: 'patel'}
    print(data[4])  # patel
    #  print(data[3]) - throws an error
    print(data.get(1))  # akshay
    print(data.get(3))  # None
    print(data.get(3, 'Not Found'))  # Not Found

    # merge two list and convert into dictionary
    keys = ['akshay', 'mansi', 'panth']
    values = ['SevUsal', 'VadaPav', 'ColdCoco']
    dic = dict(zip(keys, values))
    print(dic)  # {'akshay': 'SevUsal', 'mansi': 'VadaPav', 'panth': 'ColdCoco'}

    dic['Kush'] = 'IceCream'
    print(dic)  # {'akshay': 'SevUsal', 'mansi': 'VadaPav', 'panth': 'ColdCoco', 'Kush': 'IceCream'}

    del dic['Kush']
    print(dic)  # {'akshay': 'SevUsal', 'mansi': 'VadaPav', 'panth': 'ColdCoco'}

    # dictionary contains values, list and dictionary
    prog = {'ssp': 'Akshay', 'dup': ['Jay', 'Anjali'], 'ump': {'elder': 'Sunil', 'younger': 'Dinesh'}}
    print(prog)  # {'ssp': 'Akshay', 'dup': ['Jay', 'Anjali'], 'ump': {'elder': 'Sunil', 'younger': 'Dinesh'}}
    print(prog['ssp'])  # Akshay
    print(prog['dup'][1])  # Anjali
    print(prog['ump']['younger'])  # Dinesh


if __name__ == '__main__':
    printvalue()
