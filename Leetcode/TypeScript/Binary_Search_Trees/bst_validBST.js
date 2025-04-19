/*
98. Validate Binary Search Tree
Medium
13.9K
1.1K
Companies
Given the root of a binary tree, determine if it is a valid 
binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater
than the node's key. Both the left and right subtrees must 
also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
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
 * @return {boolean}
 */
// var isValidBST = function(root) {
//     const dfs = (node, min, max) => {
//     if (!node) return true; 

//     if (node.val <= min || node.val >= max){
//     return false; 
//      }
//      return dfs(node.left, min, node.val) && dfs(node.right, node.val, max)
//       }
//   return dfs (root, -Infinity, Infinity);
// };

var isValidBST3 = function(root, minimum, maximum) {
    // Base case: root is null...
    if(root == null) return true;
    // If the value of root is less or equal to minimum...
    // Or If the value of root is greater or equal to maximum...
    if(root.val <= minimum || root.val >= maximum) return false;
    // Recursively call the function for the left and right subtree...
    return isValidBST(root.left, minimum, root.val) && isValidBST(root.right, root.val, maximum);
};


const isValidBST1 = (root) => {

    //create a dfs helper function that takes a node, a min and max value
    const dfs = (node, min, max) => {
        //if there is node, return true (traversed the branch successfully)
        if (!node) return true; 
        //base case: if node.val is less than min or node.val is greater than max
        if (node.val <= min || node.val >= max) return false; 
            //return false;
        //return dfs helper with min params, AND dfs helper with max params
        return dfs(node.left, min, node.val) && dfs(node.right, node.val, max );

    }
//return dfs passing in root, -infinity and infinity
return dfs(root, -Infinity, Infinity);
}

const isValidBST = (root, min, max) => {
    if (!root) return true;

    if(root.val <= min || root.val >= max) return false;

    return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max)
}





