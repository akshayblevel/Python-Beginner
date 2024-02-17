# What is the expected output of the following code?

train_speed = {"FlyingScotman": 201, "TGV": 320, "Shinkansen": 320}

for train in train_speed:
    print(train[0], end="")

'''
Iterating through a dictionary is actually iterating through a list of all the dictionary's keys.
The [0] index retrieves the first character of each key so we won't expect any other answer.
'''

# OUTPUT
# FTS
