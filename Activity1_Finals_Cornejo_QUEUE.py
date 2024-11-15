from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from CircularQueue import CircularQueue as CircularQueue
from LinkedDeque import LinkedDeque as Deque
from PositionalList import PositionalList as PositionalList
Q = Queue()
S = Stack()
CircQ = CircularQueue()
D = Deque()
P = PositionalList()


for i in range(1, 9):
    D.insert_last(i)
    print(D.last())
print()
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
D.insert_last(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_last())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
for i in range(1, 9):
    print(D.delete_first())