class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print("Queue Elements:", self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.display()

print("Size of Queue:", q.size())

print("First element removed:", q.dequeue())

q.display()
