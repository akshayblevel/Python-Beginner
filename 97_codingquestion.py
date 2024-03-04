# What is the expected result of the following code?

x = 100
y = x
x = 200

print(y)

'''
Python does not read this as, “y should now refer to the variable x.” Rather, it read it as, 
“y should now refer to whatever value x refers to.”
Because x refers to the integer 100, y now refers to the integer 100. 
After these two assignments (“x = 100” and “y = x”), there are now two references to the integer 100 
that did not previously exist.
When we say that “x = 200”, we’re removing one of those references, such that x no longer refers to 100. 
Instead, x will now refer to the integer 200.
'''

# OUTPUT
# 100
