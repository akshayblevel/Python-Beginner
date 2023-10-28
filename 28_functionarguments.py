
def updatevalue(value):
    print("Before updating value: ", value)
    print("Before updating value address: ", id(value))
    value = value * 2
    print("After updating value: ", value)
    print("After updating value address: ", id(value))


inputValue = 5
print("Initial inputValue: ", inputValue)
print("Initial inputValue address: ", id(inputValue))
updatevalue(inputValue)
print("After updating inputValue: ", inputValue)

# Initial inputValue:  5
# Initial inputValue address:  140725372904360
# Before updating value:  5
# Before updating value address:  140725372904360
# After updating value:  10
# After updating value address:  140725372904520
# After updating inputValue:  5

# Input value is not getting changed even after calling function that means pass by value


def updatelstvalue(value):
    print("Before updating value: ", value)
    print("Before updating value address: ", id(value))
    value[1] = 25
    print("After updating value: ", value)
    print("After updating value address: ", id(value))


inputValue = [10, 20, 30]
print("Initial inputValue: ", inputValue)
print("Initial inputValue address: ", id(inputValue))
updatelstvalue(inputValue)
print("After updating inputValue: ", inputValue)

# Initial inputValue:  [10, 20, 30]
# Initial inputValue address:  2798836798784
# Before updating value:  [10, 20, 30]
# Before updating value address:  2798836798784
# After updating value:  [10, 25, 30]
# After updating value address:  2798836798784
# After updating inputValue:  [10, 25, 30]

# Input Value (List) is getting changed after calling function that means pass by reference
