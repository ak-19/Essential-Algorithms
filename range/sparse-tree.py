from typing import List

class SparseTable:
    def __init__(self, arr: List[int], op):
        """Builds a sparse table for idempotent op = max/min over arr."""
        self.n = len(arr)
        self.op = op
        self.log = [0]*(self.n+1)
        for i in range(2, self.n+1):
            self.log[i] = self.log[i//2] + 1
        K = self.log[self.n] + 1
        self.st = [arr[:]]  # st[0] is length-1 intervals
        j = 1
        while j < K:
            prev = self.st[j-1]
            size = 1 << (j-1)
            cur = [self.op(prev[i], prev[i+size]) for i in range(self.n - (1<<j) + 1)]
            self.st.append(cur)
            j += 1

    def query(self, L: int, R: int) -> int:
        """Inclusive range query in O(1)."""
        j = self.log[R - L + 1]
        return self.op(self.st[j][L], self.st[j][R - (1<<j) + 1])
    

# example usage
st_max = SparseTable([2,3,4,1,2], max)
st_min = SparseTable([1,2,1,2,1], min)