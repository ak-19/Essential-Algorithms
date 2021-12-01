from typing import List

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from itertools import combinations, permutations
import math

class Solution:
    def findNumberOfLIS(self, A: List[int]) -> int:
        N = len(A)     
        lis = []
        frequency_of_this_length = defaultdict(list)
        frequency_of_this_length[-1].append((1, -math.inf))
        
        max_len = 1

        for val in A:
            
            length = bisect_left(lis, val)

            if length >= len(lis): 
                lis.append(val)
            else: 
                lis[length] = val

            curr_lis_count = 0
            

            for count, a in frequency_of_this_length[length-1]:
                if val > a: 
                    curr_lis_count += count
            
            frequency_of_this_length[length].append((curr_lis_count, val))
            
            max_len = max(max_len, length)
       
        if len(lis) == 1: return N
        
        return sum(count for count, _ in frequency_of_this_length[max_len])

print(Solution().findNumberOfLIS([1,3,5,4,7]) == 2)
print(Solution().findNumberOfLIS([2,2,2,2,2]) == 5)
print(Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]) == 3)
print(Solution().findNumberOfLIS([1,3,2]) == 2)
print(Solution().findNumberOfLIS([3,1,2]) == 1)
print(Solution().findNumberOfLIS([1,1,1,2,2,2,3,3,3]) == 27)

