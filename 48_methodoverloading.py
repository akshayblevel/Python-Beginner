class Student:

    def total_marks(self, maths=None, science=None, english=None):
        total = 0
        if maths!=None and science!=None and english!=None:
            total = maths+science+english
        elif maths!=None and science!=None:
            total = maths + science
        else:
            total = maths

        return  total


s = Student()
print(s.total_marks(10, 20))
print(s.total_marks(10, 20, 30))
