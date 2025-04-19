/*
235. Lowest Common Ancestor of a Binary Search Tree
Medium
8.8K
248
Companies
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a 
    node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself 
according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
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

//T O(n) S O(H) 
 var lowestCommonAncestor = function(root, p, q) {
    //create a conditional variable checking if the p.val is less than root.val AND q.val is less than root.val
    const isGreater = (p.val < root.val) && (q.val < root.val);
    //if this conditional variable is true, 
        //return the recursive call to the original function with root.left, p, and q
    if (isGreater) return lowestCommonAncestor(root.left, p, q);

    //create a conditional statement checking if p.val and q.val are greater than root.val
    const isLess = (root.val < p.val) && (root.val < q.val);
    //if condtional is true, return recursive call to original function with root.right, p and q
    if (isLess) return lowestCommonAncestor(root.right, p, q);

    //return the current root
    return root;
};

//T O(N) S O(1)

var lowestCommonAncestor2 = function(root, p, q) {

    //create a loop while the root isn't null
    while (root.val){
        //create condtional statement check if p.val and q.val are greater than root.val
        let isGreater = (p.val > root.val && q.val > root.val);
        //if true ->
        if (isGreater){
            //reassign the root to be root.right 
            root = root.right;
            //continue
            continue; 
        }
        //create condtional statement check if p.val and q.val are less than root.val
        let isLess = p.val < root.val && q.val < root.val;
        //if true ->
        if (isLess){
            //reassign the root to be root.left 
            root = root.left;
            //continue
            continue;
        }
        //otherwise if neither -> break out of while loop
        break; 
    }
//return the current root
return root; 

}