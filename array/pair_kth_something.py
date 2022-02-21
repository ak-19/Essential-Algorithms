def kth_smallest_absolute_distance_pair(A, k):
    N = len(A)
    
    def possible(val):
        count = L = 0        
        for R, v in enumerate(A):
            while L < R and A[R] - A[L] > val: L += 1                
            count += R - L        
        return count >= k
    
    A.sort()  
    
    lo, hi = 0, A[-1] - A[0]
    
    while lo < hi:
        mid = (lo + hi) // 2        
        if possible(mid): hi = mid
        else: lo = mid + 1
        
    return lo

from heapq import heappop, heappush

def k_smallest_sums_pairs(A, B, k):
    seen = set()
    result = []
    N1 = len(A)
    N2 = len(B)
    pq = [(A[0]+ B[0], 0, 0)]
    
    while len(result) < k and pq:
        v, i1, i2 = heappop(pq)
        result.append((A[i1], B[i2]))
        
        for i, j in [(i1 + 1, i2), (i1, i2 + 1)]:
            if i < N1 and j < N2 and (i, j) not in seen:
                heappush(pq, (A[i]+B[j], i, j))
                seen.add((i, j))
    
    return result    