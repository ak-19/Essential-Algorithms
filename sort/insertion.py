from collections import Counter
def insort(A):
    N = len(A)

    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v: 
            A[j + 1] = A[j]
            j -= 1        
        A[j + 1] = v

    return A


print(insort([7,6,5,4,3,2,1]))
print(insort([27, 49, 14, 93, 96, 92, 43, 76, 97, 92, 85, 84, 100, 5, 84, 54, 17, 64, 85, 96]))