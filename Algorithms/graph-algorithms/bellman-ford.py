"""
Bellman-Ford Algorithm Templates
Applicable LeetCode Problems:
- 787. Cheapest Flights Within K Stops
- 743. Network Delay Time
- 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
- 1615. Maximal Network Rank
- 1928. Minimum Cost to Reach Destination in Time
"""

from collections import defaultdict

def bellman_ford(graph, start, num_nodes):
    """
    Bellman-Ford algorithm for shortest paths with negative edge detection
    graph: adjacency list {node: [(neighbor, weight), ...]}
    Returns: (distances, has_negative_cycle)
    Time: O(VE), Space: O(V)
    """
    distances = [float('inf')] * num_nodes
    distances[start] = 0
    
    # Relax edges V-1 times
    for _ in range(num_nodes - 1):
        updated = False
        for node in graph:
            if distances[node] != float('inf'):
                for neighbor, weight in graph[node]:
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight
                        updated = True
        
        # Early termination if no updates
        if not updated:
            break
    
    # Check for negative cycles
    has_negative_cycle = False
    for node in graph:
        if distances[node] != float('inf'):
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    has_negative_cycle = True
                    break
        if has_negative_cycle:
            break
    
    return distances, has_negative_cycle

def bellman_ford_with_path(graph, start, target, num_nodes):
    """
    Bellman-Ford with path reconstruction
    Returns: (distance, path, has_negative_cycle)
    """
    distances = [float('inf')] * num_nodes
    predecessor = [-1] * num_nodes
    distances[start] = 0
    
    # Relax edges
    for _ in range(num_nodes - 1):
        updated = False
        for node in graph:
            if distances[node] != float('inf'):
                for neighbor, weight in graph[node]:
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight
                        predecessor[neighbor] = node
                        updated = True
        
        if not updated:
            break
    
    # Check for negative cycles
    has_negative_cycle = False
    for node in graph:
        if distances[node] != float('inf'):
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    has_negative_cycle = True
                    break
        if has_negative_cycle:
            break
    
    # Reconstruct path
    path = []
    if distances[target] != float('inf') and not has_negative_cycle:
        current = target
        while current != -1:
            path.append(current)
            current = predecessor[current]
        path.reverse()
    
    return distances[target], path, has_negative_cycle

def shortest_path_with_k_edges(graph, start, target, k, num_nodes):
    """
    Modified Bellman-Ford: shortest path with exactly/at most k edges
    Useful for problems like "Cheapest Flights Within K Stops"
    
    dp[i][v] = minimum cost to reach vertex v using at most i edges
    Time: O(k * E), Space: O(k * V)
    """
    dp = [[float('inf')] * num_nodes for _ in range(k + 2)]
    dp[0][start] = 0
    
    for i in range(1, k + 2):
        dp[i] = dp[i-1][:]  # Copy previous values
        
        for node in graph:
            if dp[i-1][node] != float('inf'):
                for neighbor, weight in graph[node]:
                    dp[i][neighbor] = min(dp[i][neighbor], 
                                        dp[i-1][node] + weight)
    
    return dp[k+1][target] if dp[k+1][target] != float('inf') else -1

def shortest_path_with_time_limit(graph, start, target, max_time, num_nodes):
    """
    Modified Bellman-Ford with time constraints
    Each edge has (neighbor, cost, time)
    
    Returns minimum cost to reach target within max_time
    """
    # dp[t][v] = minimum cost to reach v in exactly t time
    dp = [[float('inf')] * num_nodes for _ in range(max_time + 1)]
    dp[0][start] = 0
    
    for t in range(1, max_time + 1):
        dp[t] = dp[t-1][:]  # Can stay at same node
        
        for node in graph:
            if dp[t-1][node] != float('inf'):
                for neighbor, cost, time in graph[node]:
                    if t >= time:
                        dp[t][neighbor] = min(dp[t][neighbor], 
                                            dp[t-time][node] + cost)
    
    return min(dp[t][target] for t in range(max_time + 1))

