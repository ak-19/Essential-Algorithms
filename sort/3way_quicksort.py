from random import randint

def sortArray(A):  
    """
    Sorts an array in-place using the 3-way quicksort algorithm.

    Parameters:
        A (List[int]): The array to be sorted.

    Returns:
        List[int]: The sorted array.

    Algorithm:
        1. Partition the array into three parts: elements less than the pivot, elements equal to the pivot, and elements greater than the pivot.
        2. Recursively sort the subarrays to the left and right of the pivot.
        3. Return the sorted array.

    Time complexity:
        - Average case: O(n log n)
        - Worst case: O(n^2), randomization of pivot reduces chance of worst case

    Space complexity:
        - O(log n), recursion stack

    Note:
        - This function modifies the input array in-place.
        - The pivot element is chosen randomly from the input array.
    """
    def partition(l, r):
        p = randint(l,r)    
        v = A[p]
        A[l],A[p] = A[p],A[l]
        i = l + 1
        while i <= r:
            if A[i] > v:
                A[r], A[i] = A[i], A[r] 
                r -= 1
            elif A[i] < v:
                A[l], A[i] = A[i], A[l]                    
                l += 1
                i += 1
            else: i += 1
        return l, r
    def qsort(l, r):
        if l >= r: return
        l1, l2 = partition(l, r)
        qsort(l, l1 - 1)
        qsort(l2 + 1, r)
    qsort(0, len(A) - 1)
    return A