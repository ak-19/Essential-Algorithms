def perm(n, k):
    k_of_p = 1
    for i in range(k): 
        k_of_p *= n
        n -= 1        
    return k_of_p