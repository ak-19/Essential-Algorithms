def prefix_function(pattern):
    """
    Calculates the prefix function of a string
    :param pattern: string
    :return: list of integers
    """
    n = len(pattern)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi

# print(prefix_function('abababcaab'))