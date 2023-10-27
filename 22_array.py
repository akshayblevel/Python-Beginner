from array import *

#   TypeCode  CType             PythonType          MinSizeInBytes
#   'b'       signed char       int                 1
#   'B'       unsigned char     int                 1
#   'u'       Py_UNICODE        unicode character   2
#   'h'       signed short      int                 2
#   'H'       unsigned short    int                 2
#   'i'       signed int        int                 2
#   'I'       unsigned int      int                 2
#   'l'       signed long       int                 4
#   'L'       unsigned long     int                 4
#   'f'       float             float               4
#   'd'       double            float               8

vals = array('i', [2, 5, 8, 11, 18])

# Get the address and size of an array
print(vals.buffer_info())  # (3090525830256, 5) (address, size)

for i in range(len(vals)):
    print(vals[i])

# 2
# 5
# 8
# 11
# 18

for e in vals:
    print(e)

# 2
# 5
# 8
# 11
# 18

# Print single element of an array
print(vals[1])  # 5

# Copy array in new array

newVals = array(vals.typecode, (a for a in vals))

for e in newVals:
    print(e)

# Reverse the array
vals.reverse()
print(vals)  # array('i', [18, 11, 8, 5, 2])

# Character
charArr = array('u', ['a', 'k', 's', 'h', 'a', 'y'])

for e in charArr:
    print(e)

# a
# k
# s
# h
# a
# y
