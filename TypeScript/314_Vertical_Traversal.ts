/*
'''
314. Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7



Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

'''

'''
solution keep track of position with hashmap
using breadth first search
hash = {0: [3, 15], -1: [9] 1: [15, 20], 2: [7]}
by starting at root 0: root [(0, 3), (-1, 9), (1, 20), (15, 0), (7, 2)]
sort the keys and then output each of those positions
'''
*/

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function verticalOrder(root: TreeNode | null): number[][] {
    if (!root) return []; 
    const Q: Array<[TreeNode, number]> = [];
    const ordering: { [key: number]: number[] } = {};
    Q.push([root, 0]);
  
    while (Q.length > 0) {
      const [curr, index] = Q.shift()!; 
      if (!ordering[index]) {
        ordering[index] = [];
      }
      ordering[index].push(curr.val);
  
      if (curr.left) Q.push([curr.left, index - 1]);
      if (curr.right) Q.push([curr.right, index + 1]);
    }
  
    const order = Object.keys(ordering).map(Number).sort((a, b) => a - b); 
    const verticals: number[][] = []; 
  
    for (let i of order) {
      verticals.push(ordering[i]);
    }
  
    return verticals;
  }
  