class A:

    def display(self):
        print("display method of class A")


class B(A):
    pass


a1 = B()
a1.display()

# OUTPUT
# display method of class A


class C(A):
    def display(self):
        print("display method of class C")


a1 = C()
a1.display()

# OUTPUT
# display method of class C
