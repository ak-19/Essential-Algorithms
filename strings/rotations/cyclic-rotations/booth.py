def booth(s: str) -> int:
    """
    Return the starting index of the lexicographically smallest
    cyclic rotation of s.

    Time:  O(n)
    Space: O(n)
    """
    n = len(s)
    if n == 0: return -1

    doubled = s + s
    failure = [-1] * (2 * n)

    candidate = 0

    for j in range(1, 2 * n):
        i = failure[j - candidate - 1]

        while i != -1 and doubled[j] != doubled[candidate + i + 1]:
            if doubled[j] < doubled[candidate + i + 1]:
                candidate = j - i - 1

            i = failure[i]

        if doubled[j] != doubled[candidate + i + 1]:
            if doubled[j] < doubled[candidate]:
                candidate = j

            failure[j - candidate] = -1
        else:
            failure[j - candidate] = i + 1

        if candidate >= n:
            break

    return candidate 