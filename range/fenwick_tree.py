class FenwickTree:
    def __init__(self, A) -> None:
        N = len(A)
        self.N = len(A)
        self.tree = [0] * (N + 1)
        for i in range(N): self.update(i, A[i])
                
    def get_range(self, i, j):
        return self.get_val(j) - self.get_val(i - 1)

    def get_val(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]               
            i -= (i & -i)            
        return s

    def update(self, i, val):
        i += 1
        while i <= self.N:
            self.tree[i] += val
            i += (i & -i)
          
t = FenwickTree([1,0,2,1,1,3,0,4,2,5,2,2,3,1,0,2])

print(t.get_range(0,3))
print(t.get_range(2,5))
print(t.get_range(3,11))

