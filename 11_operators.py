
# Arithmatic | Assignment | Relational | Logical | Unary
# Arithmatic Operator

x = 14
y = 10

print(x + y)  # 24
print(x - y)  # 4
print(x * y)  # 140
print(x / y)  # 1.4
print(x % y)  # 4

# Assignment Operator

x = x + 2
print(x)  # 16

x += 1
print(x)  # 17

num, num1 = 14, 10
print(num)  # 14
print(num1)  # 10

# Unary Operator

num = -num
print(num)  # -14

print(num < num1)  # True
print(num > num1)  # False
print(num == num1)  # False
print(num <= num1)  # True
print(num >= num1)  # False
print(num != num1)  # True

# Logical Operator

num = 14
num1 = 10
print(num > 13 and num1 < 11)  # True
print(num > 13 and num1 < 10)  # False
print(num > 13 or num < 10)  # True

x = num > 13 and num1 < 11
print(not x)  # False
