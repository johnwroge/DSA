"""
Floyd-Warshall Algorithm Templates
Applicable LeetCode Problems:
- 399. Evaluate Division
- 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
- 1462. Course Schedule IV
- 1547. Minimum Cost to Cut a Stick (variant)
- 1617. Count Subtrees With Max Distance Between Cities
- 1976. Number of Ways to Arrive at Destination (variant)
"""

from collections import defaultdict

def floyd_warshall(graph, num_nodes):
    """
    Floyd-Warshall algorithm for all-pairs shortest paths
    Time: O(V³), Space: O(V²)
    Returns: distance matrix
    """
    # Initialize distance matrix
    dist = [[float('inf')] * num_nodes for _ in range(num_nodes)]
    
    # Distance from node to itself is 0
    for i in range(num_nodes):
        dist[i][i] = 0
    
    # Fill in direct edges
    for node in graph:
        for neighbor, weight in graph[node]:
            dist[node][neighbor] = weight
    
    # Floyd-Warshall main loop
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def floyd_warshall_with_path(graph, num_nodes):
    """
    Floyd-Warshall with path reconstruction
    Returns: (distance_matrix, get_path_function)
    """
    dist = [[float('inf')] * num_nodes for _ in range(num_nodes)]
    next_node = [[-1] * num_nodes for _ in range(num_nodes)]
    
    # Initialize
    for i in range(num_nodes):
        dist[i][i] = 0
    
    for node in graph:
        for neighbor, weight in graph[node]:
            dist[node][neighbor] = weight
            next_node[node][neighbor] = neighbor
    
    # Main algorithm
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]
    
    def get_path(start, end):
        """Reconstruct path from start to end"""
        if next_node[start][end] == -1:
            return []
        
        path = [start]
        current = start
        while current != end:
            current = next_node[current][end]
            path.append(current)
        return path
    
    return dist, get_path

def floyd_warshall_from_edges(edges, num_nodes):
    """
    Floyd-Warshall from edge list format
    edges: list of (u, v, weight)
    """
    dist = [[float('inf')] * num_nodes for _ in range(num_nodes)]
    
    # Initialize diagonal
    for i in range(num_nodes):
        dist[i][i] = 0
    
    # Add edges
    for u, v, weight in edges:
        dist[u][v] = weight
        # For undirected graph, uncomment the next line
        # dist[v][u] = weight
    
    # Floyd-Warshall
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def detect_negative_cycle_floyd_warshall(graph, num_nodes):
    """
    Use Floyd-Warshall to detect negative cycles
    """
    dist = floyd_warshall(graph, num_nodes)
    
    # Check diagonal for negative values
    for i in range(num_nodes):
        if dist[i][i] < 0:
            return True
    
    return False

def floyd_warshall_transitive_closure(graph, num_nodes):
    """
    Floyd-Warshall for transitive closure (reachability)
    Returns boolean matrix indicating reachability
    """
    reach = [[False] * num_nodes for _ in range(num_nodes)]
    
    # Initialize: direct edges and self-loops
    for i in range(num_nodes):
        reach[i][i] = True
    
    for node in graph:
        for neighbor in graph[node]:
            reach[node][neighbor] = True
    
    # Floyd-Warshall for reachability
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    
    return reach

def floyd_warshall_max_min_path(graph, num_nodes, mode='max'):
    """
    Modified Floyd-Warshall for maximum/minimum bottleneck paths
    mode: 'max' for maximum bottleneck, 'min' for minimum bottleneck
    """
    if mode == 'max':
        initial_value = 0
        compare_func = max
    else:  # min
        initial_value = float('inf')
        compare_func = min
    
    dist = [[initial_value] * num_nodes for _ in range(num_nodes)]
    
    # Initialize
    for node in graph:
        for neighbor, weight in graph[node]:
            dist[node][neighbor] = weight
    
    # Set diagonal based on mode
    for i in range(num_nodes):
        dist[i][i] = float('inf') if mode == 'max' else 0
    
    # Floyd-Warshall with modified update rule
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if mode == 'max':
                    new_dist = min(dist[i][k], dist[k][j])
                    dist[i][j] = max(dist[i][j], new_dist)
                else:  # min
                    new_dist = max(dist[i][k], dist[k][j])
                    dist[i][j] = min(dist[i][j], new_dist)
    
    return dist

