from random import randint

def sum_all_subarray_quadratic(A):
    N = len(A)
    total = 0

    for i in range(N):
        s = 0
        for j in range(i, N):
            s += A[j]
            total += s

    return total

def sum_all_subarray_linear(A):
    N = len(A)    
    return sum((N - i) * (i + 1) * v for i, v in enumerate(A))

#stress test !!
# while True:
#     A = [randint(1, 100) for _ in range(20)]

#     if sum_all_subarray_quadratic(A) != sum_all_subarray_linear(A):
#         print(A)
#         break

#regular test
# A = [randint(1, 100) for _ in range(100)]
# print(sum_all_subarray_quadratic(A))
# print(sum_all_subarray_linear(A))
