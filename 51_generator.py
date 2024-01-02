def starpattern():
    str = "*"

    while len(str) <= 5:
        val = str
        str = f'{(len(str)+1) *  "*"}'
        yield val


pattern = starpattern()

for i in pattern:
    print(i)

# *
# **
# ***
# ****
# *****
