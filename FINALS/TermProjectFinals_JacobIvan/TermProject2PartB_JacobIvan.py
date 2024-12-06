from LinkedBinaryTree import LinkedBinaryTree as Tree
print("Matrix 1:")
tree7 = Tree()

root = tree7._add_root('r')
node_a = tree7._add_left(root, 'a')
node_b = tree7._add_left(node_a, 'b')
node_c = tree7._add_right(node_a, 'c')
node_d = tree7._add_right(node_b, 'd')
node_e = tree7._add_left(node_c, 'e')
node_f = tree7._add_right(node_c, 'f')
node_g = tree7._add_right(node_e, 'g')
node_h = tree7._add_right(node_g, 'h')

print("Inorder traversal: ", end=" ")
for i in tree7.inorder():
    print(i.element(), end=" ")
print()

print("Preorder traversal: ", end=" ")
for i in tree7.positions():
    print(i.element(), end=" ")
print()

print("Postorder traversal: ", end=" ")
for i in tree7.postorder():
    print(i.element(), end=" ")
print()
print()

print("Matrix 2:")
tree8 = Tree()

root = tree8._add_root('r')
node_a = tree8._add_left(root, 'a')
node_b = tree8._add_right(root, 'b')
node_c = tree8._add_left(node_a, 'c')
node_d = tree8._add_right(node_a, 'd')
node_e = tree8._add_right(node_b, 'e')
node_f = tree8._add_right(node_e, 'f')
node_g = tree8._add_right(node_f, 'g')

print("Inorder traversal: ", end=" ")
for i in tree8.inorder():
    print(i.element(), end=" ")
print()

print("Preorder traversal: ", end=" ")
for i in tree8.positions():
    print(i.element(), end=" ")
print()

print("Postorder traversal: ", end=" ")
for i in tree8.postorder():
    print(i.element(), end=" ")
print()
print()

print("Matrix 3:")
tree9 = Tree()

root = tree9._add_root('r')
node_a = tree9._add_left(root, 'a')
node_b = tree9._add_right(root, 'b')
node_c = tree9._add_right(node_a, 'c')
node_d = tree9._add_left(node_b, 'd')
node_e = tree9._add_right(node_b, 'e')
node_f = tree9._add_left(node_c, 'f')

print("Inorder traversal: ", end="")
for position in tree9.inorder():
    print(position.element(), end=" ")
print()

print("Preorder traversal: ", end="")
for position in tree9.positions():
    print(position.element(), end=" ")
print()

print("Postorder traversal: ", end="")
for position in tree9.postorder():
    print(position.element(), end=" ")
print()
print()

print("Matrix 4:")
tree10 = Tree()

root = tree10._add_root('r')
node_a = tree10._add_left(root, 'a')
node_b = tree10._add_right(root, 'b')
node_c = tree10._add_left(node_a, 'c')
node_d = tree10._add_right(node_a, 'd')
node_e = tree10._add_left(node_b, 'e')
node_f = tree10._add_right(node_b, 'f')

node_g = tree10._add_left(node_c, 'g')
node_h = tree10._add_right(node_c, 'h')
node_i = tree10._add_left(node_e, 'i')

print("Inorder traversal: ", end="")
for position in tree10.inorder():
    print(position.element(), end=" ")
print()

print("Preorder traversal: ", end="")
for position in tree10.positions():
    print(position.element(), end=" ")
print()

print("Postorder traversal: ", end="")
for position in tree10.postorder():
    print(position.element(), end=" ")
print()
