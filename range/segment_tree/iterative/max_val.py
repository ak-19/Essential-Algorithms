class MaxSegmentTree:
    def __init__(self, N):
        self.N = N
        self.tree = [0] * 2 * self.N
       
    def max_range(self, L, R):
        L += self.N
        R += self.N
        ans = 0
        while L < R:
            if L & 1:
                ans = max(ans, self.tree[L])
                L += 1
            if R & 1:
                R -= 1
                ans = max(ans, self.tree[R])
            L >>= 1
            R >>= 1
        return ans
    
    def update(self, index, val):
        index += self.N
        self.tree[index] = val
        while index > 1:
            index >>= 1
            self.tree[index] = max(self.tree[index * 2], self.tree[index * 2 + 1])