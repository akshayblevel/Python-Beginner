# What is the expected output of the following code?

train_speed = {"FlyingScotman": 201, "TGV": 320, "Shinkansen": 320}

for train in train_speed.values():
    print(str(train)[0], end="")

'''
As the .values() method returns a list of dictionary values(the keys are ignored!), the [0] index
retrieves the first character of the string obtained from each value's integer number. This is where
the answer came from.
'''

# OUTPUT
# 233
