def patch_array(A, n):    
    '''
    Given array A, find number of missing numbers that are needed to 
    construct continious sequence of numbers in range [1,n] 
    '''            
    patches = 0
    i = 0
    miss = 1
    
    while miss <= n:        
        if i < len(A) and A[i] <= miss:
            miss += A[i]
            i += 1            
        else:
            miss += miss
            patches += 1
    
    return patches