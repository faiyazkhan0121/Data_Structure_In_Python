
# Min Heap

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent = (index - 1) // 2

        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = \
                self.heap[parent], self.heap[index]

            index = parent
            parent = (index - 1) // 2

    def display(self):
        print("Min Heap:", self.heap)


# Main Program
h = MinHeap()

values = [40, 20, 30, 10, 50, 15]

for value in values:
    h.insert(value)

h.display()