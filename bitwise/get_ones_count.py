def kernigham_get_one_count(v):
    count = 0
    while v > 0:
        v &= (v - 1)
        count += 1
    return count

def get_one_count(v):
    count = 0
    while v > 0:
        count += v & 1
        v >>= 1
    return count    

print(int('110', 2), kernigham_get_one_count(6))
print(int('110', 2), get_one_count(6))
