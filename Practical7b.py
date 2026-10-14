#Perform and visualize in-order, pre-order, and post-order traversals.
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# In-order: Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Pre-order: Root -> Left -> Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Post-order: Left -> Right -> Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Dataset
data = [50, 30, 70, 20, 40, 60, 80]

# Create BST
root = None

for value in data:
    root = insert(root, value)


# Perform traversals
print("In-order Traversal:")
inorder(root)

print("\nPre-order Traversal:")
preorder(root)

print("\nPost-order Traversal:")
postorder(root)