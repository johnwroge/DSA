
/*
Given a binary tree, determine if it is 
height-balanced

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
*/



var isBalanced = function(root) {
    // If the tree is empty, we can say it’s balanced...
    if (root == null)  return true;
    // Height Function will return -1, when it’s an unbalanced tree...
	if (Height(root) == -1)  return false;
	return true;
}
// Create a function to return the “height” of a current subtree using recursion...
var Height = function(root) {
    // Base case...
	if (root == null)  return 0;
    // Height of left subtree...
	let leftHeight = Height(root.left);
    // Height of height subtree...
	let rightHight = Height(root.right);
    // In case of left subtree or right subtree unbalanced, return -1...
	if (leftHeight == -1 || rightHight == -1)  return -1;
    // If their heights differ by more than ‘1’, return -1...
    if (Math.abs(leftHeight - rightHight) > 1)  return -1;
    // Otherwise, return the height of this subtree as max(leftHeight, rightHight) + 1...
	return Math.max(leftHeight, rightHight) + 1;
};

//easier optimized solution 

var isBalanced = (root) => {
let res = true; 
const maxDepth = (node) => {
    if (!node) return 0;
    let l = maxDepth(node.left), r = maxDepth(node.right);
    if (Math.abs(l - r) > 1) res = false;
    return 1 + Math.max(l, r)
}
maxDepth(root);
return res; 
}