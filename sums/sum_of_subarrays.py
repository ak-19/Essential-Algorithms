from typing import List

def sum_of_all_subarrays(A: List[int]) -> int:
    """
    :type A: List[int]
    :rtype: int
    The idea is to calculate the contribution of each element in the array. 
    Each element A[i] appears in (i + 1) * (n - i) subarrays. 
    For example, if the array is [1, 2, 3], A[0] appears in 3 subarrays [1], [1, 2], [1, 2, 3]. 
    A[1] appears in 2 subarrays [2], [2, 3]. A[2] appears in 1 subarray [3]. 
    So the contribution of A[0] is 1 * 3 = 3, A[1]'s contribution is 2 * 2 = 4, A[2]'s contribution is 3 * 1 = 3.
    The total sum of all subarray is 3 + 4 + 3 = 10.
    """""""""    
    total_sum = 0
    n = len(A)    
    for i in range(n):
        contribution = A[i] * (i + 1) * (n - i)
        total_sum += contribution    
    return total_sum