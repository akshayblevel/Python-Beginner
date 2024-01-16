'''
MERGE SORT

                                    5   3   8   6   7   2
                        5   3   8                               6   7   2               # divide into sub arrays
                    5           3   8                       6           7   2
                    5       3           8                   6       7           2
                    5               3   8                   6           2   7           # sort and merge back
                        3   5   8                               2   6   7
                                    2   3   5   6   7   8

'''


def sort(lst):
    if len(lst) > 1:

        center = len(lst) // 2
        left = lst[:center]
        right = lst[center:]

        # Sort the two halves
        sort(left)
        sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

    return lst


lst = [5, 3, 8, 6, 7, 2]
sort(lst)

print(lst)

# OUTPUT
# [2, 3, 5, 6, 7, 8]
