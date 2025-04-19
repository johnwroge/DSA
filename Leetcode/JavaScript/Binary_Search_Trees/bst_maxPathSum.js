/*
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
 in the sequence has an edge connecting them. A node can only appear in the sequence at 
 most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


*/

/**
 * https://leetcode.com/problems/binary-tree-maximum-path-sum/
 * Time O(N) | Space O(H)
 * @param {TreeNode} root
 * @return {number}
 */
//create an implicit parameter of an array containing -negative (initial maxPathSum)
 var maxPathSum = function(root, maxValue = [ -Infinity ]) {
    //invoke pathSum helper function with root and current max value
    pathSum(root, maxValue);
    //return final max value at index 0
    return maxValue[0];
};

//create helper function that takes a root and maxValue
const pathSum = (root, maxValue) => {
    //base case: if root is null then return 0
    const isBaseCase = root === null;
    if (isBaseCase) return 0;
    //return the function invocation of dfs passing in root and dfs 
    return dfs(root, maxValue);
}

//create dfs helper function that takes a node and a max value
const dfs = (node, maxValue) => {
    //create a variable left and assign to the maximum of either 0, or the recursive call to previous helper 
    //passing in node.left and the curretn max value
    const left = Math.max(0, pathSum(node.left, maxValue));
     //create a variable right and assign to the maximum of either 0, or the recursive call to previous helper 
    //passing in node.right and the curretn max value
    const right = Math.max(0, pathSum(node.right, maxValue));
    //create a sum variable and assign to the left plus right plus current node value
    const sum = left + right + node.val;
    //reassign the max value at the 0th index to be the maximum of either maxValue at 0 index or the sum
    maxValue[0] = Math.max(maxValue[0], sum);
    //return the maximum of either the left or right ADDED to the current node.val 
    return Math.max(left, right) + node.val;
}



























