from collections import defaultdict
from heapq import heappop, heappush
from sortedcontainers import SortedList as bst

class MinOperationsToMakeKEqualBst:
    def __init__(self):
        self.left, self.left_sum = bst(), 0
        self.right, self.right_sum = bst(), 0
        self.total = 0

    def balance(self):
        if len(self.left) > len(self.right) + 1:
            v = self.left.pop()
            self.left_sum -= v
            self.right.add(v)
            self.right_sum += v
        elif len(self.left) < len(self.right):
            v = self.right.pop(0)
            self.right_sum -= v
            self.left.add(v)
            self.left_sum += v

    def add(self, v):
        self.total += v
        if not self.left or  self.left[-1] >= v:
            self.left.add(v)
            self.left_sum += v
        else:
            self.right.add(v)
            self.right_sum += v            

        self.balance()

    def remove(self, v):
        if not self.left or self.left[-1] >= v:
            self.left.remove(v)
            self.left_sum -= v
        else:
            self.right.remove(v)
            self.right_sum -= v          
        
        self.balance()

    def cost(self):
        if len(self.left) == 0:
            return 0
        if len(self.right) == 0:
            return self.total - self.left_sum

        left_cost = len(self.left) * self.left[-1] - self.left_sum
        right_cost = self.right_sum - len(self.right) * self.left[-1]
        return left_cost + right_cost


class SlidingWindowEqualizer:
    def __init__(self, A, k, balancer_provider):
        self.k = k
        moe = balancer_provider()
        cost = []
        for i in range(k):
            moe.add(A[i])
        cost.append(moe.cost())

        for i in range(k, len(A)):
            moe.remove(A[i-k])    
            moe.add(A[i])
            cost.append(moe.cost())
        self.cost = cost        

# print(SlidingWindowEqualizer([15, 3, 8, 6, 2, 9, 1, 7, 4, 10, 12, 14, 11, 13, 15, 18, 16, 17, 19, 20], 4, MinOperationsToMakeKEqualBst).cost)
# print(SlidingWindowEqualizer([12, 3, 31, 1, 43, 12, 11, 21, 11 ], 4, MinOperationsToMakeKEqualBst).cost)