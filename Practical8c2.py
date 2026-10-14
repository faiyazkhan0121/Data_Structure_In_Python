# Patient Triage using Priority Queue

import heapq

patients = []

# Add patients
heapq.heappush(patients, (1, "Patient A - Critical"))
heapq.heappush(patients, (3, "Patient B - Normal"))
heapq.heappush(patients, (2, "Patient C - Serious"))
heapq.heappush(patients, (1, "Patient D - Critical"))

print("Patient Treatment Order:")

while patients:
    priority, patient = heapq.heappop(patients)
    print("Priority:", priority, "->", patient)