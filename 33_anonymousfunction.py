from functools import reduce


# Normal function
def square(x):
    x = x * x
    return x


result = square(5)
print(result)  # 25

# Anonymous function

fun = lambda x: x * x
result = fun(6)
print(result)  # 36

# filter


def is_even(n):
    return n % 2 == 0


nums = [14, 10, 81, 17, 10, 17, 16, 11, 84]
evens = list(filter(is_even, nums))
print(evens)
# [14, 10, 10, 16, 84]

odd = list(filter(lambda n: n % 2 != 0, nums))
print(odd)
# [81, 17, 17, 11]


# map

doubles = list(map(lambda n: n * 2, evens))
print(doubles)  # [28, 20, 20, 32, 168]

# reduce

total = reduce(lambda a, b: a + b, doubles)
print(total)  # 268
