# What is the expected result of the following code?

def combine(width, height=10, depth=0, is_3D=False):
    return (is_3D, width, height, depth)


print(combine(height=1, width=2)[3])


'''
Two parameters are set during invocation i.e. height=1 and width=2
two parameters retains their default values i.e depth=0 and is_3D=False
In effect, the function returns the following list: [False, 2, 1, 0]
the list's fourth element is zero, thus, you see it on the screen.
'''

# OUTPUT
# 0
