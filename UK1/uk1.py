# Struktur data pohon
graph = {
    'S': {'A': 4, 'B': 4, 'C': 3},
    'A': {'D': 4, 'E': 3, 'F': 3},
    'B': {'G': 2},
    'C': {'H': 3, 'I': 2},
    'D': {},
    'E': {'J': 4, 'K': 4},
    'F': {},
    'G': {'L': 5, 'M': 5},
    'H': {},
    'I': {'N': 3, 'O': 2},
    'J': {},
    'K': {},
    'L': {},
    'M': {},
    'N': {},
    'O': {},
}

# Generate and Test
def generate_and_test(graph, start, goal):
    visited = []
    path = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            print(f"Visiting {node}")
            if node == goal:
                path.append(node)
                return path
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    path.append(node)
    return None

# Breadth First Search
from collections import deque

def bfs(graph, start, goal):
    visited = []
    path = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            print(f"Visiting {node}")
            if node == goal:
                path.append(node)
                return path
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    path.append(node)
    return None

print("Generate and Test:")
print(generate_and_test(graph, 'S', 'K'))

print("\nBreadth First Search:")
print(bfs(graph, 'S', 'K'))
