
def addition(x, y):
    z = x + y
    return z


result = addition(10, 12)
print(result)  # 22

result = addition('akki', 'patel')
print(result) # akkipatel


def add_sub(x, y):
    a = x + y
    s = x - y
    return a, s


res, res1 = add_sub(10, 12)
print(res)  # 22
print(res1)  # -2
print(res, res1)  # 22 -2
