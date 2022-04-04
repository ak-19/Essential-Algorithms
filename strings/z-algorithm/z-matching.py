from zcount import z_count, z_count_v2

def z_algorithm(p, t):
    P = len(p)
    T = len(t)
    s = p + '$' + t
    count = z_count(s)
    result = []
    for i, length in enumerate(count):
        if length == P:
            result.append(i - P - 1)
    return result

def z_algorithm_v2(p, t):
    P = len(p)
    T = len(t)
    s = p + '$' + t
    count = z_count_v2(s)
    result = []
    for i, length in enumerate(count):
        if length == P:
            result.append(i - P - 1)
    return result    

print(z_algorithm('ana', 'ananabanana') == z_algorithm_v2('ana', 'ananabanana'))