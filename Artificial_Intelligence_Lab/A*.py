import heapq

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

def a_star_search(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, [start]))  # (f, g, node, path)
    closed_set = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            return path, g  # return path and cost

        if node in closed_set:
            continue
        closed_set.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in closed_set:
                g_new = g + cost
                f_new = g_new + heuristics[neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float("inf")  # if no path found

# Run A*
start, goal = 'S', 'G'
path, cost = a_star_search(graph, heuristics, start, goal)

print("Optimal Path:", path)
print("Total Cost:", cost)

