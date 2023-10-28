
x = 14


# Global variable - accessible inside function
def accessvariable():
    print("Inside Function: ", x)


accessvariable()
print("Outside Function: ", x)
# Inside Function:  14
# Outside Function:  14


# Global variable - change value of global variable creates actually new
def accessvariable():
    x = 10
    print("Inside Function: ", x)


accessvariable()
print("Outside Function: ", x)
# Inside Function:  10
# Outside Function:  14


# Global variable - change value of global variable without creating new
def accessvariable():
    global x
    x = 10
    print("Inside Function: ", x)


accessvariable()
print("Outside Function: ", x)
# Inside Function:  10
# Outside Function:  10


# Global variable - change value of global variable in presence of local variable with same name
def accessvariable():
    x = 10
    globals()['x'] = 25
    print("Inside Function - local: ", x)
    print("Inside Function - global: ", globals()['x'])


accessvariable()
print("Outside Function: ", x)
# Inside Function - local:  10
# Inside Function - global:  25
# Outside Function:  25
