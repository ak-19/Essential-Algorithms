def nCr1(n, r, mod):
    """
    Calculate nCr % mod.
    using builtin pow function
    """
    if r > n: return 0
    if r > n - r: r = n - r
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator = (numerator * (n - i)) % mod
        denominator = (denominator * (i + 1)) % mod
    return (numerator * pow(denominator, mod - 2, mod)) % mod

def nCr2(n, r, mod):
    """
    Calculate nCr % mod.
    """
    if r > n: return 0
    if r > n - r: r = n - r
    f = [1] 
    inv = [exp_mod(1, mod-2, mod)]    
    for i in range(1, n + 1):
        f.append(f[-1] * i % mod)
        inv.append(pow(f[-1], -1, mod))            
    return f[n] * inv[r] * inv[n - r] % mod

def exp_mod(base, exp, mod):
    """
    Fast expontation via squaring and modulo division.
    """
    result = 1
    while exp:
        if exp % 2: result = (result * base) % mod
        exp //= 2
        base = (base ** 2) % mod
    return result

def nCr3(n, r, mod):
    """
    Calculate nCr % mod.
    """
    if r > n: return 0
    if r > n - r: r = n - r
    f = [1] 
    inv = [exp_mod(1, mod-2, mod)]    
    for i in range(1, n + 1):
        f.append(f[-1] * i % mod)
        # TODO - mod -2 as exp - need math proof for this
        inv.append(exp_mod(f[-1], mod-2, mod))            
    return f[n] * inv[r] * inv[n - r] % mod