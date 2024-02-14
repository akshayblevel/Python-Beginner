# What is the expected output of the following code?

list_one = [1, 2]
list_two = list_one[:]
list_two.append(3)
print(list_one[-1])

'''
As list_two originates from a slice of list_one, both these names refer to
different(separate) data. Therefore, the element appended to the first of them
doesn't exist in the second, and vice versa.
'''

# OUTPUT
# 2
