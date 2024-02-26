# What is the expected result of the following code?

def combine(width, height=2, depth=0, is_3D=False):
    return (is_3D, width, height, depth)


print(combine(1)[2])


'''
Only one parameter is explicitly set during invocation and it's width
all remaining parameters retain their default values
consequently, the function returns the following tuple: [False, 1, 2, 0]
the tuple's third element is 2and this is the output that goes to the screen.
'''

# OUTPUT
# 2
