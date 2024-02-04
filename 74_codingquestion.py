# How many asterisks (*) does the code output to the screen?

torque = 5
while torque > 0:
    torque -= 3
    print("*", end="")
else:
    print("*")

'''
To find the answer, we need to analyze the sequence of values the torque variable takes:
it starts with 5 and goes through 2 and -1. This means that the while loop's body is responsible for the first 
two asterisks. The third asterisk comes from the else: branch. 
'''

# OUTPUT
# ***
