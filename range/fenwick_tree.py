class FenwickTree:
    def __init__(self, A):
        N = len(A)
        self.N = len(A)
        self.A = A        
        self.tree = [0] * (N + 1)
        for i in range(N): self.construct(i, A[i])
            
    def construct(self, i, val):
        i += 1
        while i <= self.N:
            self.tree[i] += val
            i += (i & -i)    
            
    def update(self, i, val):
        self.construct(i, val - self.A[i])
        self.A[i] = val
    
    def get_val(self, i):
        i, s = i + 1, 0
        while i > 0:
            s += self.tree[i]               
            i -= (i & -i)            
        return s
    
    def get_range(self, i, j):
        return self.get_val(j) - self.get_val(i - 1)    

    def sumRange(self, left: int, right: int) -> int:
        return self.get_range(left, right)
        
          
t = FenwickTree([1,0,2,1,1,3,0,4,2,5,2,2,3,1,0,2])

print(t.get_range(0,3))
print(t.get_range(2,5))
print(t.get_range(3,11))

