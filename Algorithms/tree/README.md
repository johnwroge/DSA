# Tree Algorithms

This repository contains basic templates for fundamental tree algorithms that can be adapted to solve most tree-related problems.

## Algorithm Overview

| File | Description | Time | Space | Common Use Cases |
|------|-------------|------|-------|------------------|
| **traversals.py** | Tree traversal methods | O(n) | O(h) | Visiting nodes, serialization |
| **lca.py** | Lowest Common Ancestor | O(n) | O(h) | Finding common ancestors |
| **tree-construction.py** | Building trees from inputs | O(n) | O(n) | Creating trees from traversals |
| **tree-properties.py** | Tree analysis and validation | O(n) | O(h) | Measuring tree characteristics |

*where n = number of nodes, h = height of tree*

## Quick Pattern Recognition

### 🌳 Tree Traversals
**When to use**: 
- Need to visit all nodes
- Process nodes in specific order
- Serialize/deserialize trees
- Level-by-level processing

**Key patterns**:
```
"inorder", "preorder", "postorder", "level order"
"traverse", "visit all nodes", "process tree"
"serialize", "flatten tree"
```

### 🔍 Lowest Common Ancestor (LCA)
**When to use**:
- Find common ancestor of nodes
- Tree queries about relationships
- Path problems between nodes

**Key patterns**:
```
"lowest common ancestor", "LCA", "common parent"
"path between nodes", "distance between nodes"
"genealogy", "hierarchy problems"
```

### 🏗️ Tree Construction
**When to use**:
- Build tree from traversals
- Convert between data structures
- Deserialize tree representations

**Key patterns**:
```
"construct tree", "build from traversal"
"preorder and inorder", "serialize/deserialize"
"convert array to tree", "rebuild tree"
```

### 📊 Tree Properties
**When to use**:
- Analyze tree characteristics
- Validate tree structure
- Measure tree metrics

**Key patterns**:
```
"height", "depth", "diameter", "balanced"
"validate BST", "tree properties"
"symmetric", "complete tree"
```

## Basic Templates

### Tree Traversal Template
```python
def inorder_recursive(root):
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result
```

### LCA Template
```python
def lca_binary_tree(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lca_binary_tree(root.left, p, q)
    right = lca_binary_tree(root.right, p, q)
    
    if left and right:
        return root
    
    return left or right
```

### Tree Construction Template
```python
def build_tree_pre_in(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    inorder_map = {val: i for i, val in enumerate(inorder)}
    
    def build(left, right):
        if left > right:
            return None
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_pos = inorder_map[root_val]
        
        root.left = build(left, root_pos - 1)
        root.right = build(root_pos + 1, right)
        
        return root
    
    return build(0, len(inorder) - 1)
```

### Tree Properties Template
```python
def tree_height(root):
    if not root:
        return 0
    
    return 1 + max(tree_height(root.left), tree_height(root.right))
```

## Common Tree Patterns

### Recursive Pattern
```python
def tree_recursive_template(root):
    # Base case
    if not root:
        return base_value
    
    # Process children
    left_result = tree_recursive_template(root.left)
    right_result = tree_recursive_template(root.right)
    
    # Combine results
    return combine(root.val, left_result, right_result)
```

### Level-by-Level Pattern
```python
def level_order_template(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
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
```

## Decision Guide

### Choose Traversal When:
- Need to visit all nodes in specific order
- Converting tree to linear structure
- Processing nodes level by level
- Serializing/deserializing trees

### Choose LCA When:
- Finding relationships between nodes
- Path problems between two nodes
- Genealogy or hierarchy questions
- Distance calculations in trees

### Choose Construction When:
- Building tree from given data
- Converting between representations
- Reconstructing from traversals
- Deserializing tree data

### Choose Properties When:
- Analyzing tree structure
- Validating tree constraints
- Computing tree metrics
- Checking tree properties

## Common Mistakes

1. **Null pointer errors**: Always check if node exists before accessing
2. **Incorrect base cases**: Handle empty trees properly
3. **Stack overflow**: Be aware of recursion depth for very deep trees
4. **Wrong traversal order**: Understand when to use pre/in/post order
5. **Index errors**: Be careful with array bounds in construction

## Key Tips

- **Draw examples** to understand tree structure
- **Start with base case** in recursive solutions
- **Use helper functions** to maintain clean interfaces
- **Consider iterative solutions** for very deep trees
- **Test with edge cases**: empty trees, single nodes, skewed trees

## Practice Progression

1. **Master basic traversals** (recursive and iterative)
2. **Learn tree properties** (height, diameter, balance)
3. **Practice tree construction** (from arrays, traversals)
4. **Tackle LCA problems** (various scenarios)
5. **Combine techniques** for complex problems

Choose the template that matches your problem type and adapt the basic structure as needed!