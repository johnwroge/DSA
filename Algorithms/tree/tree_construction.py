"""
LeetCode Problems where Tree Construction can be applied:

105. Construct Binary Tree from Preorder and Inorder Traversal
106. Construct Binary Tree from Inorder and Postorder Traversal
108. Convert Sorted Array to Binary Search Tree
109. Convert Sorted List to Binary Search Tree
297. Serialize and Deserialize Binary Tree
449. Serialize and Deserialize BST
889. Construct Binary Tree from Preorder and Postorder Traversal
1008. Construct Binary Search Tree from Preorder Traversal
"""

from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# =============================================================================
# CONSTRUCT FROM TRAVERSALS
# =============================================================================

def build_tree_pre_in(preorder, inorder):
    """
    LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal
    
    Time: O(n), Space: O(n)
    """
    if not preorder or not inorder:
        return None
    
    # Build index map for inorder for O(1) lookup
    inorder_map = {val: i for i, val in enumerate(inorder)}
    self.pre_idx = 0
    
    def build(left, right):
        if left > right:
            return None
        
        # Root is next element in preorder
        root_val = preorder[self.pre_idx]
        self.pre_idx += 1
        root = TreeNode(root_val)
        
        # Find root position in inorder
        root_pos = inorder_map[root_val]
        
        # Build left subtree first (preorder: root -> left -> right)
        root.left = build(left, root_pos - 1)
        root.right = build(root_pos + 1, right)
        
        return root
    
    return build(0, len(inorder) - 1)

def build_tree_in_post(inorder, postorder):
    """
    LeetCode 106: Construct Binary Tree from Inorder and Postorder Traversal
    
    Time: O(n), Space: O(n)
    """
    if not inorder or not postorder:
        return None
    
    inorder_map = {val: i for i, val in enumerate(inorder)}
    self.post_idx = len(postorder) - 1
    
    def build(left, right):
        if left > right:
            return None
        
        # Root is next element from end of postorder
        root_val = postorder[self.post_idx]
        self.post_idx -= 1
        root = TreeNode(root_val)
        
        root_pos = inorder_map[root_val]
        
        # Build right subtree first (postorder: left -> right -> root)
        root.right = build(root_pos + 1, right)
        root.left = build(left, root_pos - 1)
        
        return root
    
    return build(0, len(inorder) - 1)

def build_tree_pre_post(preorder, postorder):
    """
    LeetCode 889: Construct Binary Tree from Preorder and Postorder Traversal
    Note: This assumes the tree is full binary tree for unique construction
    
    Time: O(n), Space: O(n)
    """
    if not preorder or not postorder:
        return None
    
    postorder_map = {val: i for i, val in enumerate(postorder)}
    self.pre_idx = 0
    
    def build(left, right):
        if left > right:
            return None
        
        root_val = preorder[self.pre_idx]
        self.pre_idx += 1
        root = TreeNode(root_val)
        
        if left == right:
            return root
        
        # Next element in preorder is left child (if exists)
        if self.pre_idx < len(preorder):
            left_val = preorder[self.pre_idx]
            left_pos = postorder_map[left_val]
            
            root.left = build(left, left_pos)
            root.right = build(left_pos + 1, right - 1)
        
        return root
    
    return build(0, len(postorder) - 1)

def bst_from_preorder(preorder):
    """
    LeetCode 1008: Construct BST from Preorder Traversal
    
    Time: O(n), Space: O(h)
    """
    def build(min_val, max_val):
        nonlocal idx
        if idx >= len(preorder):
            return None
        
        val = preorder[idx]
        if val < min_val or val > max_val:
            return None
        
        idx += 1
        root = TreeNode(val)
        root.left = build(min_val, val)
        root.right = build(val, max_val)
        
        return root
    
    idx = 0
    return build(float('-inf'), float('inf'))

# =============================================================================
# CONSTRUCT FROM ARRAYS/LISTS
# =============================================================================

def sorted_array_to_bst(nums):
    """
    LeetCode 108: Convert Sorted Array to Binary Search Tree
    Build height-balanced BST
    
    Time: O(n), Space: O(log n)
    """
    def build(left, right):
        if left > right:
            return None
        
        # Choose middle element as root for balance
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        
        return root
    
    return build(0, len(nums) - 1)

def sorted_list_to_bst(head):
    """
    LeetCode 109: Convert Sorted List to Binary Search Tree
    Build height-balanced BST from linked list
    
    Time: O(n), Space: O(log n)
    """
    # Convert to array first (simpler approach)
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    
    return sorted_array_to_bst(vals)

