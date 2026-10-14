# Hash Table using Separate Chaining

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# Main Program
ht = HashTable(5)

ht.insert(10, "Apple")
ht.insert(15, "Mango")
ht.insert(7, "Banana")
ht.insert(12, "Orange")

print("Hash Table:")
ht.display()