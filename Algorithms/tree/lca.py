"""
LeetCode Problems where LCA algorithms can be applied:

236. Lowest Common Ancestor of a Binary Tree
235. Lowest Common Ancestor of a Binary Search Tree
1644. Lowest Common Ancestor of a Binary Tree II
1650. Lowest Common Ancestor of a Binary Tree III
1676. Lowest Common Ancestor of a Binary Tree IV
1123. Lowest Common Ancestor of Deepest Leaves
865. Smallest Subtree with all the Deepest Nodes
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for node with parent pointer
class TreeNodeWithParent:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def lca_binary_tree(root, p, q):
    """
    LeetCode 236: Lowest Common Ancestor of a Binary Tree
    Find LCA in any binary tree
    
    Time: O(n), Space: O(h)
    """
    if not root or root == p or root == q:
        return root
    
    # Search in left and right subtrees
    left = lca_binary_tree(root.left, p, q)
    right = lca_binary_tree(root.right, p, q)
    
    # If both subtrees contain one of p, q, then root is LCA
    if left and right:
        return root
    
    # Return the non-null result
    return left or right

def lca_bst(root, p, q):
    """
    LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
    Optimized LCA for BST using BST property
    
    Time: O(h), Space: O(1) iterative
    """
    current = root
    
    while current:
        # Both nodes are in left subtree
        if p.val < current.val and q.val < current.val:
            current = current.left
        # Both nodes are in right subtree
        elif p.val > current.val and q.val > current.val:
            current = current.right
        # Nodes are on different sides or one is current
        else:
            return current
    
    return None

def lca_bst_recursive(root, p, q):
    """
    Recursive version of BST LCA
    
    Time: O(h), Space: O(h)
    """
    if not root:
        return None
    
    # Both nodes are in left subtree
    if p.val < root.val and q.val < root.val:
        return lca_bst_recursive(root.left, p, q)
    # Both nodes are in right subtree
    elif p.val > root.val and q.val > root.val:
        return lca_bst_recursive(root.right, p, q)
    # Split point found
    else:
        return root

def lca_with_parent_pointers(p, q):
    """
    LeetCode 1650: LCA with parent pointers
    Find LCA when nodes have parent pointers
    
    Time: O(h), Space: O(1)
    """
    # Calculate depths
    def get_depth(node):
        depth = 0
        while node.parent:
            depth += 1
            node = node.parent
        return depth
    
    depth_p = get_depth(p)
    depth_q = get_depth(q)
    
    # Make sure p is deeper than q
    if depth_p < depth_q:
        p, q = q, p
        depth_p, depth_q = depth_q, depth_p
    
    # Move p up to same level as q
    for _ in range(depth_p - depth_q):
        p = p.parent
    
    # Move both up until they meet
    while p != q:
        p = p.parent
        q = q.parent
    
    return p

def lca_with_path(root, p, q):
    """
    LCA using path from root to nodes
    
    Time: O(n), Space: O(h)
    """
    def find_path(node, target, path):
        if not node:
            return False
        
        path.append(node)
        
        if node == target:
            return True
        
        if (find_path(node.left, target, path) or 
            find_path(node.right, target, path)):
            return True
        
        path.pop()
        return False
    
    path_p, path_q = [], []
    
    if not find_path(root, p, path_p) or not find_path(root, q, path_q):
        return None
    
    # Find last common node in paths
    lca = None
    for i in range(min(len(path_p), len(path_q))):
        if path_p[i] == path_q[i]:
            lca = path_p[i]
        else:
            break
    
    return lca

def lca_multiple_nodes(root, nodes):
    """
    LeetCode 1676: LCA of multiple nodes
    Find LCA of multiple nodes
    
    Time: O(n), Space: O(h)
    """
    node_set = set(nodes)
    
    def dfs(node):
        if not node:
            return None
        
        if node in node_set:
            return node
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        # If both subtrees have target nodes
        if left and right:
            return node
        
        return left or right
    
    return dfs(root)

def lca_deepest_leaves(root):
    """
    LeetCode 1123: LCA of Deepest Leaves
    Find LCA of all deepest leaves
    
    Time: O(n), Space: O(h)
    """
    def dfs(node):
        if not node:
            return None, 0
        
        left_lca, left_depth = dfs(node.left)
        right_lca, right_depth = dfs(node.right)
        
        if left_depth > right_depth:
            return left_lca, left_depth + 1
        elif right_depth > left_depth:
            return right_lca, right_depth + 1
        else:
            # Equal depths - current node is LCA
            return node, left_depth + 1
    
    lca, _ = dfs(root)
    return lca

def lca_exists_check(root, p, q):
    """
    LeetCode 1644: LCA with existence check
    Find LCA only if both nodes exist
    
    Time: O(n), Space: O(h)
    """
    def find_lca(node):
        if not node:
            return None, False, False
        
        if node == p and node == q:
            return node, True, True
        
        left_lca, left_has_p, left_has_q = find_lca(node.left)
        if left_lca and left_has_p and left_has_q:
            return left_lca, True, True
        
        right_lca, right_has_p, right_has_q = find_lca(node.right)
        if right_lca and right_has_p and right_has_q:
            return right_lca, True, True
        
        # Check current node
        has_p = left_has_p or right_has_p or (node == p)
        has_q = left_has_q or right_has_q or (node == q)
        
        if has_p and has_q:
            return node, True, True
        
        return None, has_p, has_q
    
    lca, has_p, has_q = find_lca(root)
    return lca if (has_p and has_q) else None

# =============================================================================
# ADVANCED LCA ALGORITHMS
# =============================================================================

class LCAPreprocessor:
    """
    Preprocessing for O(1) LCA queries using binary lifting
    
    Preprocessing: O(n log n), Query: O(1), Space: O(n log n)
    """
    
    def __init__(self, root):
        self.LOG = 20  # log2(max_nodes)
        self.parent = {}
        self.depth = {}
        
        # Build parent table using binary lifting
        self._preprocess(root)
    
    def _preprocess(self, root):
        # DFS to set up parent and depth
        def dfs(node, par, d):
            if not node:
                return
            
            self.parent[node] = [[None] * self.LOG for _ in range(1)]
            self.depth[node] = d
            self.parent[node][0][0] = par
            
            dfs(node.left, node, d + 1)
            dfs(node.right, node, d + 1)
        
        dfs(root, None, 0)
        
        # Fill binary lifting table
        for j in range(1, self.LOG):
            for node in self.parent:
                if len(self.parent[node]) <= j:
                    self.parent[node].append([None] * self.LOG)
                
                if self.parent[node][j-1][0]:
                    self.parent[node][j][0] = self.parent[self.parent[node][j-1][0]][j-1][0]
    
    def lca(self, u, v):
        """Get LCA in O(1) time after preprocessing"""
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        # Bring u to same level as v
        diff = self.depth[u] - self.depth[v]
        for i in range(self.LOG):
            if (diff >> i) & 1:
                u = self.parent[u][i][0]
        
        if u == v:
            return u
        
        # Binary search for LCA
        for i in range(self.LOG - 1, -1, -1):
            if (self.parent[u][i][0] != self.parent[v][i][0]):
                u = self.parent[u][i][0]
                v = self.parent[v][i][0]
        
        return self.parent[u][0][0]

# =============================================================================
# GENERIC LCA TEMPLATE
# =============================================================================

def lca_template(root, nodes, condition_func=None):
    """
    Generic LCA template for various conditions
    
    Args:
        root: Tree root
        nodes: List of target nodes
        condition_func: Optional condition function
    
    Returns:
        LCA based on specified conditions
    """
    target_set = set(nodes)
    
    def dfs(node):
        if not node:
            return None, 0
        
        # Check if current node satisfies condition
        is_target = node in target_set
        if condition_func:
            is_target = is_target and condition_func(node)
        
        left_lca, left_count = dfs(node.left)
        right_lca, right_count = dfs(node.right)
        
        current_count = left_count + right_count + (1 if is_target else 0)
        
        # If we found LCA in subtree, return it
        if left_lca:
            return left_lca, current_count
        if right_lca:
            return right_lca, current_count
        
        # Check if current node is LCA
        if current_count == len(nodes):
            return node, current_count
        
        return None, current_count
    
    lca, _ = dfs(root)
    return lca