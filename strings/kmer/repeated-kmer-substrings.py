def findRepeatedDnaSequencesRK(s, k, alpha='ACGT'):
    cc = lambda x: alpha.index(x)        
    N = len(s)
    
    L = len(alpha)

    if N < k: return []        
    A = [cc(c) for c in s]
    
    seen = set()
    result = set()
    
    hh = 0
    
    #rabin-karpp rolling hash
    for i in range(k): 
        hh = hh * L + A[i]            
    seen.add(hh)
    
    for i in range(1, N - k + 1):
        hh = hh * L + A[i + k - 1] - A[i-1] * (L**k)
        if hh in seen:
            result.add(s[i:i+k])
        else:
            seen.add(hh)
    
    return result   
        
print(findRepeatedDnaSequencesRK('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT', 10))

def findRepeatedDnaSequencesBitmask(s, k):
    cc = lambda x: 'ACGT'.index(x)        
    N = len(s)
    
    if N < k: return []        
    A = [cc(c) for c in s]
    
    seen = set()
    result = set()
    
    bitmask = 0
    
    #rabin-karpp rolling hash
    for i in range(k): 
        bitmask = (bitmask << 2) | A[i]            
    seen.add(bitmask)
    
    for i in range(1, N - k + 1):            
        bitmask = (bitmask << 2) | A[i+k-1]            
        bitmask &= ~(3 << 2 * k)
        
        if bitmask in seen:
            result.add(s[i:i+k])
        else:
            seen.add(bitmask)
    
    return result

print(findRepeatedDnaSequencesBitmask('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT', 10))
