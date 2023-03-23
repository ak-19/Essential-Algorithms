# accepts array of comparable values
# finds next bigger permutation if else exists, else returns empty array
def next_larger(s):
    N = len(s)
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]: i -= 1
    if i < 0: return []
    j = N - 1
    while j>=0 and s[i] >= s[j]: j -= 1
    s[i], s[j] = s[j], s[i]
    s[i + 1:] = reversed(s[i + 1:])
    return s