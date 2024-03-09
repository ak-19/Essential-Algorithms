from math import inf

def bellman_ford(graph, source):
    num_vertices = len(graph)
    distances = [inf] * num_vertices
    distances[source] = 0

    # Relax edges repeatedly 
    for _ in range(num_vertices - 1):
        for u, v, weight in graph:  
            if distances[u] != inf and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative-weight cycles
    for u, v, weight in graph:
        if distances[u] != inf and distances[u] + weight < distances[v]:
            print("Graph contains negative weight cycle")
            return

    return distances