def all_ones(v):
    """
    Find in number contains all ones in binary format
    """
    return v & (v + 1) == 0