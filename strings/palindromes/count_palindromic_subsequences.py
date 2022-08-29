from functools import cache

#recursive dynamic programming with memoization
def count_palindromic_subsequences(s):                                   
    mod = 10**9 + 7
    
    @cache
    def dp(i, j):
        if i > j: return 0            
        if i == j: return 1

        result = 0

        for c in set(s[i:j + 1]):
            L, R = s.find(c, i, j  + 1), s.rfind(c, i, j + 1)
            if L == R: result += 1                    
            else: result += dp(L + 1, R - 1) + 2

        return result % mod        
    
    return dp(0, len(s) - 1) % mod