def twoSumLessThanK(A, k):
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

print(twoSumLessThanK([1,2,3,4,5,6,7,8,9,10], 15))