"""
LeetCode Problems where Course Schedule Topological Sort can be applied:

207. Course Schedule
210. Course Schedule II
630. Course Schedule III
1462. Course Schedule IV
269. Alien Dictionary
310. Minimum Height Trees
329. Longest Increasing Path in a Matrix
444. Sequence Reconstruction
802. Find Eventual Safe States
851. Loud and Rich
1136. Parallel Courses
1203. Sort Items by Groups Respecting Dependencies
"""

from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    """
    LeetCode 207: Course Schedule
    Check if all courses can be finished (detect cycle in directed graph)
    
    Uses Kahn's algorithm (BFS-based topological sort)
    Time: O(V + E), Space: O(V + E)
    """
    # Build adjacency list and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Initialize queue with courses having no prerequisites
    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)
    
    completed_courses = 0
    
    # Process courses level by level
    while queue:
        course = queue.popleft()
        completed_courses += 1
        
        # Remove this course and update prerequisites for dependent courses
        for dependent_course in graph[course]:
            in_degree[dependent_course] -= 1
            if in_degree[dependent_course] == 0:
                queue.append(dependent_course)
    
    # If we completed all courses, no cycle exists
    return completed_courses == numCourses

def findOrder(numCourses, prerequisites):
    """
    LeetCode 210: Course Schedule II
    Return valid order to finish all courses, or empty if impossible
    
    Uses Kahn's algorithm to get topological ordering
    """
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    # Build graph
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Find courses with no prerequisites
    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)
    
    order = []
    
    while queue:
        course = queue.popleft()
        order.append(course)
        
        # Process dependent courses
        for dependent in graph[course]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    # Return order if all courses can be completed
    return order if len(order) == numCourses else []

def canFinishDFS(numCourses, prerequisites):
    """
    Alternative DFS-based approach for cycle detection
    
    Uses three states: 0 (unvisited), 1 (visiting), 2 (visited)
    """
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # 0: unvisited, 1: visiting (in current path), 2: visited (completed)
    state = [0] * numCourses
    
    def has_cycle(course):
        if state[course] == 1:  # Back edge found - cycle detected
            return True
        if state[course] == 2:  # Already processed
            return False
        
        state[course] = 1  # Mark as visiting
        
        # Check all dependent courses
        for dependent in graph[course]:
            if has_cycle(dependent):
                return True
        
        state[course] = 2  # Mark as completed
        return False
    
    # Check each course for cycles
    for i in range(numCourses):
        if state[i] == 0 and has_cycle(i):
            return False
    
    return True

def findOrderDFS(numCourses, prerequisites):
    """
    DFS-based topological sort
    Returns courses in reverse finishing order
    """
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    state = [0] * numCourses  # 0: unvisited, 1: visiting, 2: visited
    order = []
    
    def dfs(course):
        if state[course] == 1:  # Cycle detected
            return False
        if state[course] == 2:  # Already processed
            return True
        
        state[course] = 1  # Mark as visiting
        
        # Visit all dependent courses first
        for dependent in graph[course]:
            if not dfs(dependent):
                return False
        
        state[course] = 2  # Mark as completed
        order.append(course)  # Add to order after processing dependencies
        return True
    
    # Process all courses
    for i in range(numCourses):
        if state[i] == 0 and not dfs(i):
            return []  # Cycle detected
    
    return order[::-1]  # Reverse to get correct topological order

def scheduleCourse(courses):
    """
    LeetCode 630: Course Schedule III
    Maximum number of courses that can be taken
    
    Uses greedy approach with priority queue
    """
    import heapq
    
    # Sort courses by deadline
    courses.sort(key=lambda x: x[1])
    
    max_heap = []  # Store negative durations for max heap
    total_time = 0
    
    for duration, deadline in courses:
        # Try to add current course
        total_time += duration
        heapq.heappush(max_heap, -duration)
        
        # If we exceed deadline, remove the longest course taken so far
        if total_time > deadline:
            longest_duration = -heapq.heappop(max_heap)
            total_time -= longest_duration
    
    return len(max_heap)

def checkIfPrerequisite(numCourses, prerequisites, queries):
    """
    LeetCode 1462: Course Schedule IV
    Check if course pairs have prerequisite relationships
    
    Uses Floyd-Warshall to find all transitive dependencies
    """
    # Build adjacency matrix
    is_prereq = [[False] * numCourses for _ in range(numCourses)]
    
    # Direct prerequisites
    for u, v in prerequisites:
        is_prereq[u][v] = True
    
    # Floyd-Warshall to find transitive closure
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                is_prereq[i][j] = is_prereq[i][j] or (is_prereq[i][k] and is_prereq[k][j])
    
    # Answer queries
    return [is_prereq[u][v] for u, v in queries]

def alienOrder(words):
    """
    LeetCode 269: Alien Dictionary
    Determine order of characters in alien language
    
    Uses topological sort on character dependencies
    """
    # Build graph from adjacent word pairs
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    # Initialize in_degree for all characters
    for word in words:
        for char in word:
            in_degree[char] = 0
    
    # Compare adjacent words to find character order
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        
        # Check if word1 is prefix of word2 but longer (invalid)
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""
        
        # Find first differing character
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
    
    # Topological sort using Kahn's algorithm
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []
    
    while queue:
        char = queue.popleft()
        result.append(char)
        
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all characters are processed (no cycle)
    return ''.join(result) if len(result) == len(in_degree) else ""

