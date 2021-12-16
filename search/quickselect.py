from random import randint

def lomuto_partition(A, left, right, pivotIndex):
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[right]  = A[right], A[pivotIndex]
    storeIndex = left
    for i in range(left, right):
        if A[i] < pivotValue:
            A[storeIndex], A[i] = A[i], A[storeIndex]
            storeIndex += 1
    A[right], A[storeIndex] = A[storeIndex], A[right]
    return storeIndex

def partition(A, index, lo, hi):
    A[index], A[hi]  = A[hi], A[index]
    result_index = lo
    
    for i in range(lo, hi):
        if A[i] < A[index]:
            A[result_index], A[i]  = A[i], A[result_index]
            result_index += 1
    A[result_index], A[hi]  = A[hi], A[result_index]
    return result_index

def quickselect(A, lo, hi, k):
    if lo == hi: return
    random_index = randint(lo, hi)
    fixed_index = partition(A, random_index, lo, hi)
    
    if fixed_index == k:
        return
    
    if fixed_index < k:
        quickselect(fixed_index, hi)  
    else:
        quickselect(lo, fixed_index)  
