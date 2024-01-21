def gosper_hack(n, k):
    """Gosper's hack for iterating through bitwise k-combinations of n items."""
    c = (1 << k) - 1
    while c < 1 << n:
        yield c
        x = c & -c
        y = c + x
        c = ((c & ~y) // x >> 1) | y