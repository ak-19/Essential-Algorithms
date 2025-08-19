from typing import List

def simple_graph(deg: List[int]) -> bool:
    """
    Return True if the nonnegative integer sequence `deg` is simple,
    i.e., is the degree sequence of some simple graph, by the Erdős-Gallai theorem.

    Runs in O(n log n) using prefix sums + binary search to evaluate the inequalities.
    """
    n = len(deg)
    if n == 0:
        return True

    # Basic sanity checks: integers, range bounds, even sum
    if any(d < 0 for d in deg):
        return False
    if sum(deg) % 2 == 1:
        return False

    # Degrees cannot exceed n-1 in a simple graph
    if any(d > n - 1 for d in deg):
        return False

    # Sort nonincreasing
    d = sorted(deg, reverse=True)

    # Prefix sums: pref[i] = sum of first i degrees (pref[0] = 0)
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + d[i]

    # Helper: find largest p in {k, k+1, ..., n} with d[p-1] >= k  (1-based p)
    # Uses binary search over a descending array.
    def max_index_ge_k(k: int) -> int:
        lo, hi = k, n  # 1-based indices
        ans = k - 1    # if none found, return k-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if d[mid - 1] >= k:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

    # Erdős–Gallai inequalities
    # For each k = 1..n:
    #   sum_{i=1..k} d_i <= k(k-1) + sum_{i=k+1..n} min(d_i, k)
    for k in range(1, n + 1):
        left = pref[k]
        p = max_index_ge_k(k)  # p in [k-1, n]
        # sum_{i=k+1..n} min(d_i, k) splits at p:
        #  - indices k+1..p contribute k each  (there are max(0, p-k) of them)
        #  - indices p+1..n contribute d_i (since d_i < k)
        right = k * (k - 1)
        right += (max(0, p - k)) * k
        right += pref[n] - pref[max(p, k)]  # sum of d_{p+1..n}, handling p<k case

        if left > right: return False

    return True