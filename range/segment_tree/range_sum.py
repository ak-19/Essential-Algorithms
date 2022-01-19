class RangeSum:
    def __init__(self, A):
        self.N = len(A)
        self.tree = [0] * (self.N * 2)
        self.build_tree(A)
        
    def build_tree(self, A):
        i = 0     
        for ti in range(self.N, 2 * self.N):
            self.tree[ti] = A[i]
            i += 1
            
        for i in range(self.N - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
                    
    def update(self, index: int, val: int) -> None:
        index += self.N
        self.tree[index] = val
        while index > 0:
            L = R = index
            if index % 2 == 0: R += 1
            else: L -= 1                
            self.tree[index // 2] = self.tree[L] + self.tree[R]            
            index //= 2
                                    
    def sumRange(self, left: int, right: int) -> int:
        L = left + self.N
        R = right + self.N
        
        total = 0
        
        while L <= R:
            if L % 2:
                total += self.tree[L]
                L += 1
            if R % 2 == 0:
                total += self.tree[R]
                R -= 1
            L //= 2
            R //= 2
        
        return total