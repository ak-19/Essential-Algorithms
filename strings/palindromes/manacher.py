from typing import  List

# @#a#b#b#a#b#b#a#b#b#a#b#b#a#b#$
def manachers(S):
    N = len(S)
    A = '@#' + '#'.join(S) + '#$'

    ans = [0] * len(A)
    center = right = 0

    for i in range(1, len(A) - 1):
        if i < right:
            ans[i] = min(right - i, ans[2 * center - i])
        while A[i + ans[i] + 1] == A[i - ans[i] - 1]:
            ans[i] += 1
        if i + ans[i] > right:
            center, right = i, i + ans[i]
    return A, ans
    
def extractLSP(A, m):
    lps = max(m)
    index = None
    for i in range(len(m)):
        if m[i] == lps:
            index = i
            break

    cut = A[index - lps:index + lps + 1]

    if cut[0] == '#':
        return cut[1::2]

    return cut[::2]
    

        
# A, m = manachers("abbabbabbabbab")
A, m = manachers("abc")


print(A)
print(m)
print(extractLSP(A, m))

# "ababbb"
# "zaaaxbbby"