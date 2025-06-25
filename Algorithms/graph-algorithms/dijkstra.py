"""
Dijkstra's Shortest Path Algorithm Template
Applicable LeetCode Problems:
- 743. Network Delay Time
- 787. Cheapest Flights Within K Stops
- 1514. Path with Maximum Probability
- 1631. Path With Minimum Effort
- 1976. Number of Ways to Arrive at Destination
- 2045. Second Minimum Time to Reach Destination
- 505. The Maze II
- 499. The Maze III
- 882. Reachable Nodes In Subdivided Graph
"""

import heapq
from collections import defaultdict, deque

def dijkstra_basic(graph, start):
    """
    Basic Dijkstra's algorithm for finding shortest distances from start to all nodes
    graph: adjacency list {node: [(neighbor, weight), ...]}
    Time: O((V + E) log V), Space: O(V)
    """
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)
    visited = set()
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dict(distances)

def dijkstra_with_path(graph, start, target):
    """
    Dijkstra's algorithm that also returns the shortest path
    Returns (distance, path)
    """
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    previous = {}
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if node in visited:
            continue
        
        if node == target:
            # Reconstruct path
            path = []
            current = target
            while current is not None:
                path.append(current)
                current = previous.get(current)
            return current_dist, list(reversed(path))
        
        visited.add(node)
        
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = node
                heapq.heappush(pq, (distance, neighbor))
    
    return float('inf'), []

def dijkstra_grid(grid, start, end):
    """
    Dijkstra's for 2D grid where each cell has a weight
    grid[i][j] represents the cost to enter cell (i,j)
    """
    if not grid or not grid[0]:
        return float('inf')
    
    rows, cols = len(grid), len(grid[0])
    start_r, start_c = start
    end_r, end_c = end
    
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start_r][start_c] = grid[start_r][start_c]
    
    pq = [(grid[start_r][start_c], start_r, start_c)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while pq:
        current_dist, row, col = heapq.heappop(pq)
        
        if row == end_r and col == end_c:
            return current_dist
        
        if current_dist > distances[row][col]:
            continue
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols):
                
                distance = current_dist + grid[new_row][new_col]
                
                if distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = distance
                    heapq.heappush(pq, (distance, new_row, new_col))
    
    return distances[end_r][end_c]

def dijkstra_k_stops(graph, start, target, k):
    """
    Modified Dijkstra for problems with constraints (e.g., at most K stops)
    State: (cost, node, stops_used)
    """
    # (cost, node, stops)
    pq = [(0, start, 0)]
    # best[node][stops] = minimum cost to reach node with exactly 'stops' stops
    best = defaultdict(lambda: defaultdict(lambda: float('inf')))
    best[start][0] = 0
    
    while pq:
        cost, node, stops = heapq.heappop(pq)
        
        if node == target:
            return cost
        
        if stops > k or cost > best[node][stops]:
            continue
        
        for neighbor, price in graph[node]:
            new_cost = cost + price
            new_stops = stops + 1
            
            if new_stops <= k + 1 and new_cost < best[neighbor][new_stops]:
                best[neighbor][new_stops] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, new_stops))
    
    return -1

def dijkstra_multiple_sources(graph, sources):
    """
    Multi-source Dijkstra (useful for problems where you start from multiple points)
    """
    distances = defaultdict(lambda: float('inf'))
    pq = []
    
    # Initialize all sources
    for source in sources:
        distances[source] = 0
        heapq.heappush(pq, (0, source))
    
    visited = set()
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dict(distances)

def dijkstra_bidirectional(graph, start, target):
    """
    Bidirectional Dijkstra for faster pathfinding
    Searches from both start and target simultaneously
    """
    if start == target:
        return 0
    
    # Forward search from start
    dist_forward = defaultdict(lambda: float('inf'))
    dist_forward[start] = 0
    pq_forward = [(0, start)]
    visited_forward = set()
    
    # Backward search from target (need reverse graph)
    reverse_graph = defaultdict(list)
    for node in graph:
        for neighbor, weight in graph[node]:
            reverse_graph[neighbor].append((node, weight))
    
    dist_backward = defaultdict(lambda: float('inf'))
    dist_backward[target] = 0
    pq_backward = [(0, target)]
    visited_backward = set()
    
    best_distance = float('inf')
    
    while pq_forward or pq_backward:
        # Forward step
        if pq_forward:
            dist, node = heapq.heappop(pq_forward)
            if node not in visited_forward:
                visited_forward.add(node)
                
                # Check if we've met the backward search
                if node in visited_backward:
                    best_distance = min(best_distance, dist + dist_backward[node])
                
                for neighbor, weight in graph[node]:
                    new_dist = dist + weight
                    if new_dist < dist_forward[neighbor]:
                        dist_forward[neighbor] = new_dist
                        heapq.heappush(pq_forward, (new_dist, neighbor))
        
        # Backward step
        if pq_backward:
            dist, node = heapq.heappop(pq_backward)
            if node not in visited_backward:
                visited_backward.add(node)
                
                # Check if we've met the forward search
                if node in visited_forward:
                    best_distance = min(best_distance, dist + dist_forward[node])
                
                for neighbor, weight in reverse_graph[node]:
                    new_dist = dist + weight
                    if new_dist < dist_backward[neighbor]:
                        dist_backward[neighbor] = new_dist
                        heapq.heappush(pq_backward, (new_dist, neighbor))
        
        # Early termination if we've found a path
        if best_distance < float('inf'):
            # Check if we can do better
            min_forward = min([dist for dist, _ in pq_forward] + [float('inf')])
            min_backward = min([dist for dist, _ in pq_backward] + [float('inf')])
            
            if min_forward + min_backward >= best_distance:
                break
    
    return best_distance if best_distance < float('inf') else -1

# Example usage and test cases
if __name__ == "__main__":
    # Example graph: {node: [(neighbor, weight), ...]}
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    
    print("Distances from A:", dijkstra_basic(graph, 'A'))
    distance, path = dijkstra_with_path(graph, 'A', 'E')
    print(f"Shortest path A->E: distance={distance}, path={path}")
    
    # Example grid
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print("Grid shortest path:", dijkstra_grid(grid, (0, 0), (2, 2)))