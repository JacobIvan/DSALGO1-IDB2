
from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from LinkedDeque import LinkedDeque as Deque
Q = Queue()
S = Stack()
D1 = Deque()
D2 = Deque()
print("_______________________________________________")
print("|Variable   |Contents                         |")
print("-----------------------------------------------")
for i in range (1,9):
    D1.insert_last(i)
for i in range (1,9):
    Q.enqueue(D1.delete_first())
for i in range (1,9):
    D1.insert_first(Q.dequeue())
for i in range (1,4):
    D1.insert_last(D1.delete_first())
for i in range (1,7):
    Q.enqueue(D1.delete_last())
for i in range (1,7):
    D1.insert_last(Q.dequeue())
for i in range (1,4):
    D1.insert_first(D1.delete_last())
#============print elements of D====================
print("|D1 contents|", end='=')
while not D1.is_empty():
    print(D1.delete_first(), end='=|=')
#============print elements of Q =================
print()
print("|Q contents |", end='= ')
while not Q .is_empty():
    print(Q.dequeue(), end='=|')

for i in range (1,9):
    D2.insert_last(i)
for i in range (1,9):
    S.push(D2.delete_last())
for i in range (1,4):
    D2.insert_last(S.pop())
for i in range (1,3):
    D2.insert_first(S.pop())
for i in range (1,4):
    D2.insert_first(D2.delete_last())
for i in range (1,4):
    D2.insert_last(S.pop())
#============print elements of D2====================
print()
print("|D2 contents|", end='=')
while not D2.is_empty():
    print(D2.delete_first(), end='=|=')
#============print elements of S====================
print()
print("|S contents |", end='=')
while not S.is_empty():
    print(S.pop(), end='=|')
