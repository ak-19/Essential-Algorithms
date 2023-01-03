def lis_quadratic(A):
    N = len(A)
    dp = [1]*N
    max_lis = 1
    for i in range(N):
        for j in range(i - 1, -1, -1):
            if A[j] <= A[i]: dp[i] = max(dp[i], dp[j] + 1)
        max_lis = max(max_lis, dp[i])

    result = []
    last = None
    for i in range(N - 1, -1, -1):
        if dp[i] == max_lis and last is None:
            result.append(A[i])
            last = A[i]
            max_lis -= 1
        elif last and A[i] <= last and dp[i] == max_lis:
            result.append(A[i])
            last = A[i]
            max_lis -= 1

    return result[::-1]

print(lis_quadratic([1,4,3,7,5,8,7,8]))
print(lis_quadratic(list("babca")))
print(lis_quadratic(list("bbazb")))
print(lis_quadratic(list("edcba")))
print(lis_quadratic(list("ghi")))