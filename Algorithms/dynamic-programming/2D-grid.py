

def grid_dp(grid):
    # Common for grid-based problems like path finding, min/max path sum
    rows, cols = len(grid), len(grid[0])
    
    # Initialize DP table
    dp = [[initial_value for _ in range(cols)] for _ in range(rows)]
    
    # Set base case(s)
    dp[0][0] = grid[0][0]  # Or other base value
    
    # Fill first row and/or column if needed
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill rest of the DP table
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min_or_max(dp[i-1][j], dp[i][j-1])
    
    return dp[rows-1][cols-1]