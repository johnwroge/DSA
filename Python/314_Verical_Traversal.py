'''
314. Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7



Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

'''

'''
solution keep track of position with hashmap
using breadth first search
hash = {0: [3, 15], -1: [9] 1: [15, 20], 2: [7]}
by starting at root 0: root [(0, 3), (-1, 9), (1, 20), (15, 0), (7, 2)]
sort the keys and then output each of those positions
'''

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = deque([(root, 0)])
        positions = {}  
        while len(Q) > 0:
            length = len(Q)
            for _ in range(length):
                node, index = Q.popleft()
                if index not in positions:
                    positions[index] = []
                positions[index].append(node.val)
                if node.left:
                    Q.append((node.left, index - 1))
                if node.right:
                    Q.append((node.right, index + 1))
        verticals = []
        for i in sorted(positions.keys()):
            verticals.append(positions[i])
        return verticals
                



# Test Cases

# Example Tree:
#       3
#      / \
#     9   20
#         / \
#        15  7
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
# Expected Output: [[9], [3, 15], [20], [7]]

# Single node tree
root2 = TreeNode(1)
# Expected Output: [[1]]

# Left skewed tree:
#       1
#      /
#     2
#    /
#   3
#  /
# 4
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.left.left = TreeNode(3)
root3.left.left.left = TreeNode(4)
# Expected Output: [[4], [3], [2], [1]]

# Right skewed tree:
# 1
#  \
#   2
#    \
#     3
#      \
#       4
root4 = TreeNode(1)
root4.right = TreeNode(2)
root4.right.right = TreeNode(3)
root4.right.right.right = TreeNode(4)
# Expected Output: [[1], [2], [3], [4]]

# Mixed tree:
#       1
#      / \
#     2   3
#      \   \
#       4   5
root5 = TreeNode(1)
root5.left = TreeNode(2, None, TreeNode(4))
root5.right = TreeNode(3, None, TreeNode(5))
# Expected Output: [[2], [1, 4], [3], [5]]

# Complex tree with overlapping nodes:
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
root6 = TreeNode(1)
root6.left = TreeNode(2, TreeNode(4), TreeNode(5))
root6.right = TreeNode(3, TreeNode(6), TreeNode(7))
# Expected Output: [[4], [2], [1, 5, 6], [3], [7]]

# List of test cases with expected outputs
test_cases = [root1, root2, root3, root4, root5, root6]

for test in test_cases:
    solution = Solution()
    print(solution.verticalOrder(test))