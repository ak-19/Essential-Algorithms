import math
def verifyPreorderWithStack(preorder):
    stack = []
    min_val = -math.inf
    
    for val in preorder:
        if val <= min_val:
            return False
        while stack and stack[-1] < val:
            min_val = stack.pop()
        stack.append(val)
    return True

def verifyPreorder(preorder):
    lo = -math.inf
    hi = -math.inf

    for i, val in enumerate(preorder):
        if val <= lo:
            return False
        if val > hi:
            lo = hi
            hi = val
        else:
            j = i - 1
            while j >= 0 and val > preorder[j]:
                lo = preorder[j] 
                j -= 1 
    return True

class Solution:
    def __init__(self):
        self.index = 0
    def verifyPreorder(self, P, lo=-math.inf, hi=math.inf):
        if self.index == len(P) or P[self.index] > hi: return True
        
        self.index, mid = self.index + 1, P[self.index]
        
        return lo < mid and self.verifyPreorder(P, lo, mid) and self.verifyPreorder(P, mid, hi)