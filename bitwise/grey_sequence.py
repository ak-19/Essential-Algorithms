def grey_sequence(n):
    """
    Every adjacent number differs by one bit.
    Bitwise difference, bit by bit is just one
    """
    return [i ^ ( i >> 1 ) for i in range(n)]

def grey_code_of(n):
    return n ^ ( n >> 1 )