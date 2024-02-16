# What is the expected result of the following code?

answers = (True, False, True)
selection = answers[2:]
points = 0
for answer in selection[-1:]:
    if answer:
        points += 1
print(points)

'''
The selection has been created as a one-element slice of the answers
list. Therefore, it is a separate, one-element list which contains True.
The second slice (the one in the loop statement) changes nothing(the only
list element is also its last element). In effect, points is incremented
once inside the loop and its final value is 1.
'''

# OUTPUT
# 1
