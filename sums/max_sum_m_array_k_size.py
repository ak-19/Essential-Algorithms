from collections import defaultdict

def maxSumOfThreeSubarrays(A, k, m):
    N = len(A)
    window_sum = [sum(A[:k])]
    
    for i in range(1, N - k + 1): window_sum.append(window_sum[-1] - A[i - 1] + A[i + k - 1])
                    
    best_for = defaultdict(lambda : [0, []])
    
    for start in range(N - m * k + 1):
        for i in range(1, m + 1):
            curr_index = start + (i - 1) * k                
            if window_sum[curr_index] + best_for[i - 1][0] > best_for[i][0]:
                best_for[i][0] = window_sum[curr_index] + best_for[i - 1][0]
                best_for[i][1] = best_for[i - 1][1] + [curr_index]
    
    return best_for[m][1]