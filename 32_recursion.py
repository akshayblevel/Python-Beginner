import sys

print(sys.getrecursionlimit())  # 1000 this is the default limit

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())  # 2000 limit we increased to


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


result = factorial(5)
print(result)  # 120
