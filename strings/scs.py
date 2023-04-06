# accepts 2 strings A and B
# finds shortest common supersequence, returns string value of the scs

class Solution:
    def get_lcs(self, a, b):
        A, B = len(a), len(b)
        dp = [[''] * (B + 1) for _ in range(A + 1)]
        for i in range(1, A + 1):
            for j in range(1, B + 1):
                if a[i - 1] == b[j - 1]: dp[i][j] = dp[i - 1][j - 1] + a[i - 1] 
                else: dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
        return dp[A][B]

    def shortestCommonSupersequence(self, A: str, B: str) -> str:
        lcs = self.get_lcs(A, B)
        result, i, j = '', 0, 0
        M, N = len(A), len(B)

        for c in lcs:
            while i < M and  A[i] != c: 
                result += A[i]
                i += 1
            while j < N and  B[j] != c: 
                result += B[j]
                j += 1                

            i += 1
            j += 1
            result += c

        if i < len(A): result += A[i:]
        if j < len(B): result += B[j:]

        return result