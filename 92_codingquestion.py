# What is the expected result of the following code?

def walk(stop, start=1):
    print(start, end=" ")
    if start + 1 < stop:
        walk(stop, start + 1)


walk(3)


'''
walk(3) which is in fact executed as walk(3, 1)
walk(3, 2) (1 is printed in this cycle)
No invocation occurs now as the condition is not met, but 2 is printed)
'''

# OUTPUT
# 1 2
