from LinkedStack import LinkedStack
from LinkedQueue import LinkedQueue
class StackandQueue:

    def __init__(self):
        self.front_queue = LinkedQueue()
        self.back_stack = LinkedStack()

    def len(self):
        return len(self.front_queue) + len(self.back_stack)

    def is_empty(self):
        return self.len() == 0

    def add_first(self, e):
        self.front_queue.enqueue(e)

    def add_last(self, e):
        self.back_stack.push(e)

    def delete_first(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        if self.front_queue.is_empty():
            while not self.back_stack.is_empty():
                self.front_queue.enqueue(self.back_stack.pop())
        return self.front_queue.dequeue()

    def delete_last(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        if self.back_stack.is_empty():
            while not self.front_queue.is_empty():
                self.back_stack.push(self.front_queue.dequeue())
        return self.back_stack.pop()

    def first(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        if self.front_queue.is_empty():
            while not self.back_stack.is_empty():
                self.front_queue.enqueue(self.back_stack.pop())
        return self.front_queue.first()

    def last(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        if self.back_stack.is_empty():
            while not self.front_queue.is_empty():
                self.back_stack.push(self.front_queue.dequeue())
        return self.back_stack.top()

D = StackandQueue()

for i in range (1 ,6):
    D.add_first(i)

print(D.first())
print(D.last())
print(D.delete_first())
print(D.delete_last())
print(D.delete_first())

