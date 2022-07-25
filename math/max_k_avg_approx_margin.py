def findMaxAverage(A, k, error_margin):        
    N = len(A)  
    lo, hi = min(A), max(A)
    
    def valid(mid):
        s = minSum = prevSum = 0 
        for i in range(k):
            s += A[i] - mid     
            
        if s >= 0: return True
        
        for i in range(k, N):
            s += A[i] - mid
            prevSum += A[i-k] - mid
            minSum = min(prevSum, minSum)
            
            if s >= minSum: return True

        return False
            
    while hi - lo >  error_margin:
        mid = (lo + hi) *.5            
        if valid(mid): lo = mid
        else: hi = mid
                                                                                                                                
    return lo