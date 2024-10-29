function BinarySearchTree(value) {
  this.value = value;
  this.right = null;
  this.left = null;
}

/*

Given the root of a binary search tree and a callback function, apply the
callback to the values of the BST in breadth-first order.

Example:

If the tree is

     4
   /   \
  2     7
 / \     \
1   3     9
         /
        8

then apply the callback on the numbers in the order:
4, 2, 7, 1, 3, 9, 8.

Hint:

Maintain a queue (array) consisting of the nodes we need to operate on.
For each node in the queue, push the left and right children (if applicable) to
the end of the queue. Keep consuming the queue (using the shift method) until
there are no more nodes in the queue.

Utilizing recursion is not necessary, nor recommended.

*/

const bfs = (root, callback) => {
  //initialize a node as the root
  let node = root;
  // and a queue
  const queue = [];
  //and a results
  const results = [];
  //push the root into the queue
  queue.push(node);
    //test while the queue contains nodes
    while (queue.length){
      //reassign the node to be first element in the queue
      node = queue.shift();
      //push the eval result of callback passing in the node value into the results array
      results.push(callback(node.value));
      //check if there is a left, if yes push into the queue
      if(node.left) queue.push(node.left);
      //check if there is a right, if yes, push into the queue
      if (node.right) queue.push(node.right);
    }
  //return the finished results array
  return results;
};

//


/*
102. Binary Tree Level Order Traversal
Medium
12.3K
242
Companies
Given the root of a binary tree, return the level order traversal 
of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
 var levelOrder = function(root) {
  if (root === null) return [];
  let queue = [root];
  let result = [];
  while (queue.length > 0) {
      let level = [];
      let size = queue.length;
      for (let i = 0; i < size; i++) {
          let node = queue.shift();
          level.push(node.val);
          if (node.left !== null) queue.push(node.left);
          if (node.right !== null) queue.push(node.right);
      }
      result.push(level);
  }
  return result;
};

var zigZagBST = function(root){




  
}












/*

Extension:

Given a 2D grid of 0s, 1s, and a single 2, with the start position the top-left
corner, determine the minimum distance need to travel to the 2.

value iteration algorithm (discrete algorithm for sum)



0s represent traversable land.
1s represent "water" that we cannot traverse.
2 represents our final goal.

The top-left corner will always be a 0. We will try to reach the 2 by
traversing through land. We are only allowed to traverse up/left/down/right,
with no diagonal movement allowed. If the 2 cannot be reached, return -1.

Examples:

Input:
[
  [0, 0, 1, 1],
  [2, 0, 1, 0],
  [1, 0, 0, 0]
]
Output: 1 (starting at the top-left corner, move down)

Input:
[
  [0, 0, 1, 1],
  [0, 0, 1, 2],
  [1, 0, 0, 0]
]
Output: 6 (starting at the top-left corner, either move
down-right-down-right-right-up, or right-down-down-right-right-up)

Input:
[
  [0, 0, 0, 1, 1, 0, 2, 0]
]
Output: -1 (the 2 is not reachable by land)

Hint:

Apply the general principles of breadth-first search. Maintain a queue of
positions with their distances. When consuming each position, check to see which
neighbors are traversable and haven't already been visited.

*/

const minimumDistance = grid => {

  //create a variable to store the current count;
  let row = 0;
  let col = 0;
  for (let i = row; i < grid.length; i++){
    for (let j = col; j < grid[0].length; j++){
      if (grid[i][j] === 0){
      traverse(grid, row, col, count = 0);
      }
    }
  }

  //return the final count
  return count;
};

const traverse = (grid, row, col, count) => {
 
  
  //base case: if row or col isn't valid, return;
  if (row >= grid.length || row < 0 || col >= grid[0].length || col < 0 || grid[row][col] === 1){
     return;
  }
  //base case: if current value is a 2 return the count;
  if (grid[row][col] === 2){
    return count; 
  } 

  grid[row][col] = 1; 

  //call traverse
  traverse(grid, row + 1, col, count + 1)
  traverse(grid, row - 1, col, count + 1)
  traverse(grid, row, col + 1, count + 1)
  traverse(grid, row, col - 1, count + 1)
}


console.log(minimumDistance([
  [0, 0, 1, 1],
  [2, 0, 1, 0],
  [1, 0, 0, 0]
]))

module.exports = {BinarySearchTree, bfs, minimumDistance};
