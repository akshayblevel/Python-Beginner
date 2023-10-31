class Employee:

    type = "FullTime"               # class level variable

    def __init__(self):
        self.company = "Apple"      # instance level variable
        self.experience = 10        # instance level variable


e1 = Employee()
e2 = Employee()

e2.experience = 5

Employee.type = "PartTime"          # change in class level variable implements in all instances

print(e1.company, e1.experience, e1.type)
print(e2.company, e2.experience, e2.type)

# Apple 10 PartTime
# Apple 5 PartTime
