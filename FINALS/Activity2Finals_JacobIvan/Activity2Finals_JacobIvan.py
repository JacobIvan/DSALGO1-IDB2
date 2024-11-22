import re
from LinkedStack import LinkedStack
from PositionalList import PositionalList

precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
operators = set(precedence.keys())
S = LinkedStack()
output = LinkedStack()

x = input("Enter any Arithmetic Equation :\n")
x = re.sub(r'(\d+|[a-zA-Z]+|\))', r' \1 ', x)
x = re.sub(r'([+\-*/^()])', r' \1 ', x)
x = ' '.join(x.split())
tokens = x.split()

for token in tokens:
    if token.isalnum():
        output.push(token)
    elif token in operators:
        while (not S.is_empty() and S.top() != '(' and
               precedence.get(S.top(), 0) >= precedence[token]):
            output.push(S.pop())
        S.push(token)
    elif token == '(':
        S.push(token)
    elif token == ')':
        while not S.is_empty() and S.top() != '(':
            output.push(S.pop())
        if S.is_empty():
            raise ValueError("Mismatched parentheses")
        S.pop()
    else:
        raise ValueError(f"Unknown token: {token}")

while not S.is_empty():
    output.push(S.pop())
final_output = LinkedStack()

while not output.is_empty():
    final_output.push(output.pop())
print("Postfix Expression: ", end="")

while not final_output.is_empty():
    print(final_output.pop(), end=" ")

print()

'''========================================= POSITIONAL LIST============================================'''
P = PositionalList()
P.add_last(1)
P.add_last(72)
P.add_last(81)
P.add_last(25)
P.add_last(65)
P.add_last(91)
P.add_last(11)

def insertion_sort(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value > marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot


def insertion_sort_descending(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value < marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot
insertion_sort_descending(P)
print("The sorted list of elements are: ")
for x in P:
    print(x, end=' ')
print()

insertion_sort(P)
print("The sorted list of elements are: ")
for x in P:
    print(x, end=' ')
print()