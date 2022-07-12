from math import sqrt

class Decomposer:
    def __init__(self, A):
        self.A = A
        self.N = len(A)
        self.block = []
        block_index = -1
        block_size = int(sqrt(self.N))
        self.block_size = block_size
        for i in range(self.N):
            if i % block_size == 0:
                block_index += 1
            if block_index == len(self.block):
                self.block.append(0)
            self.block[block_index] += A[i]

    def update(self, index, val):
        if index < 0 or index >= self.N: return 0        
        block_index = index // self.block_size
        self.block[block_index] += val - self.A[index]
        self.A[index] = val

    def query(self, l, r):
        if l > r or l < 0 or r >= self.N: return 0
        l_index = l // self.block_size
        r_index = r // self.block_size

        result = sum(self.block[l_index+1:r_index])

        for i in range(l, (l_index + 1) * self.block_size):
            result += self.A[i]

        for i in range(r_index * self.block_size, r + 1):
            result += self.A[i]

        return result

