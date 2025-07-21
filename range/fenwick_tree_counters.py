from collections import Counter

class FenwickTreeCounter:
    """
    Fenwick Tree (Binary Indexed Tree) 
    used as a count of k values in a range
    input: int max value allowed, must be small enough to fit in memory a array length of max_val + 1    
    """
    def __init__(self, A):
        N = len(A)
        self.N = len(A)
        self.A = A        
        self.tree = [Counter() for _ in range(N + 1)]
        for idx, val in enumerate(self.A): self._add(idx, val)
 
    def _add(self, idx, val):
        i = idx + 1
        while i <= self.N:
            self.tree[i][val] += 1
            i += i & -i

    def _remove(self, idx, val):
        i = idx + 1
        while i <= self.N:
            self.tree[i][val] -= 1
            if self.tree[i][val] == 0:
                del self.tree[i][val]
            i += i & -i
            
    def update(self, idx, new_val):
        if self.A[idx] != new_val:
            self._remove(idx, self.A[idx])
            self.A[idx] = new_val
            self._add(idx, new_val)
    
    def get_val(self, i, k):
        i, s = i + 1, 0
        while i > 0:
            s += self.tree[i][k]
            i -= (i & -i)            
        return s
    
    def get_range(self, i, j, k):
        return self.get_val(j, k) - self.get_val(i - 1, k)    

    def sumRange(self, left: int, right: int, k) -> int:
        return self.get_range(left, right, k)