class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

#UnionFind variation where size of component, not rank, matters!
class UF:
    def __init__(self, N) -> None:
        self.p = list(range(N))
        self.size = [1] * N

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def connect(self, x, y):
        px = self.find(self.p[x])
        py = self.find(self.p[y])

        if px != py:
            self.p[py]= self.p[px]
            self.size[px] += self.size[py]

    def get_size(self, x):
        return self.size[x]