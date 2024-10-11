class Stack:
    def __init__(self):
        self.items = []

    def push(self, itemfromOBJ):
        self.items.append(itemfromOBJ)
        print(f"Pushed element {itemfromOBJ}; After the push: {self.items}")

    def pop(self):
        if not len(self.items) == 0:
            popped = self.items.pop()
            print(f"Popped element: [{popped}]; After the pop: {self.items}")
            print()
        else:
            print("Stack is empty [:(] Can no longer pop")
            print()

    def top(self):
        if not self.is_empty():
            print(f"Rightmost/Top element: [{self.items[-1]}]")
        else:
            print("Stack is empty")

    def len(self):
        print()
        print(f"Current stack length: {len(self.items)}")

    def is_empty(self):
        walanglaman = len(self.items) == 0
        print(f"Is the stack empty? {walanglaman}")
        return walanglaman

S = Stack()
print("Simulation 1")
S.push(5)
S.push(3)
S.len()
S.pop()
S.is_empty()
S.pop()
S.is_empty()
S.pop()
S.push(7)
S.push(9)
S.top()
S.push(4)
S.len()
S.pop()
S.push(6)
S.push(8)
S.pop()
print()
print("Simulation 2")
X = Stack()
X.push(5)
X.push(3)
X.pop()
X.push(2)
X.push(8)
X.pop()
X.pop()
X.push(9)
X.push(1)
X.pop()
X.push(7)
X.push(6)
X.pop()
X.pop()
X.push(4)
X.pop()
X.pop()


