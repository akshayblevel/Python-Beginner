
class Author:

    name = 'Akshay'

    def __init__(self, r1, r2, r3):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3

    def get_r1(self):           # Accessor Method
        return self.r1

    def set_r1(self, value):     # Mutator Method
        self.r1 = value

    def avg_rating(self):       # Instance Method
        return (self.r1 + self.r2 + self.r3) / 3

    @classmethod
    def get_author(cls):        # Class Method
        return cls.name

    @staticmethod               # Static Method
    def get_class_info():
        print("This class provides Author and his rating info")


a1 = Author(9, 8, 6)
a2 = Author(8, 7, 6)

print(a1.avg_rating())
print(Author.get_author())
Author.get_class_info()
