# What is the expected output of the following code?

others = -1
for i in range(1, 3):
    for j in range(1, 2):
        if i == j:
            others += 1
    else:
        others += 1
print(others)

'''
The sequence of values produced by the outer for loop contains two values: 1 and 2.
The inner for loop covers one value only:1. A common part of these two sets contains
only one value: 1. So the other variable is incremented once the inner loop's body
and twice inside the loop's else: branch. Considering that the initial variable's value
is -1, it will leave the loops with 2.
'''

# OUTPUT
# 2
