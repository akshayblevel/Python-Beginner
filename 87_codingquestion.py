# What is the expected result of the following code?

def sample(value):
    return value + value


x = sample(value=1)
y = sample(x)
print(y)


'''
The function returns its argument doubled. Although each of the invocations makes use of
different argument passing techniques, the effect remains the same and this is why the
initial argument value equal to 1 turns into 4.
'''

# OUTPUT
# 4