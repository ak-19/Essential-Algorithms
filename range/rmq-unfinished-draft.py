import math

class Rmq:
    def __init__(self, A):
        N = len(A)

        log_table = [0] * (N + 1)
        for i in range(2, N + 1): log_table[i] = log_table[i//2] + 1

        L = 2 ** (log_table[-1] - 1)
        rmq = [[math.inf] * L for _ in range(N)]

        for i in range(N):
            min_so_far = math.inf
            for j in range(L):
                index =  i + j
                if index >= N: break
                min_so_far = min(min_so_far, A[index])
                rmq[i][j] = min_so_far


        self.rmq = rmq


a = [1,2,3,4,5,6,7,8,9]

rmq = Rmq(a)

print(rmq)


