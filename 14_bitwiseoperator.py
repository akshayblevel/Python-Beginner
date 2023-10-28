
# ~ compliment
x = 14
# Binary of 14 is 00001110
# Compliment of above number is reverse of binary number that is 11110001
print(~x)  # -15
# How come -15?
# Binary of 15 is 00001111
# Now 1s compliment of above number is 11110000
# Add 1 in above number to get 2s compliment that is 11110001 which equals -15

# Bitwise AND operator
print(14 & 10)  # 10
# 14  00001110
# 10  00001100
# -------------
#     00001100  We get 1 when both are 1

# Bitwise OR operator
print(14 | 10)  # 14
# 14  00001110
# 10  00001100
# -------------
#     00001110  We get 1 when any of is 1

# Bitwise XOR operator
print(14 ^ 10)  # 4
# 14  00001110
# 10  00001100
# -------------
#     00000010  We get 1 when both bits are not same

# Left Shift Operator
print(14 << 1)  # 28
# 14                1110.000
# shift 1 digit     11100.00  that is 28

# Right Shift Operator
print(14 >> 2)  # 3
# 14                1110.000
# shift 1 digit     11.100  that is 3