# =============== PROBLEM-SPECIFIC APPLICATIONS ===============

def evaluate_division_floyd_warshall(equations, values, queries):
    """
    LeetCode 399: Evaluate Division using Floyd-Warshall
    """
    # Build graph
    graph = defaultdict(dict)
    variables = set()
    
    for i, (a, b) in enumerate(equations):
        graph[a][b] = values[i]
        graph[b][a] = 1.0 / values[i]
        variables.add(a)
        variables.add(b)
    
    # Convert to matrix format
    var_list = list(variables)
    var_to_idx = {var: i for i, var in enumerate(var_list)}
    n = len(var_list)
    
    # Initialize distance matrix with multiplication semantics
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 1.0
    
    for var in variables:
        i = var_to_idx[var]
        for neighbor, weight in graph[var].items():
            j = var_to_idx[neighbor]
            dist[i][j] = weight
    
    # Floyd-Warshall with multiplication
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != 0 and dist[k][j] != 0:
                    if dist[i][j] == 0:  # No path exists yet
                        dist[i][j] = dist[i][k] * dist[k][j]
                    else:
                        # Keep existing path (all should be equal if consistent)
                        pass
    
    # Process queries
    result = []
    for a, b in queries:
        if a not in var_to_idx or b not in var_to_idx:
            result.append(-1.0)
        else:
            i, j = var_to_idx[a], var_to_idx[b]
            result.append(dist[i][j] if dist[i][j] != 0 else -1.0)
    
    return result

def find_city_threshold_distance_fw(n, edges, distance_threshold):
    """
    LeetCode 1334: Find the City With the Smallest Number of Neighbors 
    at a Threshold Distance using Floyd-Warshall
    """
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Count reachable cities for each city
    min_neighbors = float('inf')
    result_city = -1
    
    for i in range(n):
        neighbors = sum(1 for j in range(n) 
                       if i != j and dist[i][j] <= distance_threshold)
        
        if neighbors <= min_neighbors:
            min_neighbors = neighbors
            result_city = i
    
    return result_city

def course_schedule_iv_fw(num_courses, prerequisites, queries):
    """
    LeetCode 1462: Course Schedule IV using Floyd-Warshall for reachability
    """
    # Build reachability matrix
    reach = floyd_warshall_transitive_closure(
        defaultdict(list, {pre: [course] for course, pre in prerequisites}),
        num_courses
    )
    
    # Answer queries
    result = []
    for pre, course in queries:
        result.append(reach[pre][course])
    
    return result

def count_subtrees_max_distance(n, edges):
    """
    LeetCode 1617: Count Subtrees With Max Distance Between Cities
    Uses Floyd-Warshall to compute all distances
    """
    # Build distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for u, v in edges:
        dist[u-1][v-1] = 1  # Convert to 0-indexed
        dist[v-1][u-1] = 1
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    def is_connected_subtree(mask):
        """Check if subset represents a connected subtree"""
        cities = [i for i in range(n) if mask & (1 << i)]
        if len(cities) <= 1:
            return True
        
        # Check if all cities are connected within the subset
        for i in cities:
            for j in cities:
                if dist[i][j] == float('inf'):
                    return False
        
        # Check if it forms a tree (connected with n-1 edges)
        edge_count = 0
        for u, v in edges:
            if (mask & (1 << (u-1))) and (mask & (1 << (v-1))):
                edge_count += 1
        
        return edge_count == len(cities) - 1
    
    result = [0] * (n - 1)  # result[i] = count of subtrees with max distance i+1
    
    # Check all possible subsets
    for mask in range(1, 1 << n):
        if is_connected_subtree(mask):
            cities = [i for i in range(n) if mask & (1 << i)]
            if len(cities) >= 2:
                max_dist = 0
                for i in cities:
                    for j in cities:
                        max_dist = max(max_dist, dist[i][j])
                result[max_dist - 1] += 1
    
    return result

