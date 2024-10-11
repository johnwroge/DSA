/*
Given an array of arrays representing a collection of islands. Return the maximum area of the largest island. 
An island is a group of 1's surrounded by 0's water. Assume the entire grid is surrounded by water 0's
*/




const maxArea= (grid) => {

    //create a max area variable
    let count = 0; 
      //create a grid representing if the space has been visited
      let visited = {};
    //iterate over every vertex in grid and check if the value is 1
    for (let i = 0; i < grid.length; i++){
        for (let j = 0; j < grid[0].length; j++){
        //if true invoke dfs with the current vertex
            if (grid[i][j] === 1){
                console.log(i,j)
                let val = dfs(visited, i, j)
            //reassign max to be returned value or  previous max
                count = Math.max(count, val);
            } 
        }
    
    }
  
    function dfs(visited, i, j) {
        //base case -> if the value is 0, does not exist, or is out of bounds return 0
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || !grid[i][j] || visited[[i,j]]){
            return 0; 
        }
        visited[[i,j]] = true;
        //otherwise change the current cell in visited object to be true
        //return 1 + the function calls
        return 1 + dfs(visited, i + 1, j) + dfs(visited, i - 1, j) + dfs(visited, i, j + 1) + dfs(visited, i, j - 1)
    }
return count; 
}




console.log(maxArea(
    [[0,0,0,1,0,0],
     [1,1,0,1,0,0],
     [1,0,0,1,0,0],
     [0,0,0,1,0,0],
     [0,0,0,1,0,0],
     [0,0,0,1,0,0]]
     ));