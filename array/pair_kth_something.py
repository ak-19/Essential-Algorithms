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