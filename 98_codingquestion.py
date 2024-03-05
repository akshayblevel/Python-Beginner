# Is this valid in python?

def my_function():
    print(my_function.what)


my_function.what = "right?"
my_function()


'''
It is valid. In Python, everything is an object, including functions. 
But if we don't have what defined, we will get an Attribute error.
'''

# OUTPUT
# right?
