from numpy import *

arr = array([1, 2, 3, 4, 5])

# Add number in each element of an array
arr = arr + 5
print(arr)  # [ 6  7  8  9 10]

arr1 = [2, 4, 6, 8, 10]
# Add two different arrays
arr2 = arr + arr1
print(arr2)  # [ 8 11 14 17 20]

# Concatenate two arrays
print(concatenate([arr, arr1]))  # [ 6  7  8  9 10  2  4  6  8 10]

print(sin(arr))  # [-0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]
print(cos(arr))  # [ 0.96017029  0.75390225 -0.14550003 -0.91113026 -0.83907153]
print(sum(arr))  # 40
print(sqrt(arr))  # [2.44948974 2.64575131 2.82842712 3.         3.16227766]
print(min(arr))  # 6
print(max(arr))  # 10

# Copy array
# ----------

# Copy - array element and memory address same

arr = array([1, 3, 5, 7, 9])
copyArr = arr
print(copyArr)  # [1 3 5 7 9]
print(id(arr))  # 1531319910640
print(id(copyArr))  # 1531319910640

# Shallow Copy - array element is same but address is different, but if you modify one array, changes applied to both

copyArr = arr.view()
print(copyArr)  # [1 3 5 7 9]
print(id(arr))  # 1984046072048
print(id(copyArr))  # 1984042661520
copyArr[1] = 2
print(arr)  # [1 2 5 7 9]
print(copyArr)  # [1 2 5 7 9]

# Deep Copy - array element is same but address is different, if you modify one array, changes won't be applied to both

copyArr = arr.copy()
print(copyArr)  # [1 2 5 7 9]
print(id(arr))  # 1591924195568
print(id(copyArr))  # 1592199057104
copyArr[1] = 3
print(arr)  # [1 2 5 7 9]
print(copyArr)  # [1 3 5 7 9]
