"""
LeetCode Problems where Tree Properties can be applied:

104. Maximum Depth of Binary Tree
111. Minimum Depth of Binary Tree
110. Balanced Binary Tree
543. Diameter of Binary Tree
124. Binary Tree Maximum Path Sum
98. Validate Binary Search Tree
100. Same Tree
101. Symmetric Tree
226. Invert Binary Tree
114. Flatten Binary Tree to Linked List
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# =============================================================================
# BASIC TREE PROPERTIES
# =============================================================================

def max_depth(root):
    """
    LeetCode 104: Maximum Depth of Binary Tree
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))

def min_depth(root):
    """
    LeetCode 111: Minimum Depth of Binary Tree
    Minimum depth to a leaf node
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    # If only one subtree exists, go to that subtree
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    
    # Both subtrees exist
    return 1 + min(min_depth(root.left), min_depth(root.right))

def is_balanced(root):
    """
    LeetCode 110: Balanced Binary Tree
    Check if tree is height-balanced
    
    Time: O(n), Space: O(h)
    """
    def check_balance(node):
        if not node:
            return 0, True
        
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)
        
        # Check if current subtree is balanced
        balanced = (left_balanced and right_balanced and 
                   abs(left_height - right_height) <= 1)
        
        height = 1 + max(left_height, right_height)
        
        return height, balanced
    
    _, balanced = check_balance(root)
    return balanced

def diameter(root):
    """
    LeetCode 543: Diameter of Binary Tree
    Longest path between any two nodes
    
    Time: O(n), Space: O(h)
    """
    def dfs(node):
        if not node:
            return 0
        
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        
        # Update global diameter
        self.diameter = max(self.diameter, left_depth + right_depth)
        
        # Return depth of this subtree
        return 1 + max(left_depth, right_depth)
    
    self.diameter = 0
    dfs(root)
    return self.diameter

def count_nodes(root):
    """
    Count total number of nodes
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def count_leaves(root):
    """
    Count number of leaf nodes
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1
    
    return count_leaves(root.left) + count_leaves(root.right)

# =============================================================================
# TREE VALIDATION
# =============================================================================

def is_valid_bst(root):
    """
    LeetCode 98: Validate Binary Search Tree
    
    Time: O(n), Space: O(h)
    """
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

def is_same_tree(p, q):
    """
    LeetCode 100: Same Tree
    Check if two trees are identical
    
    Time: O(min(m,n)), Space: O(min(m,n))
    """
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))

def is_symmetric(root):
    """
    LeetCode 101: Symmetric Tree
    Check if tree is symmetric around center
    
    Time: O(n), Space: O(h)
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    
    return is_mirror(root.left, root.right) if root else True

def is_complete_tree(root):
    """
    Check if tree is complete (all levels filled except possibly last)
    
    Time: O(n), Space: O(w) where w is max width
    """
    if not root:
        return True
    
    from collections import deque
    queue = deque([root])
    found_none = False
    
    while queue:
        node = queue.popleft()
        
        if not node:
            found_none = True
        else:
            if found_none:  # Found node after None
                return False
            
            queue.append(node.left)
            queue.append(node.right)
    
    return True

# =============================================================================
# TREE TRANSFORMATIONS
# =============================================================================

def invert_tree(root):
    """
    LeetCode 226: Invert Binary Tree
    Mirror the tree
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return None
    
    # Swap children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root

def flatten_to_linked_list(root):
    """
    LeetCode 114: Flatten Binary Tree to Linked List
    Flatten to preorder linked list
    
    Time: O(n), Space: O(h)
    """
    def flatten(node):
        if not node:
            return None
        
        # Flatten subtrees and get their tails
        left_tail = flatten(node.left)
        right_tail = flatten(node.right)
        
        # If left subtree exists, insert it between root and right subtree
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        
        # Return the tail of current tree
        return right_tail or left_tail or node
    
    flatten(root)

# =============================================================================
# PATH PROBLEMS
# =============================================================================

def max_path_sum(root):
    """
    LeetCode 124: Binary Tree Maximum Path Sum
    Maximum path sum between any two nodes
    
    Time: O(n), Space: O(h)
    """
    def max_gain(node):
        if not node:
            return 0
        
        # Maximum gain from left and right subtrees
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Path through current node
        current_max = node.val + left_gain + right_gain
        
        # Update global maximum
        self.max_sum = max(self.max_sum, current_max)
        
        # Return maximum gain from this node (single path)
        return node.val + max(left_gain, right_gain)
    
    self.max_sum = float('-inf')
    max_gain(root)
    return self.max_sum

def has_path_sum(root, target_sum):
    """
    Check if tree has root-to-leaf path with given sum
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return False
    
    # Leaf node
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Check both subtrees with reduced target
    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or 
            has_path_sum(root.right, remaining))

