def debruijn(n, k):
    seen = set()
    result = ""
    def dfs(curr):
        nonlocal result
        for d in range(k):
            candidate = curr + str(d)
            if candidate not in seen:
                seen.add(candidate)
                dfs(candidate[1:])
                result += str(d)
    dfs("0" * (n - 1))
    return result + "0" * (n - 1)