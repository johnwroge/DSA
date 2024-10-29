
/*
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


*/

//soln 1
var diameterOfBinaryTree = function(root) {
    if (!root) return 0; 
    //create a max count initialized at 0
    let maxCount = 0;
    //create helper function that traverses through tree
    function dfs (node){
        if (!node) return 0;
        //create a left 
        let left = dfs(node.left);
        //create a right
        let right = dfs(node.right);
        //reassign the max count to be the maximum of left + right or current max
        maxCount = Math.max(maxCount, left + right);
        
        return Math.max(left, right) + 1;
    }
    //call the helper function with the root
    dfs(root);
    //return the max count
    return maxCount
};


//sol2 

var diameterOfBinaryTree = function(root, max = [0]) {
    diameterOfTree(root, max);

    return max[0];
};

const diameterOfTree = (root, max) => {
    const isBaseCase = root === null;
    if (isBaseCase) return 0;

    return dfs(root, max);
}

const dfs = (root, max) => {
    const left = diameterOfTree2(root.left, max);
    const right = diameterOfTree2(root.right, max);

    const diameter = left + right;
    max[0] = Math.max(max[0], diameter);

    const height = Math.max(left, right);

    return height + 1;
}