def max_sliding_windows(A, k):
    N = len(A)      
    
    if N == 1: return A
    if N * k  == 0: return []
    
    L = [A[0]]        
    R = [0] * N
    R[-1] = A[-1]
    
    for i in range(1, N): 
        if i % k == 0:
            L.append(A[i])
        else:
            L.append(max(A[i], L[-1]))
            
    for i in range(N - 2, -1, -1):
        if i % k == 0:
            R[i] = A[i]
        else:            
            R[i] = max(A[i], R[i + 1])
        
    return [max(R[i] , L[i + k - 1]) for i in range(N - k + 1)]