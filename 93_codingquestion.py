# What is the expected result of the following code?

def walk(top):
    if top == 0:
        return 0
    return top + walk(top - 1)


print(walk(2))


'''
walk(2) which returns 2 + walk(1)
walk(1) which returns 1 + walk(0)
walk(0) which returns 0 and breaks the invocation chain
consequently, the final result is 2 + 1 + 0
'''

# OUTPUT
# 3
