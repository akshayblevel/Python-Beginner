# What is the expected result of the following code?

squares = []

for x in range(5):
    squares.append(lambda: x**2)

print(squares[2]())
print(squares[4]())

'''
This happens because x is not local to the lambdas, but is defined in the outer scope, 
and it is accessed when the lambda is called — not when it is defined. 
At the end of the loop, the value of x is 4, so all the functions now return 4**2, i.e. 16.
'''


# OUTPUT
# 16
# 16
