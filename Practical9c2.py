social_network = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

visited = set()

def find_connections(person):
    visited.add(person)
    print(person, end=" ")

    for friend in social_network[person]:
        if friend not in visited:
            find_connections(friend)


print("People connected to A:")
find_connections("A")