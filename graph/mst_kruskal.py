from union_find import UnionFind

def mst_2d_points(p):
    N = len(p)
    e = []
    uf = UnionFind(N)
    for i in range(N):
        x, y = p[i]
        for j in range(i + 1, N):
            xx, yy = p[j]
            e.append((abs(x - xx) + abs(y - yy), i, j))
    e.sort()
    mst = 0
    for w, a, b in e:
        if not uf.connected(a, b):
            mst += w
            uf.union(a, b)
    return mst