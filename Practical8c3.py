# Job Scheduling using Priority Queue

import heapq

jobs = []

# Add jobs
heapq.heappush(jobs, (2, "Job A"))
heapq.heappush(jobs, (1, "Job B"))
heapq.heappush(jobs, (3, "Job C"))
heapq.heappush(jobs, (1, "Job D"))

print("Job Execution Order:")

while jobs:
    priority, job = heapq.heappop(jobs)
    print("Priority:", priority, "->", job)