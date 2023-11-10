from math import ceil, log2, inf

'''
Range minimum query implemented using recursive segment tree
'''
class Rmq:
    def __init__(self, A):
        self.N = len(A)
        self.A = A
        x = ceil(log2(self.N))
        x = 2 * (2 ** x) - 1
        self.tree = [0] * x

        self.build(0, 0, self.N - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.A[start]
            return self.A[start]
        
        mid = (start + end) // 2

        self.build(2 * node + 1, start, mid)

        self.tree[node] = min(self.build(node * 2 + 1, start, mid), self.build(node * 2 + 2, mid + 1, end))

        return self.tree[node]
    
    def range_min(self, l, r):
        return self._range_min(0, 0, self.N - 1, l, r)
    
    def _range_min(self, node, L, R, l, r):
        if l > R or r < L:
            return inf
        
        if l <= L and r >= R:
            return self.tree[node]
        
        mid = (L + R) // 2

        return min(self._range_min(2 * node + 1, L, mid, l, r), self._range_min(2 * node + 2, mid + 1, R, l, r))