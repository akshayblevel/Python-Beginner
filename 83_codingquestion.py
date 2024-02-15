# What is the expected result of the following code?

answers = (True, True, False)
selection = answers[3:]
points = 0
for answer in selection[-2:]:
    if answer:
        points += 1
print(points)

'''
The selection has been created as a zero-element of answers
(the slice starts beyond the list!). The second slice (the 
one in the loop statement) changes nothing (the empty list
remains empty), and therefore points is not incremented even
once inside the loop, and its final value is 0.
'''

# OUTPUT
# 0
