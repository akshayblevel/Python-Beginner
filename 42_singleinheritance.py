
class Parent:
    def parent_method1(self):
        print("Parent Method 1")

    def parent_method2(self):
        print("Parent Method 2")


class Child(Parent):
    def child_method1(self):
        print("Child Method 1")

    def child_method2(self):
        print("Child Method 2")


parent = Parent()

parent.parent_method1()
parent.parent_method2()

# Parent Method 1
# Parent Method 2

child = Child()

child.parent_method1()
child.parent_method2()
child.child_method1()
child.child_method2()

# Parent Method 1
# Parent Method 2
# Child Method 1
# Child Method 2
