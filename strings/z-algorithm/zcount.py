def z_count_v2(s):
    N = len(s)
    count = [0] * N
    count[0] = N
    L = R = 0
    for i in range(1, N):
        if i <= R: count[i] = min(R - i + 1, count[i - L])

        while i + count[i] < N and s[count[i]] == s[i + count[i]]: count[i] += 1

        if i + count[i] - 1 > R: L, R = i, i + count[i] - 1    
    return count    

def z_count(s):
    N = len(s)
    count = [0] * N
    count[0] = N

    L = R = k = 0

    for i in range(1, N):
        if i > R:
            L = R = i
            while R < N and s[R - L] == s[R]: R += 1
            count[i] = R - L
            R -= 1
        else:
            k = i - L
            if count[k] < R - i + 1:
                count[i] = count[k]
            else:
                L = i
                while R < N and s[R] == s[R-L]: R += 1
                count[i] = R - L
                R -= 1

    return count

# print(z_count('aaavaavaaaavvava') == [16, 2, 1, 0, 2, 1, 0, 3, 4, 2, 1, 0, 0, 1, 0, 1])
# print(z_count_v2('aaavaavaaaavvava') == [16, 2, 1, 0, 2, 1, 0, 3, 4, 2, 1, 0, 0, 1, 0, 1])

#               L
#                   R
# a a a v a a v a a a a v v a v a
#16 2 1 0 3 1 0 3 4 2 1 0 0 1 0 1
  
              