def printvalue():
    nums = [10, 20, 30, 40, 50, 60]
    print(nums)  # [10, 20, 30, 40, 50, 60]
    print(nums[0])  # 10
    print(nums[5])  # 60
    print(nums[-1])  # 60
    print(nums[-6])  # 10
    print(nums[0:3])  # [10, 20, 30]
    print(nums[1:4])  # [20, 30, 40]
    print(nums[3:])  # [40, 50, 60]
    print(nums[:3])  # [10, 20, 30]
    print(nums[3:10])  # [40, 50, 60]
    print(len(nums))   # 6

    names = ['akshay', 'kumar', 'satish', 'chandra', 'patel']
    print(names)  # ['akshay', 'kumar', 'satish', 'chandra', 'patel']

    values = [56.77, 'akshay', 5677]
    print(values)  # [56.77, 'akshay', 5677]

    listoflist = [nums, names]
    print(listoflist)  # [[10, 20, 30, 40, 50, 60], ['akshay', 'kumar', 'satish', 'chandra', 'patel']]

    nums.append(70)
    print(nums)  # [10, 20, 30, 40, 50, 60, 70]

    nums.insert(2, 25)
    print(nums)  # [10, 20, 25, 30, 40, 50, 60, 70]

    nums.remove(25)
    print(nums)  # [10, 20, 30, 40, 50, 60, 70]

    nums.pop(2)
    print(nums)  # [10, 20, 40, 50, 60, 70]

    nums.pop()
    print(nums)  # [10, 20, 40, 50, 60]

    del nums[2:]
    print(nums)  # [10, 20]

    nums.extend([30, 40, 50,  60])
    print(nums)  # [10, 20, 30, 40, 50, 60]

    print(min(nums))  # 100
    print(max(nums))  # 60
    print(sum(nums))  # 210

    nums.sort()
    print(nums)  # [10, 20, 30, 40, 50, 60]


if __name__ == '__main__':
    printvalue()
