class StarPattern:

    def __init__(self):
        self.str = "*"

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.str) <= 5:
            val = self.str
            self.str = f'{(len(self.str)+1) *  "*"}'
            return val
        else:
            raise StopIteration


pattern = StarPattern()

print(next(pattern))

# *
# **
# ***
# ****
# *****

for i in pattern:
    print(i)

# It won't print again as values are read once
