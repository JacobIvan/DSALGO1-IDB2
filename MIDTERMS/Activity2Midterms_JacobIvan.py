class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, itemfromOBJ):
        print(f"Current queue contents: Q = {self.items} ")
        self.items.append(itemfromOBJ)
        print(f"Item to Enqueue: {itemfromOBJ}\nQueue after the Enqueue: {self.items}\n")

    def dequeue(self):
        if not len(self.items) == 0:
            print(f"Current queue contents: Q = {self.items}")
            popped = self.items.pop(0)
            print(f"Item to dequeue: [{popped}]\nQueue after the Dequeue: {self.items}")
            print()
        else:
            print("Queue is empty [:(] Can no longer dequeue")
            print()

    def first(self):
        if not self.is_empty():
            print(f"First element: [{self.items[0]}]")
        else:
            print("Queue is empty")
    def len(self):

        print(f"Current queue length: {len(self.items)}")
        print()
        return len(self.items)

    def is_empty(self):
        walanglaman = len(self.items) == 0
        return print(f"Is the queue empty? {walanglaman}")

Q = Queue()
print("Operation: Q.enqueue(5)")
Q.enqueue(5)

print("Operation: Q.enqueue(3) ")
Q.enqueue(3)

print("Operation: Q.len() ")
Q.len()

print("Operation: Q.dequeue()")
Q.dequeue()

print("Operation: Q.is_empty()")
Q.is_empty()

print("Operation: Q.dequeue()")
Q.dequeue()

print("Operation: Q.is_empty()")
Q.is_empty()

print("Operation: Q.is_empty()")
Q.is_empty()

print("Operation: Q.dequeue()")
Q.dequeue()

print("Operation: Q.enqueue(7)")
Q.enqueue(7)

print("Operation: Q.enqueue(9)")
Q.enqueue(9)

print("Operation: Q.len()")
Q.len()

print("Operation: Q.enqueue(4)")
Q.enqueue(4)

print("Operation: Q.len()")
Q.len()

print("Operation: Q.dequeue()")
Q.dequeue()

print("   * =================== > End of Simulation 1 < ========================= *")
'''PART TWO SIMULATION'''

Q2 = Queue()
print("Operation: Q2.enqueue(5) ")
Q2.enqueue(5)

print("Operation: Q2.enqueue(3) ")
Q2.enqueue(3)

print("Operation: Q2.dequeue() ")
Q2.dequeue()

print("Operation: Q2.enqueue(2) ")
Q2.enqueue(2)

print("Operation: Q2.enqueue(8) ")
Q2.enqueue(8)

print("Operation: Q2.dequeue()")
Q2.dequeue()

print("Operation: Q2.dequeue()")
Q2.dequeue()

print("Operation: Q2.enqueue(9)")
Q2.enqueue(9)

print("Operation: Q2.enqueue(1)")
Q2.enqueue(1)

print("Operation: Q2.dequeue()")
Q2.dequeue()

print("Operation: Q2.enqueue(7)")
Q2.enqueue(7)

print("Operation: Q2.enqueue(6)")
Q2.enqueue(6)

print("Operation: Q2.dequeue()")
Q2.dequeue()

print("Operation: Q2.dequeue()")
Q2.dequeue()

print("Operation: Q2.enqueue(4)")
Q2.enqueue(4)

print("Operation: Q2.dequeue()")
Q2.dequeue()

print("Operation: Q2.dequeue()")
Q2.dequeue()


