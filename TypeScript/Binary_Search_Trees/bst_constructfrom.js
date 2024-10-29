/*
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
12.1K
358
Companies
Given two integer arrays preorder and inorder where preorder is
 the preorder traversal of a binary tree and inorder is the inorder
  traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 
Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
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
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
 var buildTree = function(P, I) {
    let M = new Map()
    for (let i = 0; i < I.length; i++)
        M.set(I[i], i)
    return splitTree(P, M, 0, 0, I.length-1)
};

var splitTree = function(P, M, pix, ileft, iright) {
    let rval = P[pix],
        root = new TreeNode(rval),
        imid = M.get(rval)
    if (imid > ileft)
        root.left = splitTree(P, M, pix+1, ileft, imid-1)
    if (imid < iright)
        root.right = splitTree(P, M, pix+imid-ileft+1, imid+1, iright)
    return root
}


var buildTree = function(preorder, inorder) {
	//create dfs helper function that takes a start, end and index parameter
		function dfs(start,end,index){
            //base case: if start is greater than end and preorder length matches index -> return null
			  if(start>end || preorder.length === index){
				return null;
			  }
              //create a new treenode with the value at the key of index
			  let tree = new TreeNode(preorder[index]);
              //create a getindex variable and assign to the index 
			  let getIndex = inorder.indexOf(preorder[index]);
			  tree.left = getIndex!==-1?dfs(start,getIndex-1,index+1):null;
			  tree.right = getIndex!==-1?dfs(getIndex+1,end,index+1):null;
			  preorder.splice(index,1);
			  return tree;
		}    
return dfs(0,preorder.length,0);
}