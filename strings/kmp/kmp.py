from prefix_function import prefix_function

def kmp(text, pattern):
    s = pattern + '#' + text
    S = len(s)
    P = len(pattern)
    pf = prefix_function(s)
    result = []
    for i in range(P + 1, S):
        if pf[i] == P:
            result.append(i - 2 * P)
    return result

print(kmp('abababcaab', 'aba'))