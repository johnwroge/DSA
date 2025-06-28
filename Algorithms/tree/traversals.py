"""
LeetCode Problems where Tree Traversals can be applied:

94. Binary Tree Inorder Traversal
144. Binary Tree Preorder Traversal
145. Binary Tree Postorder Traversal
102. Binary Tree Level Order Traversal
103. Binary Tree Zigzag Level Order Traversal
107. Binary Tree Level Order Traversal II
199. Binary Tree Right Side View
314. Binary Tree Vertical Order Traversal
"""

from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# =============================================================================
# RECURSIVE TRAVERSALS
# =============================================================================

def inorder_recursive(root):
    """
    LeetCode 94: Binary Tree Inorder Traversal
    Left -> Root -> Right
    
    Time: O(n), Space: O(h) where h = height
    """
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result

def preorder_recursive(root):
    """
    LeetCode 144: Binary Tree Preorder Traversal
    Root -> Left -> Right
    
    Time: O(n), Space: O(h)
    """
    result = []
    
    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    
    preorder(root)
    return result

def postorder_recursive(root):
    """
    LeetCode 145: Binary Tree Postorder Traversal
    Left -> Right -> Root
    
    Time: O(n), Space: O(h)
    """
    result = []
    
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
    
    postorder(root)
    return result

# =============================================================================
# ITERATIVE TRAVERSALS
# =============================================================================

def inorder_iterative(root):
    """
    Iterative inorder traversal using stack
    
    Time: O(n), Space: O(h)
    """
    result = []
    stack = []
    current = root
    
    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process current node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result

def preorder_iterative(root):
    """
    Iterative preorder traversal using stack
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right first, then left (stack is LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

def postorder_iterative(root):
    """
    Iterative postorder traversal using two stacks
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return []
    
    result = []
    stack1 = [root]
    stack2 = []
    
    # First stack for traversal, second for result order
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    # Pop from second stack to get postorder
    while stack2:
        result.append(stack2.pop().val)
    
    return result

# =============================================================================
# LEVEL ORDER TRAVERSALS
# =============================================================================

def level_order(root):
    """
    LeetCode 102: Binary Tree Level Order Traversal
    
    Time: O(n), Space: O(w) where w = maximum width
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_nodes)
    
    return result

def level_order_bottom(root):
    """
    LeetCode 107: Binary Tree Level Order Traversal II
    Bottom-up level order
    
    Time: O(n), Space: O(w)
    """
    result = level_order(root)
    return result[::-1]

def zigzag_level_order(root):
    """
    LeetCode 103: Binary Tree Zigzag Level Order Traversal
    Alternate left-to-right and right-to-left
    
    Time: O(n), Space: O(w)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse every other level
        if not left_to_right:
            level_nodes.reverse()
        
        result.append(level_nodes)
        left_to_right = not left_to_right
    
    return result

def right_side_view(root):
    """
    LeetCode 199: Binary Tree Right Side View
    Get rightmost node at each level
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # Last node in level is rightmost
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

def vertical_order(root):
    """
    LeetCode 314: Binary Tree Vertical Order Traversal
    Group nodes by vertical position
    
    Time: O(n), Space: O(n)
    """
    if not root:
        return []
    
    from collections import defaultdict
    column_table = defaultdict(list)
    queue = deque([(root, 0)])  # (node, column)
    
    while queue:
        node, column = queue.popleft()
        column_table[column].append(node.val)
        
        if node.left:
            queue.append((node.left, column - 1))
        if node.right:
            queue.append((node.right, column + 1))
    
    # Sort by column index and return values
    return [column_table[col] for col in sorted(column_table.keys())]

# =============================================================================
# MORRIS TRAVERSAL (CONSTANT SPACE)
# =============================================================================

def morris_inorder(root):
    """
    Morris inorder traversal with O(1) space
    
    Time: O(n), Space: O(1)
    """
    result = []
    current = root
    
    while current:
        if not current.left:
            # No left subtree, visit current and go right
            result.append(current.val)
            current = current.right
        else:
            # Find inorder predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                # Create threaded link
                predecessor.right = current
                current = current.left
            else:
                # Remove threaded link and visit current
                predecessor.right = None
                result.append(current.val)
                current = current.right
    
    return result

# =============================================================================
# GENERIC TRAVERSAL TEMPLATES
# =============================================================================

def dfs_recursive_template(root, visit_func):
    """
    Generic DFS template with custom visit function
    
    Args:
        root: Tree root
        visit_func: Function to call on each node
    """
    def dfs(node):
        if not node:
            return
        
        # Pre-order processing
        visit_func(node, 'pre')
        
        dfs(node.left)
        
        # In-order processing
        visit_func(node, 'in')
        
        dfs(node.right)
        
        # Post-order processing
        visit_func(node, 'post')
    
    dfs(root)

def bfs_template(root, level_func=None):
    """
    Generic BFS template with optional level processing
    
    Args:
        root: Tree root
        level_func: Function to call on each level
    """
    if not root:
        return
    
    queue = deque([root])
    level = 0
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Process current level
        if level_func:
            level_func(level_nodes, level)
        
        level += 1

def collect_paths(root):
    """
    Collect all root-to-leaf paths
    
    Time: O(n), Space: O(h)
    """
    paths = []
    
    def dfs(node, path):
        if not node:
            return
        
        path.append(node.val)
        
        # If leaf node, add path to result
        if not node.left and not node.right:
            paths.append(path[:])
        
        dfs(node.left, path)
        dfs(node.right, path)
        
        path.pop()  # Backtrack
    
    dfs(root, [])
    return paths