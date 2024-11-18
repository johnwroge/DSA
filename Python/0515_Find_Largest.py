'''
515. Find Largest Value in Each Tree Row
Solved
Medium
Topics
Companies
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        Q = deque([root])
        res = []
        while len(Q):
            n = len(Q)
            maxi = float('-inf')
            for _ in range(n):
                node = Q.popleft()
                if node:
                    maxi = max(maxi, node.val)
                if node and node.left: Q.append(node.left)
                if node and node.right: Q.append(node.right)
            res.append(maxi)
        return res


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root:
            q.append(root)
        res = []

        while q:
            rowmax = -float('inf')
            nextq = deque()
            for node in q:
                rowmax=max(rowmax,node.val)
                if node.left:
                    nextq.append(node.left)
                if node.right:
                    nextq.append(node.right)
            res.append(rowmax)
            q = nextq
        
        return res