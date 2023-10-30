
class Mobile:

    def __init__(self, company, version):
        self.company = company
        self.version = version

    def get_mobile(self):
        print("My mobile :", self.company, self.version)


mob1 = Mobile("Apple", 15)
mob2 = Mobile("Samsung", 12)

mob1.get_mobile()
mob2.get_mobile()

# My mobile : Apple 15
# My mobile : Samsung 12
