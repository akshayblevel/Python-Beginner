
class Customer:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.add = self.Address()

    class Address:

        def __init__(self):
            self.add1 = 'Ayappa Colony'
            self.add2 = 'Besided Petrol Pump'
            self.city = 'Hyderabad'


c1 = Customer('Jemin', 1)
c2 = Customer('Chirantan', 2)

a1 = c1.Address()
print(a1.add1, a1.add2, a1.city)

a2 = Customer.Address()
print(a2.add1, a2.add2, a2.city)
