/*
2684. Maximum Number of Moves in a Grid

You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.

 

Example 1:


Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.
Example 2:


Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
1 <= grid[i][j] <= 106
*/


function maxMovesDP(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const dp: number[][] = Array.from({ length: m }, () => Array(n).fill(0));

    // Initialize the first column as reachable.
    for (let i = 0; i < m; i++) {
        dp[i][0] = 1;
    }

    // Process each column by iterating through rows
    for (let j = 0; j < n - 1; j++) {
        for (let i = 0; i < m; i++) {
            if (dp[i][j]) { // Check if the cell is reachable
                // Try moves in three directions
                for (let di of [-1, 0, 1]) {
                    const ni = i + di;
                    const nj = j + 1;
                    if (0 <= ni && ni < m && grid[ni][nj] > grid[i][j]) {
                        dp[ni][nj] = 1;
                    }
                }
            }
        }
    }

    // Find the rightmost reachable column
    for (let j = n - 1; j >= 0; j--) {
        if (dp.some(row => row[j] === 1)) {
            return j;
        }
    }

    return 0;
}


function maxMovesBFS(grid: number[][]): number {
    const M = grid.length;
    const N = grid[0].length;
    const directions = [-1, 0, 1];

    const queue: [number, number, number][] = [];
    const visited: boolean[][] = Array.from({ length: M }, () => Array(N).fill(false));

    // Enqueue cells in the first column
    for (let i = 0; i < M; i++) {
        visited[i][0] = true;
        queue.push([i, 0, 0]);
    }

    let maxMoves = 0;

    while (queue.length) {
        const [row, col, count] = queue.shift()!; // Dequeue the front element
        maxMoves = Math.max(maxMoves, count);

        // Check all three directions
        for (let dir of directions) {
            const newRow = row + dir;
            const newCol = col + 1;

            // If valid move and cell is greater, enqueue the cell
            if (
                0 <= newRow && newRow < M &&
                newCol < N &&
                !visited[newRow][newCol] &&
                grid[row][col] < grid[newRow][newCol]
            ) {
                visited[newRow][newCol] = true;
                queue.push([newRow, newCol, count + 1]);
            }
        }
    }

    return maxMoves;
}
