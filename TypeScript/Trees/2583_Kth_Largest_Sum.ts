
/*
2583. Kth Largest Sum in a Binary Tree
Solved
Medium
Topics
Companies
Hint
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). 
If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

 

Example 1:


Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
Example 2:


Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n

*/

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/*
'''
Solution:

To get the sums of each of the levels we need a level order traversal
which can be done using the Breadth First Search algorithm. 

We traverse through the tree level by level and accumulate each of the levels values
after finding all the values we calculate the sum and append it to another array.

Once all the sums are calculated we can determine the kth largest by sorting otherwise if there
is no solution we return -1. 

'''
*/

interface TreeNode {
    value: number;
    left?: TreeNode;
    right?: TreeNode;
  }


function kthLargestLevelSum(root: TreeNode | null, k: number): number {
    if (!root){
        return -1;
    }
    const Q: Array<TreeNode> = [root]
    const totals: Array<number> = [];
    while (Q.length > 0){
        const row: Array<number> = []
        const length: number = Q.length;
        for (let i = 0; i < length; i++){
            const curr: TreeNode = Q.shift()
            row.push(curr.val)
            if (curr.left){
                Q.push(curr.left)
            }
            if (curr.right){
                Q.push(curr.right)
            }
        }
        const t: number = row.reduce((acc, curr) => acc + curr, 0,);
        totals.push(t);
    }
    
    totals.sort((a,b) => b - a);

    if (k <= totals.length){
        return totals[k - 1]
    } else {
        return -1
    }
    
};