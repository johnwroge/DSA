"""
BFS (Breadth-First Search) Templates
Applicable LeetCode Problems:
- 102. Binary Tree Level Order Traversal
- 127. Word Ladder
- 200. Number of Islands
- 207. Course Schedule
- 286. Walls and Gates
- 542. 01 Matrix  
- 690. Employee Importance
- 733. Flood Fill
- 787. Cheapest Flights Within K Stops
- 994. Rotting Oranges
- 1091. Shortest Path in Binary Matrix
- 1162. As Far from Land as Possible
- 1926. Nearest Exit from Entrance in Maze
"""

from collections import deque, defaultdict

def bfs_grid(grid, start_row, start_col):
    """
    BFS template for 2D grids
    Time: O(rows * cols), Space: O(rows * cols)
    """
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start_row, start_col, 0)])  # (row, col, distance)
    visited.add((start_row, start_col))
    
    # 4-directional movement
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    result = []
    
    while queue:
        row, col, dist = queue.popleft()
        result.append((row, col, dist))
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited and
                grid[new_row][new_col] != 0):  # Adjust condition as needed
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))
    
    return result

def bfs_graph(graph, start):
    """
    BFS template for general graphs (adjacency list)
    Time: O(V + E), Space: O(V)
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

def bfs_shortest_path(graph, start, target):
    """
    BFS to find shortest path between two nodes
    Returns distance and path
    """
    if start == target:
        return 0, [start]
    
    visited = set()
    queue = deque([(start, 0, [start])])  # (node, distance, path)
    visited.add(start)
    
    while queue:
        node, dist, path = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor == target:
                return dist + 1, path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1, path + [neighbor]))
    
    return -1, []  # No path found

def multi_source_bfs(grid, sources):
    """
    Multi-source BFS (e.g., for problems like "01 Matrix" or "Rotting Oranges")
    """
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    visited = set()
    
    # Add all sources to queue
    for r, c in sources:
        queue.append((r, c, 0))
        visited.add((r, c))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    result = [[float('inf')] * cols for _ in range(rows)]
    
    while queue:
        row, col, dist = queue.popleft()
        result[row][col] = dist
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))
    
    return result

def bfs_level_order(root):
    """
    BFS for binary tree level order traversal
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

def walls_and_gates(rooms):
    """
    LeetCode 286: Walls and Gates
    Multi-source BFS from all gates
    """
    if not rooms or not rooms[0]:
        return
    
    rows, cols = len(rooms), len(rooms[0])
    queue = deque()
    
    # Find all gates (value 0)
    for i in range(rows):
        for j in range(cols):
            if rooms[i][j] == 0:
                queue.append((i, j))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        row, col = queue.popleft()
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                rooms[new_row][new_col] == 2147483647):  # Empty room
                
                rooms[new_row][new_col] = rooms[row][col] + 1
                queue.append((new_row, new_col))

def rotting_oranges(grid):
    """
    LeetCode 994: Rotting Oranges
    Multi-source BFS from all rotten oranges
    """
    if not grid or not grid[0]:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    
    # Find all rotten oranges and count fresh ones
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh_count += 1
    
    if fresh_count == 0:
        return 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_time = 0
    
    while queue:
        row, col, time = queue.popleft()
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                grid[new_row][new_col] == 1):
                
                grid[new_row][new_col] = 2
                fresh_count -= 1
                max_time = max(max_time, time + 1)
                queue.append((new_row, new_col, time + 1))
    
    return max_time if fresh_count == 0 else -1

def shortest_path_binary_matrix(grid):
    """
    LeetCode 1091: Shortest Path in Binary Matrix
    """
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    if n == 1:
        return 1
    
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    visited = {(0, 0)}
    
    # 8-directional movement
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    while queue:
        row, col, path_len = queue.popleft()
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < n and 
                0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                if new_row == n-1 and new_col == n-1:
                    return path_len + 1
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, path_len + 1))
    
    return -1

def word_ladder_bfs(beginWord, endWord, wordList):
    """
    LeetCode 127: Word Ladder
    """
    if endWord not in wordList:
        return 0
    
    wordSet = set(wordList)
    queue = deque([(beginWord, 1)])
    visited = {beginWord}
    
    while queue:
        word, length = queue.popleft()
        
        if word == endWord:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                
                if new_word in wordSet and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, length + 1))
    
    return 0

