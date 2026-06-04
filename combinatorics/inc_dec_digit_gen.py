def generate_numbers_with_increasing_digits():
    """
    Generate and print all numbers with strictly increasing digits (from 1 to 9).
    No repeats allowed, and digits must be in increasing order.
    """
    res = set()
    inc_digits = list(range(1, 10))
    for mask in range(1, 1 << 9):
        num = 0
        for i in range(9):
            if mask & (1 << i):
                num = num * 10 + inc_digits[i]
        res.add(num)
    return res

def generate_numbers_with_increasing_digits():
    """
    Generate and print all numbers with strictly decreasing digits (from 0 to 9).
    No repeats allowed, and digits must be in decreasing order.
    """
    res = set()
    for mask in range(1, 1 << 10):
        chosen = []
        for d in range(10):
            if mask & (1 << d):
                chosen.append(d)
        chosen.sort(reverse=True)
        if chosen[0] == 0: continue
        num = 0
        for d in chosen: num = num * 10 + d
        res.add(num)
    return res
