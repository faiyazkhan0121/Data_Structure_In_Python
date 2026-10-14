class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    # Insert (with update check for duplicate keys)
    def insert(self, key, value):
        index = self.hash_function(key)
        
        # Check if key already exists, update if found
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                print("Updated:", key, "->", value)
                return
                
        # Otherwise, append new key-value pair
        self.table[index].append((key, value))
        print("Inserted:", key, "->", value)

    # Search
    def search(self, key):
        index = self.hash_function(key)

        for k, v in self.table[index]:
            if k == key:
                print("Found:", key, "->", v)
                return v

        print("Key not found")
        return None

    # Delete
    def delete(self, key):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                print("Deleted:", key)
                return

        print("Key not found")

    # Display
    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            print(f"{i} : {self.table[i]}")


# Main Program
ht = HashTable(5)

# Insertion
ht.insert(10, "Apple")
ht.insert(15, "Mango")
ht.insert(7, "Banana")
ht.insert(12, "Orange")

ht.display()

# Search
print("\nSearch Operation:")
ht.search(15)

# Delete
print("\nDelete Operation:")
ht.delete(15)

ht.display()