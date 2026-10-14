# Graph using Adjacency Matrix

vertices = 5

graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

# Add edges
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (3, 4)
]

for u, v in edges:
    graph[u][v] = 1
    graph[v][u] = 1

print("Adjacency Matrix:")

for row in graph:
    print(row)