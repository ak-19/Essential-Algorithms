class SegmentTree:
    def __init__(self, N, update_compare, query_compare):
        self.N = N
        self.H = 1
        while 1 << self.H < N:
            self.H += 1

        self.update_compare = update_compare
        self.query_compare = query_compare
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def apply(self, index, val):
        self.tree[index] = self.update_compare(self.tree[index], val)
        if index < self.N: self.lazy[index] = self.update_compare(self.lazy[index], val)

    def pull(self, index):
        while index > 1:
            index /= 2
            self.tree[index] = self.query_compare(self.tree[index*2], self.tree[index*2 + 1])
            self.tree[index] = self.update_compare(self.tree[index], self.lazy[index])

    def push(self, index):
        for h in range(self.H, 0, -1):
            real_index = index >> h
            if self.lazy[real_index]:
                self.apply(real_index * 2, self.lazy[real_index])
                self.apply(real_index * 2+ 1, self.lazy[real_index])
                self.lazy[real_index] = 0

    def update(self, L, R, h):
        L += self.N
        R += self.N
        L2, R2 = L, R
        while L <= R:
            if L & 1:
                self.apply(L, h)
                L += 1
            if R & 1 == 0:
                self.apply(R, h)
                R -= 1
            L /= 2; R /= 2
        self.pull(L2)
        self.pull(R2)

    def query(self, L, R):
        L += self.N
        R += self.N
        self.push(L); self.push(R)
        ans = 0
        while L <= R:
            if L & 1:
                ans = self.query_compare(ans, self.tree[L])
                L += 1
            if R & 1 == 0:
                ans = self.query_compare(ans, self.tree[R])
                R -= 1
            L /= 2; R /= 2
        return ans