def all_path_sums(root, target_sum):
    """
    Find all root-to-leaf paths with given sum
    
    Time: O(n), Space: O(h)
    """
    def dfs(node, remaining, path, result):
        if not node:
            return
        
        path.append(node.val)
        
        # Leaf node
        if not node.left and not node.right and remaining == node.val:
            result.append(path[:])
        
        # Continue search
        dfs(node.left, remaining - node.val, path, result)
        dfs(node.right, remaining - node.val, path, result)
        
        path.pop()  # Backtrack
    
    result = []
    dfs(root, target_sum, [], result)
    return result

# =============================================================================
# ADVANCED PROPERTIES
# =============================================================================

def width_of_tree(root):
    """
    Maximum width of tree at any level
    
    Time: O(n), Space: O(w)
    """
    if not root:
        return 0
    
    from collections import deque
    queue = deque([(root, 0)])  # (node, position)
    max_width = 0
    
    while queue:
        level_size = len(queue)
        _, first_pos = queue[0]
        _, last_pos = queue[-1]
        
        max_width = max(max_width, last_pos - first_pos + 1)
        
        for _ in range(level_size):
            node, pos = queue.popleft()
            
            if node.left:
                queue.append((node.left, 2 * pos))
            if node.right:
                queue.append((node.right, 2 * pos + 1))
    
    return max_width

def tree_sum(root):
    """
    Sum of all node values
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    return root.val + tree_sum(root.left) + tree_sum(root.right)

def level_sums(root):
    """
    Sum of nodes at each level
    
    Time: O(n), Space: O(w)
    """
    if not root:
        return []
    
    from collections import deque
    queue = deque([root])
    sums = []
    
    while queue:
        level_size = len(queue)
        level_sum = 0
        
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        sums.append(level_sum)
    
    return sums

# =============================================================================
# GENERIC PROPERTY TEMPLATES
# =============================================================================

def tree_property_template(root, property_func, combine_func, base_case):
    """
    Generic template for computing tree properties
    
    Args:
        root: Tree root
        property_func: Function to compute property at each node
        combine_func: Function to combine results from children
        base_case: Value to return for None nodes
    """
    if not root:
        return base_case
    
    left_result = tree_property_template(root.left, property_func, combine_func, base_case)
    right_result = tree_property_template(root.right, property_func, combine_func, base_case)
    
    return property_func(root, left_result, right_result, combine_func)

def validate_tree_property(root, condition_func):
    """
    Generic template for validating tree properties
    
    Args:
        root: Tree root
        condition_func: Function that checks condition at each node
    """
    def validate(node):
        if not node:
            return True
        
        if not condition_func(node):
            return False
        
        return validate(node.left) and validate(node.right)
    
    return validate(root)

def tree_metrics(root):
    """
    Compute multiple tree metrics in single traversal
    
    Returns: (height, node_count, leaf_count, is_balanced)
    """
    def compute_metrics(node):
        if not node:
            return 0, 0, 0, True
        
        left_height, left_nodes, left_leaves, left_balanced = compute_metrics(node.left)
        right_height, right_nodes, right_leaves, right_balanced = compute_metrics(node.right)
        
        height = 1 + max(left_height, right_height)
        node_count = 1 + left_nodes + right_nodes
        
        # Count leaves
        if not node.left and not node.right:
            leaf_count = 1
        else:
            leaf_count = left_leaves + right_leaves
        
        # Check balance
        is_balanced = (left_balanced and right_balanced and 
                      abs(left_height - right_height) <= 1)
        
        return height, node_count, leaf_count, is_balanced
    
    return compute_metrics(root)