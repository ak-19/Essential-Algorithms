# Last Substring in Lexicographical Order
# O(N) time, O(1) space !!!
def lastSubstring(s):
    N = len(s)
    i = k = 0
    j = 1

    while j + k < N:

        if s[i + k] == s[j + k]: 
            k += 1

        elif s[i + k] < s[j + k]:
            i = max(i + k + 1, j)
            j = i + 1
            k = 0

        else:
            j += 1
            k = 0


    return s[i:]