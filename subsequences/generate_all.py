def generate_recursive(A):
    result = []
    def gen(index, curr):
        if index == len(A): 
            if curr: result.append(curr)
            return
        gen(index + 1, curr + [A[index]])
        gen(index + 1, curr)
    gen(0, [])    
    return result

def generate_bitmask(A):
    result = []
    N = len(A)
    for i in range(1, 2**N):
        curr = []
        for bit in range(N):
            if (i >> bit) & 1: curr.append(A[bit])
        result.append(curr)
    return result

def generate_loops(A):
    result = []
    for i in range(len(A)):
        nc = [[A[i]]]
        for c in result: nc.append(c+[A[i]])
        result.extend(nc)
    return result