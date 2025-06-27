# Minimum Spanning Tree Algorithms

This repository contains implementations of two classic algorithms for finding Minimum Spanning Trees (MSTs): **Kruskal's Algorithm** and **Prim's Algorithm**.

## What is a Minimum Spanning Tree?

A Minimum Spanning Tree is a subset of edges in a weighted, connected graph that:
- Connects all vertices together
- Has no cycles (forms a tree)
- Has the minimum possible total edge weight

For a graph with `n` vertices, an MST will always have exactly `n-1` edges.

## Algorithm Comparison

| Aspect | Kruskal's Algorithm | Prim's Algorithm |
|--------|-------------------|------------------|
| **Approach** | Edge-based (global view) | Vertex-based (local growth) |
| **Data Structure** | Union-Find + Sorted Edges | Priority Queue + Adjacency List |
| **Time Complexity** | O(E log E) | O(E log V) with binary heap |
| **Space Complexity** | O(V) for Union-Find | O(V + E) for adjacency list |
| **Best For** | Sparse graphs (few edges) | Dense graphs (many edges) |
| **Edge Processing** | All at once (sorted) | One at a time (as needed) |

## When to Use Kruskal's Algorithm

### ✅ Choose Kruskal's When:

1. **Sparse Graphs**: When the number of edges is much smaller than V²
2. **Pre-sorted Edges**: When edges are already sorted or sorting is cheap
3. **Disjoint Set Operations**: When you need Union-Find for other purposes
4. **Memory Constraints**: When you want to minimize space usage
5. **Parallel Processing**: Kruskal's can be more easily parallelized

### 📝 Common LeetCode Patterns:
- **Connection Problems**: "Connect all points with minimum cost"
- **Component Merging**: Problems involving merging disjoint sets
- **Critical Edge Detection**: Finding edges that are essential for connectivity

### 🎯 LeetCode Problems:
- **1584. Min Cost to Connect All Points** - Classic MST with coordinate points
- **1135. Connecting Cities With Minimum Cost** - Direct MST application
- **261. Graph Valid Tree** - Check if edges form a valid tree
- **1489. Find Critical and Pseudo-Critical Edges** - Advanced MST analysis

## When to Use Prim's Algorithm

### ✅ Choose Prim's When:

1. **Dense Graphs**: When the number of edges approaches V²
2. **Starting Point Matters**: When you have a specific starting vertex
3. **Incremental Growth**: When you need to build the MST step by step
4. **Memory Efficiency for Dense Graphs**: Better space usage for dense graphs
5. **Real-time Applications**: When you need to process the MST as it grows

### 📝 Common LeetCode Patterns:
- **Grid-based Problems**: 2D grids where each cell connects to neighbors
- **Coordinate Problems**: Points in space with distance calculations
- **Network Expansion**: Growing a network from a central point

### 🎯 LeetCode Problems:
- **1584. Min Cost to Connect All Points** - Can use either, but Prim's is often more intuitive
- **1168. Optimize Water Distribution in a Village** - Network optimization
- **1135. Connecting Cities With Minimum Cost** - City connection problems

## Implementation Details

### Kruskal's Algorithm Steps:
1. Sort all edges by weight
2. Initialize Union-Find structure
3. For each edge (in sorted order):
   - If edge connects different components, add to MST
   - Union the components
4. Stop when MST has V-1 edges

### Prim's Algorithm Steps:
1. Start with any vertex
2. Add all edges from current tree to priority queue
3. While queue is not empty:
   - Extract minimum weight edge
   - If it leads to unvisited vertex, add to MST
   - Add new vertex's edges to queue

## Performance Guidelines

### For Sparse Graphs (E << V²):
```
Kruskal's: O(E log E) ≈ O(E log V)
Prim's:    O(E log V)
Winner: Either (similar performance)
```

### For Dense Graphs (E ≈ V²):
```
Kruskal's: O(V² log V)
Prim's:    O(V² log V) with binary heap
           O(V²) with Fibonacci heap
Winner: Prim's (especially with advanced heaps)
```

## Space Complexity Considerations

- **Kruskal's**: O(V) for Union-Find + O(E) for edge storage
- **Prim's**: O(V + E) for adjacency list + O(V) for priority queue

## Code Organization

```
minimum-spanning-tree/
├── kruskal.py          # Kruskal's algorithm implementation
├── prim.py             # Prim's algorithm implementation
└── README.md           # This file
```

## Usage Examples

### For LeetCode 1584 (Min Cost to Connect All Points):

**Kruskal's Approach:**
```python
def minCostConnectPoints(points):
    n = len(points)
    edges = []
    # Generate all edges
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append([dist, i, j])
    return kruskal_mst_simple(n, edges)
```

**Prim's Approach:**
```python
def minCostConnectPoints(points):
    return prim_mst_with_coordinates(points)
```

## Tips for LeetCode Problems

1. **Read Carefully**: Some problems give you edges directly, others require you to generate them
2. **Edge Format**: Pay attention to whether edges are `[u, v, weight]` or `[weight, u, v]`
3. **Connectivity Check**: Always verify if the graph can form a spanning tree
4. **Coordinate Problems**: For points in space, you usually need to calculate distances
5. **Return Value**: Some problems want total cost, others want the actual edges

## Common Pitfalls

1. **Not sorting edges** in Kruskal's algorithm
2. **Forgetting path compression** in Union-Find
3. **Wrong edge format** handling
4. **Not checking graph connectivity**
5. **Off-by-one errors** in vertex indexing
6. **Using wrong distance formula** for coordinate problems

## Advanced Applications

- **Network Design**: Designing minimum cost networks (telecommunications, transportation)
- **Clustering**: MST can be used for hierarchical clustering
- **Image Processing**: MST-based segmentation algorithms
- **Approximation Algorithms**: MST is used in TSP approximations
- **Load Balancing**: Distributing load across network nodes

Choose the algorithm that best fits your specific problem constraints and graph characteristics!