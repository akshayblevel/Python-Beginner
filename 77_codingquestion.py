# What happens when the user runs the following code?

power = 1
while power < 5:
    power += 1
    print("@", end="")
    if power == 3:
        break
else:
    print("@")

'''
As the power variable begins its life with the value 1, the control smoothly enters
the while loop. Next, the power variable is incremented(it's 2 at the moment) and one @ is 
emitted. The loop's second turn causes the variable to be incremented again, and this is the moment
when the break instruction goes onto the stage - the loop is terminated and the else: branch is executed.
In effect, the second (and at the same time the last)@ is printed. 
'''

# OUTPUT
# @@
