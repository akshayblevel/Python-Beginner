# What is the expected result of the following code?

a = True
print(('A', 'B')[a == False])

'''
Here ('A', 'B') is a tuple. We could access values in tuple, use the square brackets []. The a == False 
is an expression that could be evaluated as boolean. In Python 3.x True and False are keywords and will 
always be equal to 1 and 0. So the result will be A
'''


# OUTPUT
# A
