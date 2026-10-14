# Create a binary search tree (BST) from a dataset. 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to insert a value into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Dataset
data = [50, 30, 70, 20, 40, 60, 80]

# Create BST
root = None

for value in data:
    root = insert(root, value)


print("Binary Search Tree created successfully.")