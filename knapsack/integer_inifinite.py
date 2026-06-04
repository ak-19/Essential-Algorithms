# Integer Knapsack with infinite amount of items
def knapsack_infinite(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(weights[i], capacity + 1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


# Example usage
weights = [2, 3, 4]
values = [3, 4, 5]
capacity = 6
result = knapsack_infinite(weights, values, capacity)
print("Maximum value in Knapsack =", result)

# version with reconstruction of used items
def knapsack_infinite_with_reconstruction(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    item_used = [-1] * (capacity + 1)

    for i in range(n):
        for w in range(weights[i], capacity + 1):
            if dp[w] < dp[w - weights[i]] + values[i]:
                dp[w] = dp[w - weights[i]] + values[i]
                item_used[w] = i

    # Reconstruct the items used
    w = capacity
    used_items = []
    while w > 0 and item_used[w] != -1:
        used_items.append(item_used[w])
        w -= weights[item_used[w]]

    return dp[capacity], used_items
