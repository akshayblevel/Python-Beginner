# How many asterisks (*) does the code output to the screen?

torque = 1
while torque < 2:
    torque *= 2
    print("*", end="")
else:
    print("*")

'''
The while loop's body is executed only once, as the torque variable is set
to 2 during the loop's first turn. This means that the loop will emit one asterisk.
The second asterisk is emitted by the else: branch.
'''

# OUTPUT
# **
