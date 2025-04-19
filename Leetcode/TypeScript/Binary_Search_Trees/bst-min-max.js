function BinarySearchTree(value) {
  this.value = value;
  this.right = null;
  this.left = null;
}


/*

Given the root of a binary search tree, determine the difference of the maximum
and minimum value.

Note that the function signature is NOT defined as a method on the
BinarySearchTree prototype. Instead, we provide the root as an argument to the
function.

Ex:

     4
   /   \
  2     7
 / \     \
1   3     9
         /
        8

returns 8, becuase 9 - 1 = 8

*/

const bstMinMax = root => {
let current;
//create a max variable
let min = Infinity;
//create a min variable
let max = -Infinity;
//create a queue containing the root
const queue = [root];
//loop while there are items in queue
  while (queue.length){
//assign a current to be the shifted queue
    current = queue.shift();
//check if there is a current left, push into queue
    if (current.left) queue.push(current.left);
//peform callback on current
  //reassign min to be current.val or previous min
    max = Math.max(current.value, max);
  //reassign max to current.val or previous max
    min = Math.min(current.value, min)
//check if there is current.right, push into queue
    if (current.right) queue.push(current.right);
  }
//return max minus min
return max - min; 
  
};





/*

Extension: (not necessarily related in technique to above problem, but
nevertheless still a BST problem)

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes "p" and "q" in the BST. Return the LCA node itself.

//in bst we always have left nodes less than and right nodes are greater than parent node
//a binary tree doesn't have those less than/greater than rules 

Ex:

     4
   /   \
  2     7
 / \     \
1   3     9
         /
        8

The LCA of node 1 and node 3 is node 2.
The LCA of node 8 and node 9 is node 9.
The LCA of node 2 and node 8 is node 4.

*/

const lowestCommonAncestor = (root, p, q) => {

  while (root !== null) {
    const isGreater = (root.val < p.val) && (root.val < q.val)
    if (isGreater) {
        root = root.right;
        continue;
    }

    const isLess = (p.val < root.val) && (q.val < root.val);;
    if (isLess) {
        root = root.left;
        continue;
    }

    break;
}

return root;
};

module.exports = {BinarySearchTree, bstMinMax, lowestCommonAncestor};
