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
S.push(D.delete_first())
S.push(D.delete_first())
S.push(D.delete_first())
D.insert_last(D.delete_first())
S.push(D.delete_first())
S.push(D.delete_last())
D.insert_first(S.pop())
D.insert_first(S.pop())
D.insert_first(S.pop())
D.insert_first(S.pop())
D.insert_first(S.pop())
for i in range(1, 9):
    print(D.delete_first())