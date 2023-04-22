# Given a string, find the length of its Longest Palindromic Subsequence (LPS).
def max_palindromic_subsequence_length(s) -> int:
    N = len(s)
    dp = [[0] * (N + 1) for _ in range(N)]        
    for i in range(N):  dp[i][i] = 1
    max_palindrome = 1        
    for i in range(N - 1): 
        dp[i][i + 1] = 2 if s[i] == s[i + 1] else 1
        max_palindrome = max(max_palindrome, dp[i][i + 1])
        
    for size in range(2, N): 
        for i in range(N - size):                 
            if s[i] == s[i + size]:
                dp[i][i + size] = 2 + dp[i+1][i + size - 1]                
            dp[i][i + size] = max(dp[i][i + size], dp[i+1][i + size], dp[i][i + size-1])
                
            max_palindrome = max(max_palindrome, dp[i][i + size])             
    return max_palindrome