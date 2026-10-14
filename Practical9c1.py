# Graph for Mapping Routes

graph = {
    "Mumbai": ["Pune", "Nashik"],
    "Pune": ["Mumbai", "Satara"],
    "Nashik": ["Mumbai", "Aurangabad"],
    "Satara": ["Pune"],
    "Aurangabad": ["Nashik"]
}

print("Available Routes:")

for city in graph:
    print(city, "->", graph[city])

print("\nRoute from Mumbai:")

visited = set()

def explore(city):
    visited.add(city)
    print(city, end=" ")

    for next_city in graph[city]:
        if next_city not in visited:
            explore(next_city)

explore("Mumbai")