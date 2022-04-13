from typing import  List
from bisect import bisect_left, bisect_right

def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:        
    qs = sorted(set(queries))
    
    N = len(queries)
    
    result = [-1] * N
    
    parent = list(range(N + 1))
    
    intervals.sort(key = lambda x: x[1] - x[0])
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
            
    val_map = {v:i for i, v in enumerate(qs)}
    
    for s, e in intervals:
        L, R = bisect_left(qs, s), bisect_right(qs, e)
        
        val = find(L)
        
        while val < R:
            result[val] = e-s+1
            parent[val] = val + 1
            val = find(val)

    return [result[val_map[q]] for q in queries]

print(minInterval([[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]) == [3,3,1,4])