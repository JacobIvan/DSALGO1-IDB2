from ArrayStack import ArrayStack as Stack


def reversefile(fileloc):
    stack = Stack()
    with open(fileloc, 'r') as file:
        for line in file:
            stack.push(line.rstrip('\n'))
    with open(fileloc, 'w') as file:
        while not stack.is_empty():
            file.write(stack.pop() + '\n')


def balance(expr):
    correct_pair = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in correct_pair.values():
            S.push(char)
        elif char in correct_pair.keys():
            if S.is_empty() or S.pop() != correct_pair[char]:
                return False
    return S.is_empty()


S = Stack()
userinput = input("Enter an arithmetic expression: ")
if balance(userinput):
    print("The symbols are balanced.")
else:
    print("The symbols are not balanced.")

reversefile(r"Z:\DSALGO1-IDB2\MIDTERMS\Text.txt")



