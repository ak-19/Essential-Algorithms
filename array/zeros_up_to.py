from typing import List

def count_zeros_before(A: List[int]) -> List[int]:     
    """
    Given the array consisting of 1 and 0 (ones and zeros),
    calculates number of zeros appearing before each index that has 1 (one) value
    returs: List of tuples (index, number of zeros before index)
    """
    N = len(A)
    m = [0] * N
    one_indices = [i for i in range(N) if A[i] == 1]
    return [(index, index-count) for count, index in enumerate(one_indices)]