class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_after(self, value, data):
        current = self.head
        while current is not None:
            if current.data == value:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        return False

    def delete(self, value):
        if self.head is None:
            return False
        
        # If the head node itself holds the value to be deleted
        if self.head.data == value:
            self.head = self.head.next
            return True
            
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def search(self, value):
        current = self.head
        position = 0
        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage
linked_list = SinglyLinkedList()
linked_list.insert_at_end(20)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

print("Initial List:")
linked_list.display()

linked_list.insert_at_beginning(5)
print("\nAfter inserting 5 at beginning:")
linked_list.display()

linked_list.insert_after(20, 25)
print("\nAfter inserting 25 after 20:")
linked_list.display()

linked_list.delete(20)
print("\nAfter deleting 20:")
linked_list.display()

print("\nSearching for 30:")
print("Position:", linked_list.search(30))
