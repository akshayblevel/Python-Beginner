# What happens when the user runs the following code?

power = 1
while power != 10:
    power *= 2
    if power == 5:
        continue
    print("@", end="")
else:
    print("@")

'''
As you can see, the power variable takes values which are subsequent power of 2(1,2,4,8,16,etc.)
10 does not belong to this set and the continue statement does not change anything either.
Consequently, the loop has no chance to be terminated, and runs infinitely.
'''

# OUTPUT
# The program enters an infinite loop
