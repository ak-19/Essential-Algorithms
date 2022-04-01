def lmb(v):
    return v & (-v)

print(int('110', 2), lmb(int('110', 2)))
print(int('100', 2), lmb(int('100', 2)))