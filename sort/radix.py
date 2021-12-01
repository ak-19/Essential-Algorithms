
from typing import List

def radix_sort(A):
    exp, N, mx = 1, len(A), max(A)
    temp = [0] * N
    while mx // exp:
        count = [0] * 10
        for v in A: count[(v//exp) % 10] += 1
        for i in range(1, 10): count[i] += count[i-1]
        for i in range(N - 1, -1, -1):
            index = (A[i]//exp) % 10
            temp[count[index] - 1] = A[i]
            count[index] -= 1
        for i in range(N): A[i] = temp[i]
        exp *= 10
    return A


print(radix_sort([3,6,9,1]))