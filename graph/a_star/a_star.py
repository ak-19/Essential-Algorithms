import heapq

def a_star(graph, start, goal, h):
    """
    A* algorithm implementation. for 2D grid, using manhattan distance as heuristic function
    
    Parameters
    ----------
    graph : dict
        A weighted graph given as a dictionary of adjacency lists
    start : node
        The node to start the search from
    goal : node
        The node to search for
    h : function(node, node) -> float
        A heuristic function that estimates the cost from a given node to the goal.
        In this case manhattan distance
    
        distance is:
            f(n) = g(n) + h(n)
        g(n): The actual cost from the start node to the current node n.
        h(n): A heuristic estimate of the cost from node n to the goal. 
        This is where A* shines by allowing you to estimate remaining distance efficiently.
        f(n): Total estimated cost of the path through node n to the goal. 
    Returns
    -------
    list
        The path from the start node to the goal node, or None if no path is found
    """
    open_set = []
    heapq.heappush(open_set, (0, start))  # Priority queue (f-score, node)
    
    came_from = {}  # Tracks the path
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = h(start, goal)
    
    while open_set:
        # Get node with lowest f(n)
        current_f, current = heapq.heappop(open_set)
        
        # If we reached the goal
        if current == goal:
            return reconstruct_path(came_from, current)
        
        # Explore neighbors
        for neighbor, distance in graph[current].items():
            tentative_g_score = g_score[current] + distance
            
            if tentative_g_score < g_score[neighbor]:
                # This path to neighbor is the best so far
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor, goal)
                
                # Add to open set if not already present
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # No path found

# Helper function to reconstruct the path
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# Example heuristic (Manhattan distance)
def heuristic(node, goal):
    (x1, y1) = node
    (x2, y2) = goal
    return abs(x1 - x2) + abs(y1 - y2)

# Example graph (grid with distances)
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1, (0, 2): 1},
    (0, 2): {(0, 1): 1, (1, 2): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
    (1, 1): {(1, 0): 1, (0, 1): 1, (1, 2): 1, (2, 1): 1},
    (1, 2): {(1, 1): 1, (0, 2): 1, (2, 2): 1},
    (2, 0): {(1, 0): 1, (2, 1): 1},
    (2, 1): {(2, 0): 1, (1, 1): 1, (2, 2): 1},
    (2, 2): {(2, 1): 1, (1, 2): 1}
}

# Running the algorithm
start = (0, 0)
goal = (2, 2)
path = a_star(graph, start, goal, heuristic)

print("Path found by A*:", path)
