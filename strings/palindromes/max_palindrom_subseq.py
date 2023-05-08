#1. old school, iterative bottom up dp
def longest_palindromic_subsequence_length1(s) -> int:
    N = len(s)
    dp = [[0] * N for _ in range(N)]                    
    max_palindrome = 1        

    for i in range(N - 1, -1, -1):
        dp[i][i] = 1

        for j in range(i + 1, N):   
            if s[i] == s[j]:
                dp[i][j] =  2 + dp[i + 1][j - 1]
            else:
                dp[i][j] =  max(dp[i + 1][j] , dp[i][j - 1])

            max_palindrome = max(max_palindrome, dp[i][j]) 
    
    return max_palindrome 

#2. Given a string, find the length of its Longest Palindromic Subsequence (LPS).
def max_palindromic_subsequence_length2(s) -> int:
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
# 3. alternative solution wich uses reverse string
# Given a string and its reverse, find the length of its Longest Palindromic Subsequence (LPS).
def max_palindromic_subsequence_length3(s, s2):
    N = len(s)
    dp = [[0]*(N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(N + 1):
            if 0 not in [i,j]: 
                if s[i - 1] == s2[j - 1]: dp[i][j] = 1 + dp[i - 1][j - 1]
                else: dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[N][N]