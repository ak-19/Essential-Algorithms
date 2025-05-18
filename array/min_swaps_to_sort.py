from typing import List

def min_swaps_to_sort(A: List[int]) -> int:
    """
    Calculate the minimum number of swaps required to sort an array.

    This function implements an efficient algorithm based on cycle detection.
    It finds all cycles in the permutation and calculates the minimum swaps
    needed to sort the array by breaking these cycles.

    Args:
        A (List[int]): The input array of integers to be sorted.

    Returns:
        int: The minimum number of swaps required to sort the array.

    Example:
        >>> min_swaps_to_sort([4, 3, 2, 1])
        2
        >>> min_swaps_to_sort([1, 5, 4, 3, 2])
        2
    """

    n = len(A)
    
    # Create a list of tuples (index, value) and sort by value
    # This helps us track the original positions of elements
    vi = list(enumerate(A))
    vi.sort(key=lambda x: x[1])
    
    # Track visited elements to avoid counting cycles multiple times
    visited = [False] * n
    swaps = 0
    
    # Iterate through all elements
    for i in range(n):
        # If element is not visited and is not in its correct position
        if not visited[i] and vi[i][0] != i:
            # Count the size of this cycle
            cycle_size = 0
            j = i
            
            # Traverse the cycle
            while not visited[j]:
                visited[j] = True
                j = vi[j][0]
                cycle_size += 1
            
            # Add the number of swaps needed for this cycle
            # A cycle of size k needs k-1 swaps to be sorted
            swaps += max(0, cycle_size - 1)
    
    return swaps