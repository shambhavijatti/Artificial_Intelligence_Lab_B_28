from queue import PriorityQueue

# Example graph
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'D': 12},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 7},
    'D': {'G': 2},
    'G': {}
}

# Heuristic values
heuristics = {
    'S': 7, 'A': 6, 'B': 4,
    'C': 2, 'D': 1, 'G': 0
}

def a_star_search(start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    g_cost = {start: 0}
    parent = {start: None}

    while not open_list.empty():
        f, current = open_list.get()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], g_cost[goal]

        for neighbor, cost in graph[current].items():
            tentative_g = g_cost[current] + cost
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristics[neighbor]
                open_list.put((f_cost, neighbor))
                parent[neighbor] = current

    return None, float("inf")

# Run A*
start, goal = 'S', 'G'
path, cost = a_star_search(start, goal)
print("Optimal Path:", path)
print("Total Cost:", cost)

