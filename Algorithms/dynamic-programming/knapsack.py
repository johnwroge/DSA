

def knapsack(weights, values, capacity):
    # For knapsack and related problems
    n = len(weights)
    
    # DP[i][w] = max value possible using items 0...i with weight limit w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If current item is too heavy, skip it
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of: (1) Skip current item, (2) Take current item
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
    
    return dp[n][capacity]