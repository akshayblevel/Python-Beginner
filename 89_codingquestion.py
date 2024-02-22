# What is the expected result of the following code?

def process(data):
    data[1] = 2
    return data[-2]


measurements = [0 for i in range(3)]
process(measurements)
print(measurements[-2])


'''
The process() function redefines the second element of its parameter which means that
the change affects the argument(which is visible globally). This is why the middle element of 
the measurements list(which can be indexed as [-2]) contains 2, not zero. 
'''

# OUTPUT
# 2
