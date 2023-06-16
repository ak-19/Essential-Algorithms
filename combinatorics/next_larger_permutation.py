# accepts array of comparable values
# finds next bigger permutation if else exists, else returns empty array
def next_larger(s):
    N = len(s)
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i < 0:
        return []
    j = N - 1
    while j >= 0 and s[i] >= s[j]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s[i + 1:] = reversed(s[i + 1:])
    return s

# finds next k-th larger permutation
# counts number of swaps, that is minimum swaps to get next k-th permutation
class Solution:
    def get_next_k(self, A, k):
        N = len(A)
        for _ in range(k):
            for i in range(N-2, -1, -1):
                if A[i] < A[i+1]:
                    break
            for j in range(N-1, i, -1):
                if A[i] < A[j]:
                    break
            A[i], A[j] = A[j], A[i]
            A[i+1:] = A[i+1:][::-1]
        return A

    def count_swaps(self, A, B):
        count, N = 0, len(A)
        for i in range(len(B)):
            if A[i] != B[i]:
                j = i + 1
                while (j < N and A[j] != B[i]):
                    j += 1

                while j > i:
                    A[j], A[j - 1] = A[j - 1], A[j]
                    j -= 1
                    count += 1
        return count

    def getMinimumSwapsToKthPermutation(self, orig: str, k: int) -> int:
        return self.count_swaps(list(orig), self.get_next_k(list(orig), k))
