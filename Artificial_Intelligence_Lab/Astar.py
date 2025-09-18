from queue import PriorityQueue

# Example graph
graph = {
    'Home': {'Bank': 45, 'Garden': 40, 'School': 50},
    'Bank': {'Police': 60},
    'Garden': {'Railway': 72},
    'School': {'Post': 59, 'Railway': 75},
    'Police': {'University': 28},
    'Post': {},
    'Railway': {'University': 40},
    'University': {}
}

# Corrected heuristic values
heuristics = {
    'Home': 120, 'Bank': 80, 'Garden': 100,
    'School': 70, 'Railway': 20, 'Post': 110, 'Police': 26, 'University': 0
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
start, goal = 'Home', 'University'
path, cost = a_star_search(start, goal)
print("Optimal Path:", path)
print("Total Cost:", cost)

