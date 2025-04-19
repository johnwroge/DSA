'''
2458. Height of Binary Tree After Subtree Removal Queries

You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
 

Example 1:


Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
Output: [2]
Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).
Example 2:


Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
Output: [3,2,3,2]
Explanation: We have the following queries:
- Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
- Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
- Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
- Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
m == queries.length
1 <= m <= min(n, 104)
1 <= queries[i] <= n
queries[i] != root.val

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# brute force leading to TLE 

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        result = [0] * len(queries)
  
        def dfs(node, height, value):
            nonlocal result
            if not node:
                return height - 1
            if node.val == value:
                return height - 1
            return max(dfs(node.left, height + 1, value), dfs(node.right, height + 1, value)) 
        
        for i in range(len(queries)):
            height = dfs(root, 0, queries[i])
            result[i] = height
        
        return result


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Store height for each node
        heights = {}
        
        # First get height of each node
        def get_height(node):
            if not node:
                return 0
            height = 1 + max(get_height(node.left), get_height(node.right))
            heights[node.val] = height
            return height
            
        get_height(root)
        
        # Store max possible height for each node value if that node were removed
        max_heights = {}
        
        def dfs(node, depth, max_height_without_curr):
            if not node:
                return
                
            # Store current max height possible if this node is removed
            max_heights[node.val] = max_height_without_curr
            
            # Calculate max height possible for left child
            # It's either the height through right child + current depth
            # or the max height possible without current node
            left_max = depth
            if node.right:
                left_max = max(left_max, depth + heights[node.right.val])
            left_max = max(left_max, max_height_without_curr)
            
            # Similarly for right child
            right_max = depth
            if node.left:
                right_max = max(right_max, depth + heights[node.left.val])
            right_max = max(right_max, max_height_without_curr)
            
            # Recurse
            dfs(node.left, depth + 1, left_max)
            dfs(node.right, depth + 1, right_max)
            
        dfs(root, 0, 0)
        
        return [max_heights[q] for q in queries]

# Solution 1 

class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        max_height_after_removal = [0] * 100001
        self.current_max_height = 0

        def _traverse_left_to_right(node, current_height):
            if not node:
                return

            # Store the maximum height if this node were removed
            max_height_after_removal[node.val] = self.current_max_height

            # Update the current maximum height
            self.current_max_height = max(
                self.current_max_height, current_height
            )

            # Traverse left subtree first, then right
            _traverse_left_to_right(node.left, current_height + 1)
            _traverse_left_to_right(node.right, current_height + 1)

        def _traverse_right_to_left(node, current_height):
            if not node:
                return

            # Update the maximum height if this node were removed
            max_height_after_removal[node.val] = max(
                max_height_after_removal[node.val], self.current_max_height
            )

            # Update the current maximum height
            self.current_max_height = max(
                current_height, self.current_max_height
            )

            # Traverse right subtree first, then left
            _traverse_right_to_left(node.right, current_height + 1)
            _traverse_right_to_left(node.left, current_height + 1)

        _traverse_left_to_right(root, 0)
        self.current_max_height = 0  # Reset for the second traversal
        _traverse_right_to_left(root, 0)

        # Process queries and build the result list
        return [max_height_after_removal[q] for q in queries]
            

# Single Traversal 

class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        result_map = {}
        height_cache = {}

        # Function to calculate the height of the tree
        def _height(node):
            if not node:
                return -1

            # Return cached height if already calculated
            if node in height_cache:
                return height_cache[node]

            h = 1 + max(_height(node.left), _height(node.right))
            height_cache[node] = h
            return h

        # DFS to precompute the maximum values after removing the subtree
        def _dfs(node, depth, max_val):
            if not node:
                return

            result_map[node.val] = max_val

            # Traverse left and right subtrees while updating max values
            _dfs(
                node.left,
                depth + 1,
                max(max_val, depth + 1 + _height(node.right)),
            )
            _dfs(
                node.right,
                depth + 1,
                max(max_val, depth + 1 + _height(node.left)),
            )

        # Run DFS to fill result_map with maximum heights after each query
        _dfs(root, 0, 0)

        # Build the result array based on the queries
        return [result_map[q] for q in queries]
    

class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        # Dictionary to store the index of each node value
        node_index_map = {}

        # Dictionary to store the number of nodes in the subtree for each node
        subtree_size = {}

        # Lists to store node depths and maximum depths from left and right
        node_depths = []
        max_depth_from_left = []
        max_depth_from_right = []

        # Perform DFS to populate node_index_map and node_depths
        self._dfs(root, 0, node_index_map, node_depths)

        total_nodes = len(node_depths)

        # Calculate subtree sizes
        self._calculate_subtree_size(root, subtree_size)

        # Calculate maximum depths from left and right
        max_depth_from_left.append(node_depths[0])
        max_depth_from_right.append(node_depths[-1])

        for i in range(1, total_nodes):
            max_depth_from_left.append(
                max(max_depth_from_left[i - 1], node_depths[i])
            )
            max_depth_from_right.append(
                max(
                    max_depth_from_right[i - 1],
                    node_depths[total_nodes - i - 1],
                )
            )

        max_depth_from_right.reverse()

        # Process queries
        results = []
        for query_node in queries:
            start_index = node_index_map[query_node] - 1
            end_index = start_index + 1 + subtree_size[query_node]

            max_depth = max_depth_from_left[start_index]
            if end_index < total_nodes:
                max_depth = max(max_depth, max_depth_from_right[end_index])

            results.append(max_depth)

        return results

    # Depth-first search to populate node_index_map and node_depths
    def _dfs(self, root, depth, node_index_map, node_depths):
        if not root:
            return

        node_index_map[root.val] = len(node_depths)
        node_depths.append(depth)

        self._dfs(root.left, depth + 1, node_index_map, node_depths)
        self._dfs(root.right, depth + 1, node_index_map, node_depths)

    # Calculate the size of the subtree for each node
    def _calculate_subtree_size(self, root, subtree_size):
        if not root:
            return 0

        left_size = self._calculate_subtree_size(root.left, subtree_size)
        right_size = self._calculate_subtree_size(root.right, subtree_size)

        total_size = left_size + right_size + 1
        subtree_size[root.val] = total_size

        return total_size
    




class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        # Lists and dictionaries to store tree information
        euler_tour = []
        node_heights = {}
        first_occurrence = {}
        last_occurrence = {}

        # Depth-first search to build the Euler tour and store node information
        def _dfs(root, height):
            if not root:
                return

            node_heights[root.val] = height
            first_occurrence[root.val] = len(euler_tour)
            euler_tour.append(root.val)

            _dfs(root.left, height + 1)
            _dfs(root.right, height + 1)

            last_occurrence[root.val] = len(euler_tour)
            euler_tour.append(root.val)

        # Perform DFS to build Euler tour and node information
        _dfs(root, 0)

        tour_size = len(euler_tour)
        max_depth_left = [0] * tour_size
        max_depth_right = [0] * tour_size

        # Initialize the first and last elements of max_height arrays
        max_depth_left[0] = max_depth_right[-1] = node_heights[root.val]

        # Build max_depth_left and max_depth_right arrays
        for i in range(1, tour_size):
            max_depth_left[i] = max(
                max_depth_left[i - 1], node_heights[euler_tour[i]]
            )

        for i in range(tour_size - 2, -1, -1):
            max_depth_right[i] = max(
                max_depth_right[i + 1], node_heights[euler_tour[i]]
            )

        # Process queries
        return [
            max(
                (
                    max_depth_left[first_occurrence[q] - 1]
                    if first_occurrence[q] > 0
                    else 0
                ),
                (
                    max_depth_right[last_occurrence[q] + 1]
                    if last_occurrence[q] < tour_size - 1
                    else 0
                ),
            )
            for q in queries
        ]
    


class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        # Dictionaries to store node depths and heights
        node_depths = {}
        subtree_heights = {}

        # Dictionaries to store the first and second largest heights at each level
        first_largest_height = {}
        second_largest_height = {}

        # Depth-first search to calculate node depths and subtree heights
        def _dfs(node, level):
            if not node:
                return 0

            node_depths[node.val] = level

            # Calculate the height of the current subtree
            left_height = _dfs(node.left, level + 1)
            right_height = _dfs(node.right, level + 1)
            current_height = 1 + max(left_height, right_height)

            subtree_heights[node.val] = current_height

            # Update the largest and second largest heights at the current level
            if current_height > first_largest_height.get(level, 0):
                second_largest_height[level] = first_largest_height.get(
                    level, 0
                )
                first_largest_height[level] = current_height
            elif current_height > second_largest_height.get(level, 0):
                second_largest_height[level] = current_height

            return current_height

        _dfs(root, 0)

        # Process each query
        return [
            node_depths[q]
            + (
                second_largest_height.get(node_depths[q], 0)
                if subtree_heights[q] == first_largest_height[node_depths[q]]
                else first_largest_height.get(node_depths[q], 0)
            )
            - 1
            for q in queries
        ]