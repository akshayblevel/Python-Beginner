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

vals = array('i',[2, 5, 8, 11, 18])
print(vals.buffer_info())  # (3090525830256, 5) (address, size)



