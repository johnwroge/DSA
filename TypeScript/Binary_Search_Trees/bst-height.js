function BinarySearchTree(value) {
  this.value = value;
  this.right = null;
  this.left = null;
}

/*

Find the tallest height of a binary search tree.

Ex. the tallest height of:

     4
   /   \
  2     7
 / \     \
1   3     9
         /
        8

is 3, because the tallest height of the tree connects the numbers 4 - 7 - 9 - 8
and has 3 links.

*/
//leetcode maximum depth of binary tree 

// const bstHeight = (tree,) => {
// if (!tree) return -1;
// let left = bstHeight(tree.left);
// let right = bstHeight(tree.right);
// return left > right ? left + 1 : right + 1; 
// };

const bstHeight = tree => {
  if (!tree) return -1;
  return Math.max(bstHeight(tree.left), bstHeight(tree.right)) + 1;
}




/*
  Extension:

  Write a function to see if a binary tree is "superbalanced".
  An empty tree is balanced. A non-empty binary tree T is balanced if:
    1) Left subtree of T is balanced
    2) Right subtree of T is balanced
    3) The difference between heights of left subtree and right subtree is not more than 1.
  example: http://www.geeksforgeeks.org/wp-content/uploads/balanced_tree.GIF

  A superbalanced tree is a tree that is balanced at every subtree level as well.

  Ex. 
        4                       4
      /   \                   /   \
     2     7                2       7
    / \     \             /  \     /  \
   1   3     9           1    3   5    9
            /                         /
           8                         8

  The tree on the left is balanced - height of left side is 2, height of right side is 3.
  But, it is not superbalanced since for the 7 subtree, height of left is 0, height of right is 2.
  
  The tree on the right is superbalanced since the difference in height is not more than 1 at any given subtree.
 */

const superbalanced = tree => {

  //check if tree is null or undefined, return true
  if (!tree) return true;

  if (Math.abs(bstHeight(tree.right) - bstHeight(tree.left)) > 1) return false;

  return (superbalanced(tree.right) && superbalanced(tree.left));

};

module.exports = {BinarySearchTree, bstHeight, superbalanced};
