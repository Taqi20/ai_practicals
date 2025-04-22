def calculate_heuristic(node):
    heuristic_values = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0  
    }
    return heuristic_values.get(node, float('inf'))

graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('G', 1)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('E', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    'J': []  
}

def a_star_search(start, goal):
    open_list = set([start])      
    closed_list = set()           
    g_cost = {start: 0}           
    parent = {start: None}        

    while open_list:
        current_node = None

        for node in open_list:
            if current_node is None or g_cost[node] + calculate_heuristic(node) < g_cost[current_node] + calculate_heuristic(current_node):
                current_node = node

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            print("Path found:", path)
            return path

        open_list.remove(current_node)
        closed_list.add(current_node)

        for neighbor, cost in graph.get(current_node, []):
            if neighbor in closed_list:
                continue

            tentative_g = g_cost[current_node] + cost

            if neighbor not in open_list:
                open_list.add(neighbor)
            elif tentative_g >= g_cost.get(neighbor, float('inf')):
                continue

            parent[neighbor] = current_node
            g_cost[neighbor] = tentative_g

    print("Path does not exist.")
    return None

a_star_search('A', 'G')
