class VegPizza:

    def prepare(self):
        print("Veg pizza prepared")


class NonVegPizza:

    def prepare(self):
        print("Non Veg pizza prepared")


class Pizza:

    def get_pizza(self, pizza_type):
        pizza_type.prepare()


veg = VegPizza()

pizza = Pizza()
pizza.get_pizza(veg)

# Veg pizza prepared - if you pass pizza_type as instance of NonVegPizza then it calls prepare method of NonVegPizza
