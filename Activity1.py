'''class Stack:
    def __init__(self):
        self.items = []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


stack = Stack()
results = []


operations = [
    (stack.push, 5),        # S.push(5)
    (stack.push, 3),        # S.push(3)
    (len, stack),           # len(S)
    (stack.pop, None),      # S.pop()
    (stack.is_empty, None), # S.is_empty()
    (stack.pop, None),      # S.pop()
    (stack.push, 7),        # S.push(7)
    (stack.push, 9),        # S.push(9)
    (stack.top, None),      # S.top()
    (stack.push, 4),        # S.push(4)
    (len, stack),           # len(S)
    (stack.pop, None),      # S.pop()
    (stack.push, 6),        # S.push(6)
    (stack.push, 8),        # S.push(8)
    (stack.pop, None)       # S.pop()
]


for func, value in operations:
    if value is not None:
        func(value)
    else:
        results.append(func())

for result in results:
    print(result)


'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

S = Stack()
results = []

operations = [
    (S.push, 5),
    (S.push, 3),
    (S.pop, None),
    (S.push, 2),
    (S.push, 8),
    (S.pop, None),
    (S.pop, None),
    (S.push, 9),
    (S.push, 1),
    (S.pop, None),
    (S.push, 7),
    (S.push, 6),
    (S.pop, None),
    (S.pop, None),
    (S.push, 4),
    (S.pop, None),
    (S.pop, None)
]

for func, value in operations:
    if value is not None:
        func(value)
    else:
        results.append(func())

print("Returned values during operations:", results)

