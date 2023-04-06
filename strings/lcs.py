# accepts 2 strings, a and b
# finds longest common subsequence, and returns the value of lcs string
def lcs(a, b):
    A, B = len(a), len(b)
    dp = [[''] * (B + 1) for _ in range(A + 1)]
    for i in range(1, A + 1):
        for j in range(1, B + 1):
            if a[i - 1] == b[j - 1]: dp[i][j] = dp[i - 1][j - 1] + a[i - 1] 
            else: dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
    return dp[A][B]