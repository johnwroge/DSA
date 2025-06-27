"""
LeetCode Problems where Kruskal's Algorithm can be applied:

1584. Min Cost to Connect All Points
1135. Connecting Cities With Minimum Cost
1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
1168. Optimize Water Distribution in a Village
261. Graph Valid Tree
1061. Lexicographically Smallest Equivalent String
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        self.components -= 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

def kruskal_mst(n, edges):
    """
    Kruskal's Algorithm for Minimum Spanning Tree
    
    Args:
        n: number of vertices (0 to n-1)
        edges: list of [weight, u, v] or [u, v, weight]
    
    Returns:
        (total_cost, mst_edges) or just total_cost
    """
    # Sort edges by weight
    edges.sort(key=lambda x: x[0])  # Assuming format [weight, u, v]
    
    uf = UnionFind(n)
    mst_edges = []
    total_cost = 0
    
    for weight, u, v in edges:
        if uf.union(u, v):
            mst_edges.append([u, v, weight])
            total_cost += weight
            
            # Early termination: MST complete when we have n-1 edges
            if len(mst_edges) == n - 1:
                break
    
    # Check if MST is possible (all vertices connected)
    if len(mst_edges) != n - 1:
        return -1  # or float('inf') depending on problem
    
    return total_cost, mst_edges

def kruskal_mst_simple(n, edges):
    """
    Simplified version that just returns minimum cost
    """
    edges.sort(key=lambda x: x[0])
    uf = UnionFind(n)
    total_cost = 0
    edges_used = 0
    
    for weight, u, v in edges:
        if uf.union(u, v):
            total_cost += weight
            edges_used += 1
            if edges_used == n - 1:
                break
    
    return total_cost if edges_used == n - 1 else -1

# Example usage for LeetCode 1584. Min Cost to Connect All Points
def minCostConnectPoints(points):
    n = len(points)
    edges = []
    
    # Create all possible edges with Manhattan distance
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append([dist, i, j])
    
    return kruskal_mst_simple(n, edges)