def detect_negative_cycle_bellman_ford(edges, num_nodes):
    """
    Detect negative cycle using Bellman-Ford with edge list
    edges: list of (u, v, weight)
    """
    distances = [float('inf')] * num_nodes
    distances[0] = 0  # Start from node 0
    
    # Relax edges V-1 times
    for _ in range(num_nodes - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative cycles
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return True
    
    return False

def bellman_ford_spfa(graph, start, num_nodes):
    """
    SPFA (Shortest Path Faster Algorithm) - optimized Bellman-Ford
    Uses queue to only process nodes that were updated
    Average case: O(E), Worst case: O(VE)
    """
    from collections import deque
    
    distances = [float('inf')] * num_nodes
    distances[start] = 0
    in_queue = [False] * num_nodes
    count = [0] * num_nodes  # Count of times node is processed
    
    queue = deque([start])
    in_queue[start] = True
    
    while queue:
        node = queue.popleft()
        in_queue[node] = False
        
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                distances[neighbor] = distances[node] + weight
                
                if not in_queue[neighbor]:
                    queue.append(neighbor)
                    in_queue[neighbor] = True
                    count[neighbor] += 1
                    
                    # Negative cycle detection
                    if count[neighbor] >= num_nodes:
                        return distances, True
    
    return distances, False

# =============== PROBLEM-SPECIFIC APPLICATIONS ===============

def cheapest_flights_k_stops(n, flights, src, dst, k):
    """
    LeetCode 787: Cheapest Flights Within K Stops
    Using modified Bellman-Ford
    """
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))
    
    return shortest_path_with_k_edges(graph, src, dst, k, n)

def network_delay_time_bellman_ford(times, n, k):
    """
    LeetCode 743: Network Delay Time using Bellman-Ford
    """
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    distances, has_cycle = bellman_ford(graph, k, n + 1)
    
    if has_cycle:
        return -1
    
    max_time = 0
    for i in range(1, n + 1):
        if distances[i] == float('inf'):
            return -1
        max_time = max(max_time, distances[i])
    
    return max_time

def find_city_threshold_distance_bf(n, edges, distance_threshold):
    """
    LeetCode 1334: Find the City With the Smallest Number of Neighbors 
    at a Threshold Distance using Bellman-Ford
    """
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    min_neighbors = float('inf')
    result_city = -1
    
    # Run Bellman-Ford from each city
    for city in range(n):
        distances, _ = bellman_ford(graph, city, n)
        
        neighbors = sum(1 for d in distances if d <= distance_threshold) - 1  # Exclude self
        
        if neighbors <= min_neighbors:
            min_neighbors = neighbors
            result_city = city
    
    return result_city

def minimum_cost_reach_destination_time(max_time, edges, passing_fees):
    """
    LeetCode 1928: Minimum Cost to Reach Destination in Time
    """
    n = len(passing_fees)
    graph = defaultdict(list)
    
    for u, v, time in edges:
        graph[u].append((v, passing_fees[v], time))
        graph[v].append((u, passing_fees[u], time))
    
    # dp[t][city] = minimum cost to reach city at time t
    dp = [[float('inf')] * n for _ in range(max_time + 1)]
    dp[0][0] = passing_fees[0]
    
    for t in range(1, max_time + 1):
        # Can stay at same city
        for city in range(n):
            dp[t][city] = dp[t-1][city]
        
        # Try moving from each city
        for city in range(n):
            if dp[t-1][city] != float('inf'):
                for neighbor, cost, time_needed in graph[city]:
                    if t >= time_needed:
                        dp[t][neighbor] = min(dp[t][neighbor], 
                                            dp[t-time_needed][city] + cost)
    
    result = min(dp[t][n-1] for t in range(max_time + 1))
    return result if result != float('inf') else -1

