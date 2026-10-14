#  Use traversal results to derive sorted sequences. 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert data into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# In-order traversal
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)


# Dataset
data = [50, 30, 70, 20, 40, 60, 80]

# Create BST
root = None

for value in data:
    root = insert(root, value)


# Get sorted sequence using In-order traversal
sorted_sequence = []

inorder(root, sorted_sequence)

# Display result
print("Original Dataset:")
print(data)

print("Sorted Sequence:")
print(sorted_sequence)