/*

Given a 2d grid map of 1s (land) and 0s (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

EXAMPLE 1:

Input:
[
  [0, 1, 1, 1, 0],
  [1, 1, 0, 1, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0]
]
Output: 1

Input:
[
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 1]
]
Output: 3

Assume that the grid will be an array of arrays of numbers either 0 or 1, and
that the grid will have at least one element.

//stepping stone into different graph questions. 



*/

const numIslands = grid => {
  //edge case: if grid is not defined, return 0
  if (!grid) return 0;
  //create a num islands counter
  let islands = 0;

  //create a grid to store visited information (T -> visited, F -> not visited)
  const seen = grid.map(row => row.map(col => false));
  
  for (let row = 0; row < grid.length; row++){
    for (let col = 0; col < grid[0].length; col++){
        if (grid[row][col] === 1 && !seen[row][col]){
          dfs(grid, seen, row, col);
          islands += 1;
        }
    }
  }
  return islands;
};

const dfs = (grid, seen, row, col) => {

  //base case: if row or column reaches lowest/highest index, if the position is already seen, or if the current element is a 0 -> return
  if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || seen[row][col] || grid[row][col] === 0) return;
  //change the current element to be seen 
  seen[row][col] = true;

  dfs(grid, seen, row + 1, col);
  dfs(grid, seen, row - 1, col);
  dfs(grid, seen, row, col + 1);
  dfs(grid, seen, row, col - 1);
}





console.log(numIslands([
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 1]
]))

module.exports = {numIslands};
