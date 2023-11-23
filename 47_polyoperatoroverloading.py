
class Employee:

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def __add__(self, other):
        s1 = self.s1 + other.s1
        s2 = self.s2 + other.s2
        e3 = Employee(s1, s2)

        return e3

    def __gt__(self, other):
        s1 = self.s1 + other.s1
        s2 = self.s2 + other.s2
        if s1 > s2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.s1, self.s2)


e1 = Employee(10, 20)
e2 = Employee(30, 40)

e3 = e1 + e2
print(e3.s1)  # 40

if e1 > e2:
    print("e1 wins")
else:
    print("e2 wins")

# e2 wins

print(e3)  # 40 60 - by default it prints the address of an object but as we have overridden __str__ it prints value
