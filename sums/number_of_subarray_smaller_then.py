#sliding window trick for O(n), number of subarrays Array A, with sum upto(less or equal) then value val
def subarrays_sum_upto(A, val):
    count = j = s = 0
    for i, v in enumerate(A):
        s += v
        while s > val:
            s -= A[j]
            j += 1
        print(A[j:i + 1])
        count += i - j + 1 
    return count