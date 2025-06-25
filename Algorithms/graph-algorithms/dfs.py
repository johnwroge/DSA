"""
DFS (Depth-First Search) Templates
Applicable LeetCode Problems:
- 104. Maximum Depth of Binary Tree
- 200. Number of Islands
- 207. Course Schedule
- 417. Pacific Atlantic Water Flow
- 463. Island Perimeter
- 695. Max Area of Island
- 733. Flood Fill
- 841. Keys and Rooms
- 1020. Number of Enclaves
- 1254. Number of Closed Islands
- 1971. Find if Path Exists in Graph
"""

from collections import defaultdict

def dfs_grid_recursive(grid, row, col, visited):
    """
    Recursive DFS for 2D grids
    Time: O(rows * cols), Space: O(rows * cols) for recursion stack
    """
    if (row < 0 or row >= len(grid) or 
        col < 0 or col >= len(grid[0]) or 
        (row, col) in visited or 
        grid[row][col] == 0):  # Adjust condition as needed
        return 0
    
    visited.add((row, col))
    size = 1  # Count current cell
    
    # Explore all 4 directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        size += dfs_grid_recursive(grid, row + dr, col + dc, visited)
    
    return size

def dfs_grid_iterative(grid, start_row, start_col):
    """
    Iterative DFS for 2D grids using stack
    Time: O(rows * cols), Space: O(rows * cols)
    """
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    stack = [(start_row, start_col)]
    result = []
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while stack:
        row, col = stack.pop()
        
        if ((row, col) in visited or 
            row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            grid[row][col] == 0):
            continue
        
        visited.add((row, col))
        result.append((row, col))
        
        for dr, dc in directions:
            stack.append((row + dr, col + dc))
    
    return result

def dfs_graph_recursive(graph, node, visited, result):
    """
    Recursive DFS for general graphs
    Time: O(V + E), Space: O(V)
    """
    visited.add(node)
    result.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_graph_recursive(graph, neighbor, visited, result)

def dfs_graph_iterative(graph, start):
    """
    Iterative DFS for general graphs
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add neighbors to stack (reverse order to maintain left-to-right traversal)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result

def detect_cycle_dfs(graph, num_nodes):
    """
    Detect cycle in directed graph using DFS
    Returns True if cycle exists
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_nodes
    
    def dfs(node):
        if color[node] == GRAY:  # Back edge found
            return True
        if color[node] == BLACK:  # Already processed
            return False
        
        color[node] = GRAY
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        color[node] = BLACK
        return False
    
    for i in range(num_nodes):
        if color[i] == WHITE:
            if dfs(i):
                return True
    return False

def detect_cycle_undirected_dfs(graph, num_nodes):
    """
    Detect cycle in undirected graph using DFS
    """
    visited = [False] * num_nodes
    
    def dfs(node, parent):
        visited[node] = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:  # Back edge (not to parent)
                return True
        return False
    
    for i in range(num_nodes):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False

def find_path_dfs(graph, start, target, path=[]):
    """
    Find path between two nodes using DFS
    """
    path = path + [start]
    
    if start == target:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in path:  # Avoid cycles
            new_path = find_path_dfs(graph, neighbor, target, path)
            if new_path:
                return new_path
    
    return None

def all_paths_dfs(graph, start, target):
    """
    Find all paths between two nodes using DFS
    """
    def dfs(node, path, all_paths):
        if node == target:
            all_paths.append(path[:])
            return
        
        for neighbor in graph[node]:
            if neighbor not in path:  # Avoid cycles
                path.append(neighbor)
                dfs(neighbor, path, all_paths)
                path.pop()  # Backtrack
    
    all_paths = []
    dfs(start, [start], all_paths)
    return all_paths

def number_of_islands_dfs(grid):
    """
    LeetCode 200: Number of Islands using DFS
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            (r, c) in visited or grid[r][c] == '0'):
            return
        
        visited.add((r, c))
        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and (i, j) not in visited:
                dfs(i, j)
                count += 1
    
    return count

def max_area_of_island_dfs(grid):
    """
    LeetCode 695: Max Area of Island using DFS
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    max_area = 0
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            (r, c) in visited or grid[r][c] == 0):
            return 0
        
        visited.add((r, c))
        area = 1
        # Explore all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            area += dfs(r + dr, c + dc)
        
        return area
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (i, j) not in visited:
                max_area = max(max_area, dfs(i, j))
    
    return max_area

def flood_fill_dfs(image, sr, sc, color):
    """
    LeetCode 733: Flood Fill using DFS
    """
    original_color = image[sr][sc]
    if original_color == color:
        return image
    
    rows, cols = len(image), len(image[0])
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            image[r][c] != original_color):
            return
        
        image[r][c] = color
        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    dfs(sr, sc)
    return image

def pacific_atlantic_water_flow(heights):
    """
    LeetCode 417: Pacific Atlantic Water Flow using DFS
    """
    if not heights or not heights[0]:
        return []
    
    rows, cols = len(heights), len(heights[0])
    pacific_reachable = set()
    atlantic_reachable = set()
    
    def dfs(r, c, reachable, prev_height):
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            (r, c) in reachable or heights[r][c] < prev_height):
            return
        
        reachable.add((r, c))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            dfs(r + dr, c + dc, reachable, heights[r][c])
    
    # Start DFS from borders
    for i in range(rows):
        dfs(i, 0, pacific_reachable, heights[i][0])  # Left border (Pacific)
        dfs(i, cols-1, atlantic_reachable, heights[i][cols-1])  # Right border (Atlantic)
    
    for j in range(cols):
        dfs(0, j, pacific_reachable, heights[0][j])  # Top border (Pacific)
        dfs(rows-1, j, atlantic_reachable, heights[rows-1][j])  # Bottom border (Atlantic)
    
    # Find intersection
    result = []
    for cell in pacific_reachable:
        if cell in atlantic_reachable:
            result.append(list(cell))
    
    return result

def keys_and_rooms_dfs(rooms):
    """
    LeetCode 841: Keys and Rooms using DFS
    """
    visited = set()
    
    def dfs(room):
        if room in visited:
            return
        
        visited.add(room)
        for key in rooms[room]:
            dfs(key)
    
    dfs(0)  # Start from room 0
    return len(visited) == len(rooms)

def binary_tree_max_depth_dfs(root):
    """
    LeetCode 104: Maximum Depth of Binary Tree using DFS
    """
    if not root:
        return 0
    
    return 1 + max(binary_tree_max_depth_dfs(root.left), 
                   binary_tree_max_depth_dfs(root.right))

def number_of_enclaves_dfs(grid):
    """
    LeetCode 1020: Number of Enclaves using DFS
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0):
            return
        
        grid[r][c] = 0  # Mark as visited/water
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    
    # Remove land connected to boundary
    for i in range(rows):
        dfs(i, 0)          # Left border
        dfs(i, cols - 1)   # Right border
    
    for j in range(cols):
        dfs(0, j)          # Top border
        dfs(rows - 1, j)   # Bottom border
    
    # Count remaining land
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count += 1
    
    return count

