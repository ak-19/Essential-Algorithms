def bitwise_sum(a, b):
    mask = 0xffffffff
    
    while b:
        a, b = (a ^ b) & mask,  ((a&b) << 1) & mask
    
    maximum =  0x7fffffff
    
    return a if a < maximum else ~(a^mask)