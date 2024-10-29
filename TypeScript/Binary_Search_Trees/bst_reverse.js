/*
Given the root of a binary tree, invert the tree, and return its root.
1
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
2
Input: root = [2,1,3]
Output: [2,3,1]
3
Input: root = []
Output: []


The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
*/

/***
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree1 = function(root) {

    if (!root) return root; 

 invertTree1(root.left);
 invertTree1(root.right);

 [root.left, root.right] = [root.right, root.left];


  
return root; 
    
};

const invertTree2 = (root) => {
     // Base case...
     if(root == null){
        return root
    }
    // Call the function recursively for the left subtree...
    invertTree(root.left)
    // Call the function recursively for the right subtree...
    invertTree(root.right)
    // swapping process...
    const curr = root.left
    root.left = root.right
    root.right = curr
    return root         //
}

var invertTree3 = (root) => {
    const isBaseCase = root === null;
    if (isBaseCase) return root;

    return dfs(root);
}

const dfs = (root) => {
    const left = invertTree(root.left);
    const right = invertTree(root.right);

    root.left = right;
    root.right = left;

    return root;
}