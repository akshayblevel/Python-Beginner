from numpy import *

arr1 = array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr1)
# [[1 2 3]
#  [4 5 6]]

print(arr1.dtype)  # int32

print(arr1.ndim)  # 2 - two-dimensional array

print(arr1.shape)  # (2, 3) - 2 rows and 3 columns

print(arr1.size)  # 6 - Number of elements in an array

arr2 = arr1.flatten()
print(arr2)  # [1 2 3 4 5 6] - Converts two(multi)-dimensional array into one-dimensional

arr1 = array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
])

arr2 = arr1.reshape(3, 4)  # Change the dimension of an existing array
print(arr2)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

arr2 = arr1.reshape(2, 2, 3)  # 2 arrays with 2 rows and 3 columns
print(arr2)
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

# Create matrix
arr1 = array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

m = matrix(arr1)
print(m)
# [[1 2 3 4]
#  [5 6 7 8]]

m1 = matrix('1 2 3 4 ; 5 6 7 8')
print(m1)
# [[1 2 3 4]
#  [5 6 7 8]]

m2 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')  # 3 rows and 3 columns
print(m2)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(diagonal(m2))  # [1 5 9] - get all diagonal element of matrix
print(m2.min())  # 1
print(m2.max())  # 9

# Matrix Additon

m1 = matrix('1 3 5 ; 7 9 11 ; 13 15 17')
m2 = matrix('2 4 6 ; 8 10 12 ; 14 16 18')

m3 = m1 + m2
print(m3)
# [[ 3  7 11]
#  [15 19 23]
#  [27 31 35]]

# Matrix Multiplication
m1 = matrix('1 2 3 ; 4 5 6')        # 2 X 3 Matrix
m2 = matrix('7 8 ; 9 10 ; 11 12')   # 3 X 2 Matrix

# In order to multiply, m1 column should be equal to m2 row that is 3
# and result will be m1 row and m2 column that is 2 X 2

# 1 2 3         7  8
# 4 5 6         9  10
#               11 12

# result matrix will be 2 X 2 (m1 row will be multiplied with m2 column and so on)

# 1*7+2*9+3*11      1*8+2*10+3*12
# 4*7+5*9+6*11      4*8+5*10+6*12

# 58    64
# 139   154

m3 = m1*m2
print(m3)
# [[ 58  64]
#  [139 154]]
