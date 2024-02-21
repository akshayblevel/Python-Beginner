# What is the expected result of the following code?

def process(data):
    data = [1, 2, 3]
    return data[-2]


measurements = [0 for i in range(3)]
process(measurements)
print(measurements[-2])


'''
The process() function redefines its parameter, which means that the parameter visible 
locally (in the function's scope) refers to different data than the argument used globally.
It also means that this change doesn't affect global data.
Therefore the measurements list still contains zeros.
'''

# OUTPUT
# 0
