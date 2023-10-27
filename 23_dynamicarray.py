from array import *

arr = array('i', [])

arrLen = int(input("Enter Array Length:"))

for i in range(arrLen):
    arrEle = int(input("Enter Array Element:"))
    arr.append(arrEle)

print(arr)

# Enter Array Length:3
# Enter Array Element:10
# Enter Array Element:20
# Enter Array Element:30
# array('i', [10, 20, 30])
