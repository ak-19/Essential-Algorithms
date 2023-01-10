def exponentiation_by_squaring_mod_div(base, exp, mod):
    """
    Version with modulo division constraint.
    """
    result = 1
    while exp:
        if exp % 2: result = (result * base) % mod
        exp //= 2
        base = (base ** 2) % mod
    return result

def exponentiation_by_squaring(base, exp):
    """
    faster way to exponentiation base to exp.
    Instead of repeatedly multiplying a by itself b times, 
    the method uses bitwise operations to determine the factors of b 
    and uses those factors to calculate the result.
    """
    result = 1
    while exp:
        if exp & 1: result *= base
        exp >>= 1
        base = base ** 2
    return result    