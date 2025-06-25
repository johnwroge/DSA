"""
Topological Sort Templates
Applicable LeetCode Problems:
- 207. Course Schedule
- 210. Course Schedule II
- 269. Alien Dictionary
- 310. Minimum Height Trees
- 329. Longest Increasing Path in a Matrix
- 444. Sequence Reconstruction
- 630. Course Schedule III
- 802. Find Eventual Safe States
- 851. Loud and Rich
- 1136. Parallel Courses
- 1203. Sort Items by Groups Respecting Dependencies
- 1462. Course Schedule IV
- 2115. Find All Possible Recipes from Given Supplies
"""

from collections import deque, defaultdict

# =============== KAHN'S ALGORITHM (BFS-based) ===============

def topological_sort_kahn(graph, num_nodes):
    """
    Kahn's algorithm for topological sorting using BFS
    Returns topological order if no cycle, empty list if cycle exists
    Time: O(V + E), Space: O(V)
    """
    # Calculate in-degrees
    in_degree = [0] * num_nodes
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Initialize queue with nodes having 0 in-degree
    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Remove this node from the graph
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for cycle
    return result if len(result) == num_nodes else []

def can_finish_courses_kahn(num_courses, prerequisites):
    """
    LeetCode 207: Course Schedule using Kahn's algorithm
    """
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    # Build graph
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # BFS
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    completed = 0
    
    while queue:
        course = queue.popleft()
        completed += 1
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return completed == num_courses

def find_order_kahn(num_courses, prerequisites):
    """
    LeetCode 210: Course Schedule II using Kahn's algorithm
    """
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    result = []
    
    while queue:
        course = queue.popleft()
        result.append(course)
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return result if len(result) == num_courses else []

# =============== DFS-based TOPOLOGICAL SORT ===============

def topological_sort_dfs(graph, num_nodes):
    """
    DFS-based topological sorting
    Time: O(V + E), Space: O(V)
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_nodes
    result = []
    has_cycle = False
    
    def dfs(node):
        nonlocal has_cycle
        if color[node] == GRAY:  # Back edge - cycle detected
            has_cycle = True
            return
        if color[node] == BLACK:  # Already processed
            return
        
        color[node] = GRAY
        for neighbor in graph[node]:
            dfs(neighbor)
            if has_cycle:
                return
        
        color[node] = BLACK
        result.append(node)
    
    for i in range(num_nodes):
        if color[i] == WHITE:
            dfs(i)
            if has_cycle:
                return []
    
    return list(reversed(result))

def detect_cycle_and_sort_dfs(graph, num_nodes):
    """
    Combined cycle detection and topological sorting using DFS
    Returns (has_cycle, topological_order)
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_nodes
    result = []
    
    def dfs(node):
        if color[node] == GRAY:
            return True  # Cycle found
        if color[node] == BLACK:
            return False
        
        color[node] = GRAY
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        
        color[node] = BLACK
        result.append(node)
        return False
    
    for i in range(num_nodes):
        if color[i] == WHITE:
            if dfs(i):
                return True, []
    
    return False, list(reversed(result))

# =============== ADVANCED PATTERNS ===============

def alien_dictionary_topo(words):
    """
    LeetCode 269: Alien Dictionary using topological sort
    """
    # Build graph
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    chars = set()
    
    # Get all characters
    for word in words:
        for char in word:
            chars.add(char)
    
    # Initialize in_degree
    for char in chars:
        in_degree[char] = 0
    
    # Build graph from adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        
        # Check if word1 is prefix of word2 but longer
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""  # Invalid ordering
        
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
    
    # Topological sort
    queue = deque([char for char in chars if in_degree[char] == 0])
    result = []
    
    while queue:
        char = queue.popleft()
        result.append(char)
        
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return ''.join(result) if len(result) == len(chars) else ""

def minimum_height_trees(n, edges):
    """
    LeetCode 310: Minimum Height Trees
    Remove leaf nodes layer by layer until 1-2 nodes remain
    """
    if n <= 2:
        return list(range(n))
    
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize leaves (nodes with degree 1)
    leaves = deque([i for i in range(n) if len(graph[i]) == 1])
    remaining = n
    
    while remaining > 2:
        leaf_count = len(leaves)
        remaining -= leaf_count
        
        # Remove current leaves
        for _ in range(leaf_count):
            leaf = leaves.popleft()
            
            # Remove leaf from its neighbor
            neighbor = graph[leaf][0]
            graph[neighbor].remove(leaf)
            
            # If neighbor becomes a leaf, add to queue
            if len(graph[neighbor]) == 1:
                leaves.append(neighbor)
    
    return list(leaves)

def longest_increasing_path_topo(matrix):
    """
    LeetCode 329: Longest Increasing Path in a Matrix using topological sort
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    in_degree = [[0] * cols for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Calculate in-degrees
    for i in range(rows):
        for j in range(cols):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < rows and 0 <= nj < cols and 
                    matrix[ni][nj] > matrix[i][j]):
                    in_degree[ni][nj] += 1
    
    # Start from cells with in-degree 0
    queue = deque()
    for i in range(rows):
        for j in range(cols):
            if in_degree[i][j] == 0:
                queue.append((i, j))
    
    max_length = 0
    while queue:
        max_length += 1
        size = len(queue)
        
        for _ in range(size):
            i, j = queue.popleft()
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < rows and 0 <= nj < cols and 
                    matrix[ni][nj] > matrix[i][j]):
                    in_degree[ni][nj] -= 1
                    if in_degree[ni][nj] == 0:
                        queue.append((ni, nj))
    
    return max_length

def find_safe_states_topo(graph):
    """
    LeetCode 802: Find Eventual Safe States using topological sort
    Safe states are nodes that don't lead to cycles
    """
    n = len(graph)
    
    # Reverse the graph
    reverse_graph = [[] for _ in range(n)]
    in_degree = [0] * n
    
    for i in range(n):
        for neighbor in graph[i]:
            reverse_graph[neighbor].append(i)
            in_degree[i] += 1
    
    # Start from terminal nodes (out-degree 0 in original graph)
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    safe = [False] * n
    
    while queue:
        node = queue.popleft()
        safe[node] = True
        
        for neighbor in reverse_graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return [i for i in range(n) if safe[i]]
