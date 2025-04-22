from collections import deque

def dfs_uninformed(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path

        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


def bfs_uninformed(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

# main
graph = {}
num_nodes = int(input("Enter number of nodes: "))

print("Enter node names:")
nodes = [input(f"Node {i+1}: ").strip() for i in range(num_nodes)]

print("\nEnter adjacency list (comma-separated neighbors for each node):")
for node in nodes:
    neighbors = input(f"{node}: ").strip()
    graph[node] = [neighbor.strip() for neighbor in neighbors.split(',')] if neighbors else []

start = input("\nEnter start node: ").strip()
goal = input("Enter goal node: ").strip()

BFS = bfs_uninformed(graph, start, goal)
print("\nBFS Path:", BFS if BFS else "No path found.")

DFS = dfs_uninformed(graph, start, goal)
print("\nDFS Path:", DFS if DFS else "No path found.")
