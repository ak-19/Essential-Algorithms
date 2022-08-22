# inspired by article from stack overflow:
# https://stackoverflow.com/questions/72114300/how-to-generate-k-largest-subset-sums-for-a-given-array-contains-positive-and-n
# appeared as problem #4 on 307th LeetCode Weekly Contest

from heapq import heappop, heappush


def k_maximum_priority(nums, k):
    N, max_sum, A = len(nums), sum(max(v, 0) for v in nums), sorted([abs(v) for v in nums])

    result, count = max_sum, 1

    pq = [(-max_sum + A[0], 0)]

    while count < k:
        next_smaller_sum, index = heappop(pq)
        result = -next_smaller_sum
        count += 1
        if index + 1 < N:            
            heappush(pq, (next_smaller_sum - A[index] + A[index + 1], index + 1))
            heappush(pq, (next_smaller_sum + A[index + 1], index + 1))

    return result


print(k_maximum_priority([2,4,-2], k = 5))
print(k_maximum_priority([1,-2,3,4,-10,12], k = 16))
 