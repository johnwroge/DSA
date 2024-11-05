
'''
951. Flip Equivalent Binary Trees
Solved
Medium
Topics
Companies
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

 

Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (not root1 and root2):
            return False
        if root1.val != root2.val:
            return False
        
        if root1 and root2 and root1.left and root2.right:
            if root1.left.val == root2.right.val:
                root1.left, root1.right = root1.right, root1.left
        if root1 and root2 and root1.right and root2.left:
            if root1.right.val == root2.left.val:
                root1.left, root1.right = root1.right, root1.left
        
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)