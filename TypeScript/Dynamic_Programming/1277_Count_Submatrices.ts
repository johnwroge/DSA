// Recursive Solution
function countSquares(matrix: number[][]): number {
    const solve = (i: number, j: number, grid: number[][], dp: number[][]): number => {
        // If the cell lies outside the grid, return 0
        if (i >= grid.length || j >= grid[0].length) {
            return 0;
        }
        if (grid[i][j] === 0) {
            return 0;
        }
        // If we have already visited this cell, return the memoized value
        if (dp[i][j] !== -1) {
            return dp[i][j];
        }
        // Find the answer for the cell to the right of the current cell
        const right = solve(i, j + 1, grid, dp);
        // Find the answer for the cell to the diagonal of the current cell
        const diagonal = solve(i + 1, j + 1, grid, dp);
        // Find the answer for the cell below the current cell
        const below = solve(i + 1, j, grid, dp);
        
        dp[i][j] = 1 + Math.min(right, diagonal, below);
        return dp[i][j];
    };

    let ans = 0;
    const dp: number[][] = Array(matrix.length).fill(0)
        .map(() => Array(matrix[0].length).fill(-1));
    
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            ans += solve(i, j, matrix, dp);
        }
    }
    return ans;
}

// Iterative Solution (more efficient)
function countSquares_2(matrix: number[][]): number {
    const row = matrix.length;
    const col = matrix[0].length;
    const dp: number[][] = Array(row + 1).fill(0)
        .map(() => Array(col + 1).fill(0));
    let ans = 0;
    
    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (matrix[i][j]) {
                dp[i + 1][j + 1] = Math.min(
                    dp[i][j + 1],
                    dp[i + 1][j],
                    dp[i][j]
                ) + 1;
                ans += dp[i + 1][j + 1];
            }
        }
    }
    return ans;
}