# What's the expected output of the following code?

planets = 1 + 1 // 2 * 3
if planets > 0:
    print("#")
elif planets > 1:
    print("##")
else:
    print("###")

# Output
# #

# Hint
# Hence the expression 1 + 1 // 2 * 3 evaluates to 1, and the control reaches the very first print() invocation.
