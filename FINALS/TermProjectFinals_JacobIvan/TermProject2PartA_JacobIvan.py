from LinkedBinaryTree import LinkedBinaryTree

def create_tree1():
    tree = LinkedBinaryTree()
    root = tree._add_root('-')
    left = tree._add_left(root, '*')
    tree._add_left(left, 3)
    tree._add_right(left, 5)
    right = tree._add_right(root, '+')
    left_right = tree._add_left(right, '*')
    tree._add_left(left_right, 4)
    tree._add_right(left_right, 5)
    right_right = tree._add_right(right, '-')
    tree._add_left(right_right, 6)
    tree._add_right(right_right, 7)
    return tree

def create_tree2():
    tree = LinkedBinaryTree()
    root = tree._add_root('-')
    left = tree._add_left(root, '*')
    left_left = tree._add_left(left, '+')
    tree._add_left(left_left, 'a')
    tree._add_right(left_left, 'b')
    tree._add_right(left, 'c')
    right = tree._add_right(root, '-')
    tree._add_left(right, 'd')
    tree._add_right(right, 'e')
    return tree

def create_tree3():
    tree = LinkedBinaryTree()
    root = tree._add_root('+')
    left = tree._add_left(root, '+')
    left_left = tree._add_left(left, '^')
    tree._add_left(left_left, 'a')
    tree._add_right(left_left, 'b')
    right_left = tree._add_right(left, '+')
    tree._add_left(right_left, 'c')
    tree._add_right(right_left, 'd')
    right = tree._add_right(root, '/')
    left_right = tree._add_left(right, '*')
    tree._add_left(left_right, 'e')
    tree._add_right(left_right, 'f')
    right_right = tree._add_right(right, '+')
    tree._add_left(right_right, 'g')
    tree._add_right(right_right, 'h')
    return tree

def create_tree4():
    tree = LinkedBinaryTree()
    root = tree._add_root('/')
    left = tree._add_left(root, '+')
    tree._add_left(left, 'a')
    tree._add_right(left, 'b')
    right = tree._add_right(root, '*')
    tree._add_left(right, 'c')
    right_right = tree._add_right(right, '-')
    tree._add_left(right_right, 'd')
    right_right_right = tree._add_right(right_right, '^')
    tree._add_left(right_right_right, 'e')
    tree._add_right(right_right_right, 'f')
    return tree

def create_tree5():
    tree = LinkedBinaryTree()
    root = tree._add_root('*')
    left = tree._add_left(root, '+')
    left_left = tree._add_left(left, '-')
    tree._add_left(left_left, 'a')
    tree._add_right(left_left, 'b')
    tree._add_right(left, 'c')
    right = tree._add_right(root, '*')
    left_right = tree._add_left(right, '+')
    tree._add_left(left_right, 'd')
    tree._add_right(left_right, 'e')
    right_right = tree._add_right(right, '/')
    tree._add_left(right_right, 'f')
    tree._add_right(right_right, 'g')
    return tree

def create_tree6():
    tree = LinkedBinaryTree()
    root = tree._add_root('*')
    tree._add_right(root, 8)

    left = tree._add_left(root, '/')

    num_left = tree._add_left(left, '*')
    tree._add_left(num_left, '+')
    tree._add_right(num_left, '-')
    tree._add_left(tree.left(num_left), 5)
    tree._add_right(tree.left(num_left), 2)
    tree._add_left(tree.right(num_left), 2)
    tree._add_right(tree.right(num_left), 1)

    den_right = tree._add_right(left, '+')
    tree._add_left(den_right, '+')
    tree._add_right(den_right, '-')
    tree._add_left(tree.left(den_right), 2)
    tree._add_right(tree.left(den_right), 9)
    tree._add_left(tree.right(den_right), '-')
    tree._add_right(tree.right(den_right), 1)
    tree._add_left(tree.left(tree.right(den_right)), 7)
    tree._add_right(tree.left(tree.right(den_right)), 2)

    return tree

def print_traversals(tree, tree_num):
    print(f"Traversals for Tree {tree_num}")
    print("Inorder: ", end=" ")
    for node in tree.inorder():
        print(node.element(), end=" ")
    print()

    print("Preorder: ", end=" ")
    for node in tree.positions():
        print(node.element(), end=" ")
    print()

    print("Postorder: ", end=" ")
    for node in tree.postorder():
        print(node.element(), end=" ")
    print()

# Create and print traversals for all trees
trees = [create_tree1(), create_tree2(), create_tree3(), create_tree4(), create_tree5(), create_tree6()]

for i, tree in enumerate(trees, start=1):
    print_traversals(tree, i)
