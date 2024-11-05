/*
236. Lowest Common Ancestor of a Binary Tree
Solved
Medium
Topics
Companies
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow
a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
*/



/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root: any, p: any, q: any): any {
    if (!root || root === p || q === root) return root
    let left = lowestCommonAncestor(root.left, p, q)
    let right = lowestCommonAncestor(root.right, p, q)
    return left && right ? root : left || right
};

function lowestCommonAncestor2(root: TreeNode | null, p: TreeNode, q: TreeNode): TreeNode | null{
    if (root === null) return null;
    
    const leftHasPQ = lowestCommonAncestor(root.left, p, q);
    const rightHasPQ = lowestCommonAncestor(root.right, p, q);
  
    if ((leftHasPQ && rightHasPQ) || (root.val === p.val || root.val === q.val))
      return root;
  
    return leftHasPQ || rightHasPQ;
  };
