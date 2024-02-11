# What happens when the user runs the following code?

angle = 1
for i in range(2, 5):
    if 2 * i > 4:
        angle += 1
else:
    angle -= 1
print(angle)

'''
In the sequence 2, 3, 4 which is passed through by the i variable,
only the first value (2) doesn't satisfy the condition 2 * i > 4.
In  effect, the angle variable is incremented twice inside the loop's body 
and decremented once inside the else: branch, which finally sets it to 2.
'''

# OUTPUT
# 2