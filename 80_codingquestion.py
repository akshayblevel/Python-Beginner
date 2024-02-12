# What is the expected output of the following code?

others = 0
for i in range(2):
    for j in range(2):
        if i != j:
            others += 1
else:
    others += 1
print(others)

'''
Both loops, the outer and the inner, go through the same, two-element set of values
which consist of 0 and 1. This means the condition i != j will be satisfied twice, which
results in two increments performed inside the loop's body and an additional one in the outer
loop's else: branch, that's why the final others value is equal to 3.
'''

# OUTPUT
# 3
