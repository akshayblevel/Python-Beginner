'''
BINARY SEARCH

list =  4    7   8   12  45  99
index = 0    1   2   3   4   5

Search Value = 45

STEP 1: Sort the list
STEP 2: Find the lower and upper bound
        lower bound = first index i.e 0
        upper bound = last index i.e 5
STEP 3: Find the mid-index
        mid-index = (lower + upper) / 2
                  = (0 + 5) / 2
                  = 2
STEP 4: mid-value = 8
STEP 5: If mid-value equals search value then end
STEP 6: If search value is less than mid-value
        upper bound = mid-value
STEP 7: If search value is greater than mid-value
        lower bound = mid-value
        lower bound = 8
STEP 8: Repeat from step 3 till you get search value
'''

pos = -1
def search(lst, n):
    lower_bound = 0
    upper_bound = len(lst)-1

    while lower_bound <= upper_bound:
        mid_value = (lower_bound + upper_bound) // 2
        if lst[mid_value] == n:
            globals()['pos'] = mid_value
            return True
        else:
            if lst[mid_value] < n:
                lower_bound = mid_value + 1
            else:
                upper_bound = mid_value - 1

    return False


lst = [4, 7, 8, 12, 45, 99]
n = 45


if search(lst, n):
    print("Value Found at ", pos+1)
else:
    print("Value Not Found")
