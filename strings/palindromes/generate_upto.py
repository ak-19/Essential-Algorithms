def generate(upto):
    palindromes = [[], []]
    for length in range(1, len(str(upto)) + 1):
        half_len = (length + 1) // 2
        start = 10 ** (half_len - 1)
        end = 10 ** half_len
        for half in range(start, end):
            s = str(half)
            if length % 2 == 0: p = int(s + s[::-1])
            else: p = int(s + s[-2::-1])
            if p <= upto:
                palindromes[p % 2].append(p)
    return palindromes