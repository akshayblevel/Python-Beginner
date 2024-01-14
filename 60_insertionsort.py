'''
INSERTION SORT

5           3   8   6   7   2
sorted      Unsorted

5   3       8   6   7   2
sorted      Unsorted
Iterate till value to the immediate left is lower than the value to sort
If immediate left value is higher than change the position

Pick 8 in another iteration and follow above steps
'''


def sort(lst):
    for i in range(1, len(lst)):
        value_to_sort = lst[i]
        while lst[i-1] > value_to_sort and i > 0:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i = i - 1

    return lst


lst = [5, 3, 8, 6, 7, 2]
sort(lst)

print(lst)

# OUTPUT
# [2, 3, 5, 6, 7, 8]
