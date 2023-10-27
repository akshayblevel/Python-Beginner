from numpy import *

arr = array([1, 2, 3])  # numpy has different syntax, no need to pass type
print(arr)
# [1 2 3]

arr1 = array([1, 2, 3], int)  # numpy, we can give type at end if we want
print(arr1)
# [1 2 3]

# linspace - Return evenly spaced numbers over a specified interval.
arr = linspace(11, 15, 10)
print(arr)

# arange - Return evenly spaced values within a given interval.
arr = arange(0, 9, 2)
print(arr)

# logspace - Return numbers spaced evenly on a log scale.0
arr = logspace(0, 4, 10)
print(arr)
print('%2f' %arr[4])

# zeros - Return a new array of given shape and type, filled with zeros.
arr = zeros(5)
print(arr)  # [0. 0. 0. 0. 0.]

# ones - Return a new array of given shape and type, filled with ones.
arr = ones(5)
print(arr)  # [1. 1. 1. 1. 1.]

# ones with int - Return a new array of given shape and type, filled with ones.
arr = ones(5, int)
print(arr)  # [1 1 1 1 1]
