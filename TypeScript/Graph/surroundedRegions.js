


// var solve = function(board) {

//     //iterate over the board 
//     for (let i = 0; i < board.length; i++){   
//         for (let j = 0; j < board[0].length; j++){
//         //check if the current position is a "O"
//             if (board[i][j] === "O" && (i === 0 ||j === 0 || i === board.length - 1 || j === board[0].length - 1)){
//             //check if the helper function returns true
//                 dfs(board, i, j) 
//                 //if true, update the current position to a "X"
//             }
//         }
//     }
// console.log('board',board)
//     for (let i = 0; i < board.length; i++){   
//         for (let j = 0; j < board[0].length; j++){
//             if (board[i][j] === "visited"){
//                 board[i][j] = "O"
//             } else {
//                 board[i][j] = "X"
//             }
//         }
//     }
//     //return the board
//     return board;
// };

// var solve = function(board) {
//     // iterating through the board and checking for all "O" on the edges of the board
//      //if there is an "O" on the edge, call the helper function on this position 
//      for (let i = 0; i < board.length; i++){
//          for (let j = 0; j < board[0].length; j++){
//              if (board[i][j] === "O" && (i === 0 || j === 0 || i === board.length - 1 || j === board[0].length - 1))
//                  dfs(i,j);
//          }
//      }
//    //iterating through the board, if the current element is an "visited" replace it with an "O" otherwise replace it with and "X"
//      for (let i = 0; i < board.length; i++){
//          for (let j = 0; j < board[0].length; j++){
//              if (board[i][j] === "visited"){
//                  board[i][j] = "O"
//              } else {
//                  board[i][j] = "X"
//              }
//          }
//      }
//  //create a dfs helper function
//    //function should return if either i or j is out of bounds (i,j < 0 || i >= board[0].length)
//    //or the element is "visited or an "X"    
   function dfs (i, j) {
     if (i < 0 || j < 0 || i >= board.length || j >= board[i].length 
         || board[i][j] === "visited" || board[i][j] === "X"){
         return;
     }
     //the element is an "O" so reassing the element to be 'visited' 
     board[i][j] = "visited";
     //call dfs in all 4 directions
     dfs(i + 1, j)
     dfs(i - 1, j)
     dfs(i, j + 1)
     dfs(i, j - 1)
 return; 
 } 
//  }
 
 

var solve = function(board){
    //create an object that stores if the position has been visited
    //iterate over board and check if the current index is on edge
    for (let i = 0; i < board.length; i++){
        for (let j = 0; j < board[0].length; j++){
        //check if the current value is an "O"
            if (board[i][j] === "O" && (i === 0 || j === 0 || i === board.length - 1 || j === board[0].length - 1))
            //invoke helper function passing in i,j
            dfs(i,j)
        }
    }
    //create helper function that takes two indices
    function dfs (i, j){
       /*noticed that if these conditions weren't in the right order, an error will be thrown because the value 
       at i or j is undefined and cannot be evaluated.
       */
        if ( i < 0 || j < 0 || i >= board.length || j >= board[i].length || board[i][j] === "X" || board[i][j] === "visited" ){
            return; 
        }
        board[i][j] = 'visited'; 
         dfs(i + 1, j);
         dfs(i - 1, j);
         dfs(i, j + 1);
         dfs(i, j - 1);
         return; 
    }
    //iterate over board and check if the value is a "v"
    for (let i = 0; i < board.length; i++){
        for (let j = 0; j < board[0].length; j++){
        //if true, change to an "O"
        if (board[i][j] === "visited"){
            //otherwise change to an "X"
            board[i][j] = "O"
        } else {
            board[i][j] = "X"
        }
        }
    }
return board; 
}





console.log(solve(
    [["O","X","X","X"],
     ["O","O","O","X"],
     ["O","X","O","X"],
     ["X","O","X","X"]]))