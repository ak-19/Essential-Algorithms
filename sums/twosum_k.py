def twoSumLessThanKCountSort(A, k):
    best = -1
    N = len(A)
    t = [0] * 1001
    
    for v in A: t[v] += 1
    lo, hi = 1, 1000
    
    while lo <= hi:
        if t[hi] == 0 or lo + hi >= k:
            hi -= 1
        else:
            if t[lo] > (0 if lo < hi else 1):
                best = max(best, lo+hi)
            lo += 1
    
    return best


def twoSumLessThanK2Pointer(A, k):
    best = -1
    N = len(A)
    A.sort()
    lo, hi = 0, N - 1
    
    while lo < hi:
    
        s = A[lo] + A[hi] 
        if s > 0 and s < k and s > best:
            best = s
        if s >= k:
            hi -= 1
        else:
            lo += 1
    
    return best

from bisect import bisect_left

def twoSumLessThanKBisect(A, k):
    best = -1
    N = len(A)
    A.sort()
    
    for i in range(N):
        j = bisect_left(A, k- A[i], i) - 1
        if j > i:
            s = A[i] + A[j] 
            if s > 0 and s < k and s > best:
                best = s
    
    return best

class BinarySearchSolution:
    def search(self, A, lo, v, k):
        hi = len(A) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            s = v + A[mid]
            if s == k:
                return mid
            if s < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
            
    def twoSumLessThanK(self, A, k):
        best = -1
        N = len(A)
        A.sort()
        
        for i in range(N):
            j = self.search(A, i, A[i], k) - 1
            if j > i:
                s = A[i] + A[j] 
                if s > 0 and s < k and s > best:
                    best = s
        
        return best

print(twoSumLessThanKCountSort([1,2,3,4,5,6,7,8,9,10], 15))
print(twoSumLessThanK2Pointer([1,2,3,4,5,6,7,8,9,10], 15))
print(twoSumLessThanKBisect([1,2,3,4,5,6,7,8,9,10], 15))
print(BinarySearchSolution().twoSumLessThanK([1,2,3,4,5,6,7,8,9,10], 15))