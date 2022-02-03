def max_n(A, n):
    '''
        Biggest number formed from array of 0-9 digits cponstruncting n digit decimal number, following order in array
    '''
    result = []
    
    for i, v in enumerate(A):
        while result and result[-1] < v and len(result) + len(A) - i > n: result.pop()        
        if len(result) < n: result.append(v)
    
    return result