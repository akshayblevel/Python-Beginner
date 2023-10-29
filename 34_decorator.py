
# divide two numbers with condition that if numerator is less than denominator, swap the value

def division(a, b):
    print(a / b)


def swap_division(func):   # decorator applies logic on existing function, so no need to modify existing function
    def inner(x, y):
        if x < y:
            x, y = y, x
        return func(x, y)

    return inner


swapDivision = swap_division(division)
swapDivision(4, 8)  # 2.0 parameter value got swapped and result is 8 / 4 = 2.0
