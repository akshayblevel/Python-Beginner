
def counter(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


numlst = [14, 10, 81, 17, 10, 17, 16, 11, 84]
e, o = counter(numlst)

print("Even : {} and Odd : {}".format(e, o))
# Even : 5 and Odd : 4
