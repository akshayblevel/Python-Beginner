class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_rear(self, item):
        self.items.append(item)

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


d = Deque()
print("Is Empty:", d.is_empty())
print("Add Rear 10", d.add_rear(10))
print("Add Rear 20", d.add_rear(20))
print("Add Front 5", d.add_front(5))
print("Add Front 1", d.add_front(1))
print("Size:", d.size())
print("Is Empty:", d.is_empty())
print("Add Rear 30", d.add_rear(30))
print("Items:", d.items)
print("Remove Rear", d.remove_rear())
print("Remove Front", d.remove_front())
print("Add Front 2", d.add_front(2))
print("Add rear 40", d.add_rear(40))
print(d.items)
