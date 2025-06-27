"""
LeetCode Problems where Prim's Algorithm can be applied:

1584. Min Cost to Connect All Points
1135. Connecting Cities With Minimum Cost
1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
1168. Optimize Water Distribution in a Village
261. Graph Valid Tree
"""

import heapq
from collections import defaultdict

def prim_mst(n, edges):
    """
    Prim's Algorithm for Minimum Spanning Tree
    
    Args:
        n: number of vertices (0 to n-1)
        edges: list of [u, v, weight] or [weight, u, v]
    
    Returns:
        (total_cost, mst_edges) or just total_cost
    """
    # Build adjacency list
    graph = defaultdict(list)
    for edge in edges:
        if len(edge) == 3:
            # Handle both [u, v, weight] and [weight, u, v] formats
            if isinstance(edge[0], int) and edge[0] < n:  # Likely [u, v, weight]
                u, v, weight = edge
            else:  # Likely [weight, u, v]
                weight, u, v = edge
            graph[u].append((weight, v))
            graph[v].append((weight, u))
    
    # Prim's algorithm
    visited = set()
    min_heap = [(0, 0)]  # (weight, vertex) - start from vertex 0
    total_cost = 0
    mst_edges = []
    
    while min_heap and len(visited) < n:
        weight, u = heapq.heappop(min_heap)
        
        if u in visited:
            continue
            
        visited.add(u)
        total_cost += weight
        
        if weight > 0:  # Don't add the starting vertex to MST edges
            mst_edges.append((u, weight))
        
        # Add all adjacent edges to heap
        for next_weight, v in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (next_weight, v))
    
    # Check if MST is possible
    if len(visited) != n:
        return -1  # Graph is not connected
    
    return total_cost, mst_edges

def prim_mst_simple(n, edges):
    """
    Simplified version that just returns minimum cost
    """
    graph = defaultdict(list)
    for edge in edges:
        if len(edge) == 3:
            if isinstance(edge[0], int) and edge[0] < n:
                u, v, weight = edge
            else:
                weight, u, v = edge
            graph[u].append((weight, v))
            graph[v].append((weight, u))
    
    visited = set()
    min_heap = [(0, 0)]
    total_cost = 0
    
    while min_heap and len(visited) < n:
        weight, u = heapq.heappop(min_heap)
        
        if u in visited:
            continue
            
        visited.add(u)
        total_cost += weight
        
        for next_weight, v in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (next_weight, v))
    
    return total_cost if len(visited) == n else -1

def prim_mst_with_coordinates(points):
    """
    Prim's algorithm for points in 2D space (for problems like LeetCode 1584)
    """
    n = len(points)
    if n <= 1:
        return 0
    
    visited = set()
    min_heap = [(0, 0)]  # (distance, point_index)
    total_cost = 0
    
    while min_heap and len(visited) < n:
        dist, u = heapq.heappop(min_heap)
        
        if u in visited:
            continue
            
        visited.add(u)
        total_cost += dist
        
        # Add all unvisited points to heap with Manhattan distance
        for v in range(n):
            if v not in visited:
                manhattan_dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(min_heap, (manhattan_dist, v))
    
    return total_cost

# Example usage for LeetCode 1584. Min Cost to Connect All Points
def minCostConnectPoints(points):
    return prim_mst_with_coordinates(points)

# Alternative implementation using adjacency matrix for dense graphs
def prim_mst_matrix(n, adj_matrix):
    """
    Prim's algorithm using adjacency matrix (good for dense graphs)
    """
    visited = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    total_cost = 0
    
    for _ in range(n):
        # Find minimum edge
        u = -1
        for v in range(n):
            if not visited[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        
        visited[u] = True
        total_cost += min_edge[u]
        
        # Update minimum edges
        for v in range(n):
            if not visited[v] and adj_matrix[u][v] < min_edge[v]:
                min_edge[v] = adj_matrix[u][v]
    
    return total_cost