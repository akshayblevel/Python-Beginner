# What happens when the user runs the following code?

angle = 0
for i in range(5):
    if i % 2 == 1:
        angle += 1
else:
    angle -= 1
print(angle)

'''
A close look at the inside of the for loop's body shows that the angle variable is incremented
twice; when the i variable is either 1 or 3 (these are the two cases when i % 2 == 1 is true).
The decrement occurs once - inside the else: branch.
That's why the final variable value is 1.
'''

# OUTPUT
# 1