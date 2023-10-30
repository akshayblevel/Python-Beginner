
class Pizza:

    def get_raw_material(self):
        print("dough, cheese, tomato, onion, olive")


pizza1 = Pizza()
pizza2 = Pizza()

# Call class method and pass object as parameter
Pizza.get_raw_material(pizza1)
Pizza.get_raw_material(pizza2)

# Call class method using an object where no need to pass object as parameter
pizza1.get_raw_material()
pizza2.get_raw_material()
