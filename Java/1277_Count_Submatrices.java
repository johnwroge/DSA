// Recursive Solution
class Solution {
    private int solve(int i, int j, int[][] grid, int[][] dp) {
        // If the cell lies outside the grid, return 0
        if (i >= grid.length || j >= grid[0].length) {
            return 0;
        }
        if (grid[i][j] == 0) {
            return 0;
        }
        // If we have already visited this cell, return the memoized value
        if (dp[i][j] != -1) {
            return dp[i][j];
        }
        // Find the answer for the cell to the right of the current cell
        int right = solve(i, j + 1, grid, dp);
        // Find the answer for the cell to the diagonal of the current cell
        int diagonal = solve(i + 1, j + 1, grid, dp);
        // Find the answer for the cell below the current cell
        int below = solve(i + 1, j, grid, dp);
        
        dp[i][j] = 1 + Math.min(Math.min(right, diagonal), below);
        return dp[i][j];
    }

    public int countSquares(int[][] matrix) {
        int ans = 0;
        int[][] dp = new int[matrix.length][matrix[0].length];
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }
        
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                ans += solve(i, j, matrix, dp);
            }
        }
        return ans;
    }
}

// Iterative Solution
class Solution {
    public int countSquares(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        int[][] dp = new int[row + 1][col + 1];
        int ans = 0;
        
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 1) {
                    dp[i + 1][j + 1] = Math.min(
                        Math.min(dp[i][j + 1], dp[i + 1][j]),
                        dp[i][j]
                    ) + 1;
                    ans += dp[i + 1][j + 1];
                }
            }
        }
        return ans;
    }
}