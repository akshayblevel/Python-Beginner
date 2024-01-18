
def new_stack():
    stack = []
    return stack


def is_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


def pop(stack):
    if is_empty(stack):
        return "stack is empty"

    return stack.pop()


stack = new_stack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))
push(stack, str(50))

print("stack before pop: " + str(stack))
print("popped item: " + pop(stack))
print("stack after pop: " + str(stack))

'''
pushed item: 10
pushed item: 20
pushed item: 30
pushed item: 40
pushed item: 50
stack before pop: ['10', '20', '30', '40', '50']
popped item: 50
stack after pop: ['10', '20', '30', '40']
'''