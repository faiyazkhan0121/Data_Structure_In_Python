# Priority Queue using Min Heap

import heapq

priority_queue = []

# Add tasks
heapq.heappush(priority_queue, (2, "Complete Assignment"))
heapq.heappush(priority_queue, (1, "Attend Exam"))
heapq.heappush(priority_queue, (3, "Read Book"))
heapq.heappush(priority_queue, (1, "Submit Project"))

print("Tasks according to priority:")

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print("Priority:", priority, "Task:", task)