def minimumSemesters(n, relations):
    """
    LeetCode 1136: Parallel Courses
    Minimum number of semesters to finish all courses
    
    Uses level-wise BFS (Kahn's algorithm with level tracking)
    """
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for prereq, course in relations:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Start with courses having no prerequisites
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    semesters = 0
    completed = 0
    
    while queue:
        semesters += 1
        level_size = len(queue)
        
        # Process all courses in current semester
        for _ in range(level_size):
            course = queue.popleft()
            completed += 1
            
            # Update dependent courses
            for dependent in graph[course]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
    
    return semesters if completed == n else -1

def eventualSafeNodes(graph):
    """
    LeetCode 802: Find Eventual Safe States
    Find nodes that eventually lead to terminal nodes
    
    Uses reverse topological sort (safe nodes have out-degree 0 eventually)
    """
    n = len(graph)
    reverse_graph = defaultdict(list)
    out_degree = [0] * n
    
    # Build reverse graph and calculate out-degrees
    for i in range(n):
        out_degree[i] = len(graph[i])
        for neighbor in graph[i]:
            reverse_graph[neighbor].append(i)
    
    # Start with terminal nodes (out-degree 0)
    queue = deque()
    for i in range(n):
        if out_degree[i] == 0:
            queue.append(i)
    
    safe_nodes = set()
    
    while queue:
        node = queue.popleft()
        safe_nodes.add(node)
        
        # Update nodes that point to current safe node
        for prev_node in reverse_graph[node]:
            out_degree[prev_node] -= 1
            if out_degree[prev_node] == 0:
                queue.append(prev_node)
    
    return sorted(safe_nodes)

class TopologicalSort:
    """
    Generic topological sort class with multiple algorithms
    """
    
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.in_degree = [0] * n
    
    def add_edge(self, u, v):
        """Add directed edge from u to v"""
        self.graph[u].append(v)
        self.in_degree[v] += 1
    
    def kahn_algorithm(self):
        """Kahn's algorithm (BFS-based) - returns topological order"""
        queue = deque()
        for i in range(self.n):
            if self.in_degree[i] == 0:
                queue.append(i)
        
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in self.graph[node]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order if len(order) == self.n else []  # Empty if cycle exists
    
    def dfs_topological_sort(self):
        """DFS-based topological sort"""
        state = [0] * self.n  # 0: unvisited, 1: visiting, 2: visited
        order = []
        
        def dfs(node):
            if state[node] == 1:  # Back edge - cycle detected
                return False
            if state[node] == 2:  # Already processed
                return True
            
            state[node] = 1  # Mark as visiting
            
            for neighbor in self.graph[node]:
                if not dfs(neighbor):
                    return False
            
            state[node] = 2  # Mark as completed
            order.append(node)
            return True
        
        # Process all nodes
        for i in range(self.n):
            if state[i] == 0 and not dfs(i):
                return []  # Cycle detected
        
        return order[::-1]  # Reverse for correct order
    
    def has_cycle(self):
        """Check if graph has cycle using DFS"""
        state = [0] * self.n
        
        def dfs(node):
            if state[node] == 1:
                return True  # Back edge found
            if state[node] == 2:
                return False
            
            state[node] = 1
            for neighbor in self.graph[node]:
                if dfs(neighbor):
                    return True
            state[node] = 2
            return False
        
        for i in range(self.n):
            if state[i] == 0 and dfs(i):
                return True
        return False
    
    def lexicographical_topological_sort(self):
        """Get lexicographically smallest topological ordering"""
        import heapq
        
        # Use min-heap instead of queue for lexicographical order
        heap = []
        for i in range(self.n):
            if self.in_degree[i] == 0:
                heapq.heappush(heap, i)
        
        order = []
        temp_in_degree = self.in_degree[:]
        
        while heap:
            node = heapq.heappop(heap)
            order.append(node)
            
            for neighbor in self.graph[node]:
                temp_in_degree[neighbor] -= 1
                if temp_in_degree[neighbor] == 0:
                    heapq.heappush(heap, neighbor)
        
        return order if len(order) == self.n else []

# Template for course scheduling with constraints
def solve_course_schedule_with_time(courses_with_time, max_time_per_semester):
    """
    Generic template for course scheduling with time constraints
    
    Args:
        courses_with_time: [(course_id, duration, prerequisites), ...]
        max_time_per_semester: maximum time allowed per semester
    
    Returns:
        List of semesters, each containing list of courses
    """
    n = len(courses_with_time)
    graph = defaultdict(list)
    in_degree = [0] * n
    course_duration = {}
    
    # Build dependency graph
    for i, (course_id, duration, prereqs) in enumerate(courses_with_time):
        course_duration[i] = duration
        for prereq in prereqs:
            # Find prereq index
            prereq_idx = next(j for j, (cid, _, _) in enumerate(courses_with_time) if cid == prereq)
            graph[prereq_idx].append(i)
            in_degree[i] += 1
    
    # Schedule courses semester by semester
    semesters = []
    available = deque([i for i in range(n) if in_degree[i] == 0])
    
    while available:
        current_semester = []
        current_time = 0
        next_available = deque()
        
        # Try to add courses to current semester within time limit
        while available:
            course = available.popleft()
            if current_time + course_duration[course] <= max_time_per_semester:
                current_semester.append(course)
                current_time += course_duration[course]
                
                # Update dependencies
                for dependent in graph[course]:
                    in_degree[dependent] -= 1
                    if in_degree[dependent] == 0:
                        next_available.append(dependent)
            else:
                next_available.append(course)
        
        if current_semester:
            semesters.append(current_semester)
        
        available = next_available
    
    return semesters