def sorted_list_to_bst_optimized(head):
    """
    Optimized version without extra space for array
    
    Time: O(n), Space: O(log n)
    """
    def get_size(node):
        size = 0
        while node:
            size += 1
            node = node.next
        return size
    
    def build(size):
        nonlocal head
        if size <= 0:
            return None
        
        left = build(size // 2)
        
        root = TreeNode(head.val)
        head = head.next
        
        root.left = left
        root.right = build(size - size // 2 - 1)
        
        return root
    
    size = get_size(head)
    return build(size)

# =============================================================================
# SERIALIZE AND DESERIALIZE
# =============================================================================

def serialize(root):
    """
    LeetCode 297: Serialize Binary Tree
    Convert tree to string representation
    
    Time: O(n), Space: O(n)
    """
    def preorder(node):
        if not node:
            vals.append("null")
            return
        
        vals.append(str(node.val))
        preorder(node.left)
        preorder(node.right)
    
    vals = []
    preorder(root)
    return ",".join(vals)

def deserialize(data):
    """
    LeetCode 297: Deserialize Binary Tree
    Convert string back to tree
    
    Time: O(n), Space: O(n)
    """
    def build():
        val = next(vals)
        if val == "null":
            return None
        
        root = TreeNode(int(val))
        root.left = build()
        root.right = build()
        return root
    
    vals = iter(data.split(","))
    return build()

def serialize_bst(root):
    """
    LeetCode 449: Serialize BST (more compact)
    Only store preorder for BST
    
    Time: O(n), Space: O(n)
    """
    def preorder(node):
        if node:
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
    
    vals = []
    preorder(root)
    return ",".join(vals)

def deserialize_bst(data):
    """
    LeetCode 449: Deserialize BST
    Reconstruct BST from preorder
    
    Time: O(n), Space: O(h)
    """
    if not data:
        return None
    
    vals = list(map(int, data.split(",")))
    return bst_from_preorder(vals)

# =============================================================================
# SPECIAL CONSTRUCTIONS
# =============================================================================

def build_complete_tree(arr):
    """
    Build complete binary tree from array (level-order)
    
    Time: O(n), Space: O(n)
    """
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        node = queue.popleft()
        
        # Add left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

def build_from_parent_array(parent, n):
    """
    Build tree from parent array where parent[i] is parent of node i
    
    Time: O(n), Space: O(n)
    """
    if n == 0:
        return None
    
    nodes = [TreeNode(i) for i in range(n)]
    root = None
    
    for i in range(n):
        if parent[i] == -1:
            root = nodes[i]
        else:
            parent_node = nodes[parent[i]]
            if not parent_node.left:
                parent_node.left = nodes[i]
            else:
                parent_node.right = nodes[i]
    
    return root

def build_expression_tree(postfix):
    """
    Build expression tree from postfix expression
    
    Time: O(n), Space: O(n)
    """
    stack = []
    
    for char in postfix:
        node = TreeNode(char)
        
        if char.isalnum():  # Operand
            stack.append(node)
        else:  # Operator
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    
    return stack[0] if stack else None

# =============================================================================
# GENERIC CONSTRUCTION TEMPLATE
# =============================================================================

def build_tree_template(data, build_func):
    """
    Generic template for tree construction
    
    Args:
        data: Input data (array, traversals, etc.)
        build_func: Function that defines how to build the tree
    
    Returns:
        Root of constructed tree
    """
    if not data:
        return None
    
    return build_func(data)

def validate_construction_input(preorder, inorder):
    """
    Validate that traversals can form a valid tree
    
    Time: O(n), Space: O(n)
    """
    if len(preorder) != len(inorder):
        return False
    
    if set(preorder) != set(inorder):
        return False
    
    # Check for duplicates
    if len(set(preorder)) != len(preorder):
        return False
    
    return True

def tree_from_brackets(s):
    """
    Build tree from string representation with brackets
    Example: "4(2(3)(1))(6(5))"
    
    Time: O(n), Space: O(h)
    """
    def build():
        nonlocal idx
        if idx >= len(s):
            return None
        
        # Read number
        start = idx
        if s[idx] == '-':
            idx += 1
        while idx < len(s) and s[idx].isdigit():
            idx += 1
        
        node = TreeNode(int(s[start:idx]))
        
        # Check for left child
        if idx < len(s) and s[idx] == '(':
            idx += 1  # Skip '('
            node.left = build()
            idx += 1  # Skip ')'
        
        # Check for right child
        if idx < len(s) and s[idx] == '(':
            idx += 1  # Skip '('
            node.right = build()
            idx += 1  # Skip ')'
        
        return node
    
    idx = 0
    return build() if s else None