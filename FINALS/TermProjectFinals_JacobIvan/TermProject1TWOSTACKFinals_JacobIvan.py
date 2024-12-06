from LinkedStack import LinkedStack as  LinkedStack
class TwoStackDeq:
    def __init__(self):

        self.front_stack = LinkedStack()
        self.rear_stack = LinkedStack()

    def is_empty(self):
        return self.front_stack.is_empty() and self.rear_stack.is_empty()

    def __len__(self):
        return len(self.front_stack) + len(self.rear_stack)

    def add_first(self, e):
        self.front_stack.push(e)

    def add_last(self, e):
        self.rear_stack.push(e)

    def _transfer(self, source, target):
        while not source.is_empty():
            target.push(source.pop())

    def first(self):
        if self.front_stack.is_empty():
            if self.rear_stack.is_empty():
                raise Exception("Deque is empty")
            self._transfer(self.rear_stack, self.front_stack)
        return self.front_stack.top()

    def last(self):
        if self.rear_stack.is_empty():
            if self.front_stack.is_empty():
                raise Exception("Deque is empty")
            self._transfer(self.front_stack, self.rear_stack)
        return self.rear_stack.top()

    def remove_first(self):
        if self.front_stack.is_empty():
            if self.rear_stack.is_empty():
                raise Exception("Deque is empty")
            self._transfer(self.rear_stack, self.front_stack)
        return self.front_stack.pop()

    def remove_last(self):
        if self.rear_stack.is_empty():
            if self.front_stack.is_empty():
                raise Exception("Deque is empty")
            self._transfer(self.front_stack, self.rear_stack)
        return self.rear_stack.pop()

D = TwoStackDeq()

for i in range (1 ,6):
    D.add_first(i)

print(D.first())
print(D.last())

print(D.remove_first())
print(D.remove_last())
print(D.remove_first())

