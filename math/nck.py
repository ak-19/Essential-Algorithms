def nCk1(n, k, mod):
    """
    Calculate nCr % mod.
    using builtin pow function
    """
    if k > n: return 0
    if k > n - k: k = n - k
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % mod
        denominator = (denominator * (i + 1)) % mod
    return (numerator * pow(denominator, mod - 2, mod)) % mod

def nCk2(n, k, mod):
    """
    Calculate nCr % mod.
    """
    if k > n: return 0
    if k > n - k: k = n - k
    f = [1] 
    inv = [exp_mod(1, mod-2, mod)]    
    for i in range(1, n + 1):
        f.append(f[-1] * i % mod)
        inv.append(pow(f[-1], -1, mod))            
    return f[n] * inv[k] * inv[n - k] % mod

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

def nCk3(n, k, mod):
    """
    Calculate nCr % mod.
    """
    if k > n: return 0
    if k > n - k: k = n - k
    f = [1] 
    inv = [exp_mod(1, mod-2, mod)]    
    for i in range(1, n + 1):
        f.append(f[-1] * i % mod)
        # TODO - mod -2 as exp - need math proof for this
        inv.append(exp_mod(f[-1], mod-2, mod))            
    return f[n] * inv[k] * inv[n - k] % mod