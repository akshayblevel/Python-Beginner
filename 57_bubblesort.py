'''
Bubble Sort
STEP 1: Compare first value with second value
        if second value is smaller than first value
        then swap the value
        Do it till end of list
STEP 2: Iterate step 1
'''


def sort(lst):
    for i in range(len(lst)-1, 0, -1):  # start with last index till 0
        for j in range(i):              # set range till last index
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp


lst = [5, 3, 8, 6, 7, 2]
sort(lst)

print(lst)

# OUTPUT
# [2, 3, 5, 6, 7, 8]
