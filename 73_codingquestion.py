# What's the expected output of the following code?

planets = 4 - 3 // 2 + -1
if planets < 0:
    print("#")
elif planets >= 2:
    print("##")
else:
    print("###")

# Output
# ##

# Hint
# Hence the expression 4 - 3 // 2 + -1 evaluates to 2, and the control reaches to second print() invocation only.
