# minimum height tree roots
# Given a graph, find the minimum height tree roots.
def mht(n, edges):
    if n <= 2: return list(range(n))

    g = [set() for _ in range(n)]
    
    for u, v in edges:
        g[u].add(v)
        g[v].add(u)

    leaves = [i for i in range(n) if len(g[i]) == 1]

    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = g[leaf].pop()
            g[neighbor].remove(leaf)
            if len(g[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves

    return leaves