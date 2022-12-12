def twos_complement(val, bits=32):
    if val >= 0: return val
    return (1 << bits) + val