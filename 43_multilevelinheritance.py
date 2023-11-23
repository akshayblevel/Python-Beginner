
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


class GrandChild(Child):
    def grand_child_method1(self):
        print("Grand Child Method 1")

    def grand_child_method2(self):
        print("Grand Child Method 2")


grandChild = GrandChild()

grandChild.parent_method1()
grandChild.parent_method2()
grandChild.child_method1()
grandChild.child_method2()
grandChild.grand_child_method1()
grandChild.grand_child_method2()

# Parent Method 1
# Parent Method 2
# Child Method 1
# Child Method 2
# Grand Child Method 1
# Grand Child Method 2
