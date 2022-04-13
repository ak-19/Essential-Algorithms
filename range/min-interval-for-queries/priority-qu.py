from typing import List
from collections import defaultdict
from heapq import heappop, heappush

def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:        
    ints = [] 
    val_map = defaultdict(lambda: -1)        
    intervals.sort()
    i = 0
    for q in sorted(queries):
        
        while i < len(intervals) and intervals[i][0] <= q:
            s, e = intervals[i]
            heappush(ints, (e - s + 1, e))
            i += 1
                    
        while ints and ints[0][1] < q: 
            heappop(ints)
    
        val_map[q] = ints[0][0] if ints else -1

    return [val_map[q] for q in queries]

print(minInterval([[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]) == [3,3,1,4])