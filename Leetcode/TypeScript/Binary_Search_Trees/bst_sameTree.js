/*
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,and the nodes have the same value.

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false

*//**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */

var symmetricalTree = (root) => {

    
}





var isSameTree = function(p, q) {
    
    //base case: if both not p and not q
        //return true
    //base case: otherwise, if not p, or not, q or p.val !== q.val 
        //return false
    //return isSameTree with p.left, q.left AND isSameTree with p.right and q.right

};

var isSameTree = function(p, q) {
    let output = true;
    const dfs = (tree1, tree2) => {
        if (tree1?.val !== tree2?.val) {
            return output = false;
        }

        if (tree1?.left !== undefined && tree2?.left !== undefined ) {
            dfs(tree1?.left, tree2?.left);
        } else if (!tree1?.left && tree2?.left) {
            return output = false;
        } else if (tree1?.left && !tree2?.left) {
            return output = false;
        }

        if (tree1?.right !== undefined && tree2?.right !== undefined ) {
            dfs(tree1?.right, tree2?.right);
        } else if (!tree1?.right && tree2?.right) {
            return output = false;
        } else if (tree1?.right && !tree2?.right) {
            return output = false;
        }
    }

    dfs(p, q);

    return output;
};