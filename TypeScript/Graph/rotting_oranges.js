/*
994. Rotting Oranges
Medium
10.2K
341
Companies
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally
 adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.
*/

/**
 * @param {number[][]} grid
 * @return {number}
 */

/*

1. understand the problem
    given a



2. algorithm design

3. implementation


*/



var orangesRotting = function(grid) {
    //create a bag class to store items from the grid; 
    const queue = [];
    //create a count variable
    let count = 0; 
    for (let i = 0; i < grid.length; i++){
        for (let j = 0; j < grid[0].length; j++){
            //if current value is 2 (rotten) push into queue
            if (grid[i][j] === 2){
                queue.push([i,j,0]);
                //these are rotten at time = 0
            } else if (grid[i][j] === 1){
                count += 1;
            }
            //if current value is 1, increment count and reassign to 2
        }
    }
    //while the bag is not empty, process all the neighbors
    let max = 0;
    
    while (queue.length){
        let current = queue.shift();
        let x = current[0];
        let y = current[1];
        let time = current[2];
        max = Math.max(max, time)
        
        if (x < grid.length - 1 && grid[x + 1][y] === 1){
             queue.push([x + 1, y, time + 1]);
             grid[x + 1][y] = 2;
             --count; 
        }
        if (x > 0 && grid[x - 1][y] === 1){
            queue.push([x - 1, y, time + 1])
            grid[x - 1][y] = 2;
             --count; 
        }
        if (grid[x][y + 1] === 1){
            queue.push([x, y + 1, time + 1])
            grid[x][y + 1] = 2;
             --count; 
        }
        if (grid[x][y - 1] === 1) {
            queue.push([x, y - 1, time + 1])
            grid[x][y - 1] = 2;
             --count; 
        }

    }
 //check whether we reached all the fresh oranges (if count === 0)
 return count === 0 ? time : -1; 

}


var orangesRotting = function(grid) {
    //Initialize queue for our BFS, Number of fresh oranges, and time to be returned.
    let queue = [], oranges = 0, time = 0;
    
    //Traverse matrix.  If we find a fresh orange, increment orange count.
    //If we find a rotten one, add it to the queue.
    for (let r = 0; r < grid.length; r++) {
      for (let c = 0; c < grid[r].length; c++) {
        if (grid[r][c] === 1) oranges++
        else if (grid[r][c] === 2) queue.push([r,c,0]);
      }
    }
      
    //Dirs will help us check neighbors during our BFS.  Adding these coordinates
    //to a point just gets right, left, up and down.  endR and endC are used later
    //to make sure neighbor coords are within grid.
    const dirs = [[0,1], [1,0], [0,-1], [-1,0]];
    const endR = grid.length - 1, endC = grid[0].length - 1;
    
    //Loop while queue is not empty and there are still fresh oranges.
    while (queue.length && oranges) {
    
      //Entry within queue can be destructured to make it easier to work with.
      //Each queue entry has a row, column and number of minutes taken for
      //infection to reach.
      const [curR, curC, mins] = queue.shift();
      
      //If orange is still fresh, we mark it as rotten, decrement our fresh oranges
      //count and set time to = mins.  Since we BFSing, the time it takes to infect
      //the last orange will be the time to infect all.  Once all oranges have
      //been infected, our orange count will = 0 and our condition in while loop
      //will stop the loop.  Time can then be returned.
      if (grid[curR][curC] === 1) {
        grid[curR][curC] = 2;
        oranges--;
        time = mins;
      }
  
      //Here's where our dir array above comes in handy.  We destructure
      //each entry and add it to our current to get neighbor coords below.
      for (let [addR, addC] of dirs) {
      
        //Here we obtain our new or neighbor coordinates by adding currentRow
        //and addRow of dir.  Same for col.
        const [newR, newC] = [curR + addR, curC + addC];
        
        //Here we check to make sure new coordinates lie within the grid.
        if (newR < 0 || newR > endR || newC < 0 || newC > endC) continue;
        
        //If neighbor coord is valid, and there is a fresh orange at those coordinates
        //we push coordinates to our BFS to be infected next.  We also increment the
        //mins count to track time taken to spread to that orange.
        if (grid[newR][newC] === 1) {
          queue.push([newR, newC, mins + 1])
        }
      }
    }
    
    //If we still have uninfected oranges, we return -1 because it won't spread
    //to all.  Otherwise, we simply return the time from initial infected to last
    //infected orange.
    return oranges ? -1 : time;
  };
// orangesRotting([[2,1,1],[1,1,0],[0,1,1]])