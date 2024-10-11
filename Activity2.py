class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise Exception("Queue is empty")

    def first(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise Exception("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

# Simulation of operations
q = Queue()

operations = [
    "Q.enqueue(5)",
    "Q.enqueue(3)",
    "len(Q)",
    "Q.dequeue()",
    "Q.is_empty()",
    "Q.dequeue()",
    "Q.is_empty()",
    "Q.dequeue()",
    "Q.enqueue(7)",
    "Q.enqueue(9)",
    "Q.first()",
    "Q.enqueue(4)",
    "len(Q)",
    "Q.dequeue()"
]

results = []
for op in operations:
    if op == "Q.enqueue(5)":
        q.enqueue(5)
        results.append(None)
    elif op == "Q.enqueue(3)":
        q.enqueue(3)
        results.append(None)
    elif op == "len(Q)":
        results.append(len(q))
    elif op == "Q.dequeue()":
        try:
            results.append(q.dequeue())
        except Exception as e:
            results.append(str(e))
    elif op == "Q.is_empty()":
        results.append(q.is_empty())
    elif op == "Q.enqueue(7)":
        q.enqueue(7)
        results.append(None)
    elif op == "Q.enqueue(9)":
        q.enqueue(9)
        results.append(None)
    elif op == "Q.first()":
        try:
            results.append(q.first())
        except Exception as e:
            results.append(str(e))
    elif op == "Q.enqueue(4)":
        q.enqueue(4)
        results.append(None)

print("Simulation results:")
for op, res in zip(operations, results):
    print(f"{op}: {res}")

# Final sequence of operations
final_sequence = [
    "enqueue(5)", "enqueue(3)", "dequeue()", "enqueue(2)", "enqueue(8)",
    "dequeue()", "dequeue()", "enqueue(9)", "enqueue(1)", "dequeue()",
    "enqueue(7)", "enqueue(6)", "dequeue()", "dequeue()", "enqueue(4)",
    "dequeue()", "dequeue()"
]

q = Queue()
final_results = []

for op in final_sequence:
    if op.startswith("enqueue"):
        value = int(op[8:-1])
        q.enqueue(value)
        final_results.append(None)
    elif op == "dequeue()":
        try:
            final_results.append(q.dequeue())
        except Exception as e:
            final_results.append(str(e))

print("\nFinal sequence results:")
for op, res in zip(final_sequence, final_results):
    print(f"{op}: {res}")