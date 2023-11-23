
class Parent:
    def __init__(self):
        print("Parent Constructor")

    def parent_method1(self):
        print("Parent Method 1")


class Child(Parent):
    def child_method1(self):
        print("Child Method 1")


child = Child()  # Parent Constructor
# when we create an instance of child, it calls parent constructor as child constructor is not available


class Parent1:
    def __init__(self):
        print("Parent1 Constructor")

    def parent1_method1(self):
        print("Parent1 Method 1")


class Child1(Parent1):
    def __init__(self):
        print("Child1 Constructor")

    def child1_method1(self):
        print("Child1 Method 1")


child1 = Child1()  # Child1 Constructor
# when we create an instance of child1, it calls child1 constructor as child1 constructor is available


class Parent2:
    def __init__(self):
        print("Parent2 Constructor")

    def parent2_method1(self):
        print("Parent2 Method 1")


class Child2(Parent2):
    def __init__(self):
        super().__init__()
        print("Child2 Constructor")

    def child2_method1(self):
        print("Child2 Method 1")


child2 = Child2()
# Parent2 Constructor
# Child2 Constructor
# when we create an instance of child2, it calls Child2 constructor and using super it calls Parent2 constructor


class Parent3:
    def __init__(self):
        print("Parent3 Constructor")

    def parent3_method1(self):
        print("Parent3 Method 1")


class Child3:
    def __init__(self):
        super().__init__()
        print("Child3 Constructor")

    def child3_method1(self):
        print("Child3 Method 1")


class GrandChild3(Parent3, Child3):
    def __init__(self):
        super().__init__()
        print("GrandChild3 Constructor")

    def grand_child3_method1(self):
        print("GrandChild3 Method 1")


child3 = GrandChild3()
# Parent3 Constructor
# GrandChild3 Constructor
# Super will give the priority to first inherited class (left to right), that's why Parent3 constructor is called in
# multiple inheritance
