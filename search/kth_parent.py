# k-th parent via binary lifting

class KthAncester:
    def __init__(self, n: int, parent):
        self.parent = [[-1] * 30 for _ in range(n)]
        for i in range(n): self.parent[i][0] = parent[i] 
        for pp in range(1, 30):
            for i in range(n):
                if self.parent[i][pp-1] == -1:
                     self.parent[i][pp] = -1
                else:
                    self.parent[i][pp] = self.parent[self.parent[i][pp - 1]][pp-1]        
        self.n = n               
    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(30):
            if (k >> i) & 1:
                node = self.parent[node][i]
                if node == -1: return -1        
        return node