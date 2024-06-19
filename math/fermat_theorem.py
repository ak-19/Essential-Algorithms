"""
Any positive number nnn is expressible as a sum of two squares 
if and only if the prime factorization of nnn, 
every prime of the form (4k+3)(4k+3)(4k+3) occurs an even number of times.
"""
def canBeSumOf2Squares(c):
    i = 2
    while i * i <= c:
        if c % i == 0:
            cc = 0
            while c % i == 0:
                cc += 1
                c //= i
            if i % 4 == 3 and cc % 2: return False
        i += 1
    return (c % 4) != 3