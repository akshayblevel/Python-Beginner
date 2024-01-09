'''
SELECTION SORT
STEP 1: Find the minimum value and set on 1st index
STEP 2: Find again the minimum value and set on 2nd index and so on...
'''

def sort(lst):
    for i in range(5):
        minpos = i
        for j in range(i, 6):
            if lst[j] < lst[minpos]:
                minpos = j

        temp = lst[i]
        lst[i] = lst[minpos]
        lst[minpos] = temp


lst = [5, 3, 8, 6, 7, 2]
sort(lst)

print(lst)

# OUTPUT
# [2, 3, 5, 6, 7, 8]