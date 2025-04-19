function BinarySearchTree(value) {
  this.value = value;
  this.right = null;
  this.left = null;
}

/*

Given the root of a binary search tree, determine the sum of all the values.
Note that the function signature is NOT defined as a method on the
BinarySearchTree prototype. Instead, we provide the root as an argument to the
function.
*/

const bstSum = root => {
  //create a sum variable and assign to 0
  let sum = 0;
  let current;
  //edge: check if root is null, return the sum
  if (!root) return sum; 
  //create a queue to store nodes initialized the root
  const queue = [root];
  //traverse through the tree while queue contains items
  while (queue.length){
    //assign the current to be the shifted queue
    current = queue.shift();
    //add the value to sum
    sum += current.value;
    //check if there is a left, if true -> push into the queue
    if (current.left) queue.push(current.left);
    //check if there is a right, if true -> push into the queue
    if (current.right) queue.push(current.right)
  }
    //return sum
    return sum;

};

/*

Extension:
Given the root of a binary search tree, reverse the binary search tree in-place
and return the root. Reverse the tree so that for each node, every number on the
left is greater and every number on the right is lesser.

For example, the original tree:

     4
   /   \
  2     7
 / \     \
1   3     9
         /
        8

reverses to:

     4
   /   \
  7     2
 /     / \
9     3   1
 \
  8

Do this in-place, so that we never use the BinarySearchTree constructor to
create any new nodes in memory.

Note that the function signature is NOT defined as a method on the
BinarySearchTree prototype. Instead, we provide the root as an argument to the
function.

*/

const bstReverse = root => {
  if(!root) return;
  [root.left, root.right] = [root.right, root.left];
  bstReverse(root.left);
  bstReverse(root.right);
  return root;
};

module.exports = {BinarySearchTree, bstSum, bstReverse};
