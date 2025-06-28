# Topological Sort Algorithms

This repository contains implementations of topological sorting algorithms specialized for **Course Scheduling** and **Dependency Resolution** problems, along with advanced variations and optimization techniques.

## What is Topological Sorting?

Topological sorting is a linear ordering of vertices in a **directed acyclic graph (DAG)** such that for every directed edge (u, v), vertex u appears before vertex v in the ordering.

### Key Properties:
- **Only works on DAGs**: Directed graphs with no cycles
- **Multiple valid orderings**: Usually many correct topological orders exist
- **Dependency resolution**: Perfect for problems involving prerequisites or dependencies
- **Linear time**: Both major algorithms run in O(V + E) time

## Core Applications

| Domain | Problem Type | Example |
|--------|-------------|---------|
| **Academic** | Course scheduling | Prerequisites, graduation planning |
| **Software** | Build systems | Compilation order, package dependencies |
| **Project Management** | Task scheduling | Project planning, resource allocation |
| **Manufacturing** | Process ordering | Assembly lines, workflow management |
| **Data Processing** | Pipeline design | ETL processes, data workflows |

## Algorithm Comparison

| Algorithm | Approach | Cycle Detection | Lexicographic Order | Memory Usage |
|-----------|----------|----------------|-------------------|--------------|
| **Kahn's Algorithm** | BFS-based | ✅ Easy | ✅ Possible | O(V) queue |
| **DFS-based** | Recursion | ✅ Natural | ❌ Harder | O(V) stack depth |

## 1. Kahn's Algorithm (BFS-based)

### 🎯 Core Concept
Uses **in-degree counting** and **BFS** to process nodes level by level, starting from nodes with no incoming edges.

### ⚙️ Algorithm Steps
1. **Calculate in-degrees** for all vertices
2. **Add zero in-degree vertices** to queue
3. **Process queue**: Remove vertex, decrease neighbors' in-degrees
4. **Add newly zero in-degree vertices** to queue
5. **Check completeness**: All vertices processed = no cycle

### 📝 Key Advantages
- **Easy cycle detection**: If not all vertices processed, cycle exists
- **Level-by-level processing**: Natural for parallel scheduling
- **Lexicographic ordering**: Easy with priority queue instead of regular queue
- **Intuitive logic**: Mirrors real-world dependency resolution

### 🎯 When to Choose Kahn's Algorithm
```
✅ Choose when:
- Need to detect cycles easily
- Want lexicographically smallest ordering
- Processing items in parallel batches/levels
- Building scheduling systems

❌ Don't choose when:
- Memory usage is critical (needs queue + in-degree array)
- Working with very dense graphs
- Need multiple orderings simultaneously
```

### 💡 Implementation Pattern
```python
def kahns_topological_sort(graph, n):
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == n else []  # Empty if cycle
```

## 2. DFS-based Topological Sort

### 🎯 Core Concept
Uses **depth-first search** with **three-color system** to detect cycles and build ordering in reverse finishing order.

### ⚙️ Algorithm Steps
1. **Mark all vertices** as unvisited (white)
2. **For each unvisited vertex**, start DFS
3. **Mark as visiting** (gray) when processing starts
4. **Recursively visit** all unvisited neighbors
5. **Mark as visited** (black) when processing completes
6. **Add to result** in reverse finishing order

### 📝 Key Advantages
- **Space efficient**: Only needs recursion stack and color array
- **Natural cycle detection**: Back edges (gray → gray) indicate cycles
- **Multiple DFS trees**: Can handle disconnected components
- **Reverse chronological**: Natural for dependency chains

### 🎯 When to Choose DFS-based
```
✅ Choose when:
- Memory usage is critical
- Graph is sparse or disconnected
- Need to understand dependency chains
- Working with recursive problems

❌ Don't choose when:
- Need lexicographic ordering
- Want level-by-level processing
- Stack overflow is a concern (very deep graphs)
- Prefer iterative approaches
```

### 💡 Implementation Pattern
```python
def dfs_topological_sort(graph, n):
    color = [0] * n  # 0: white, 1: gray, 2: black
    result = []
    
    def dfs(node):
        if color[node] == 1:  # Back edge - cycle detected
            return False
        if color[node] == 2:  # Already processed
            return True
        
        color[node] = 1  # Mark as visiting
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        
        color[node] = 2  # Mark as visited
        result.append(node)
        return True
    
    for i in range(n):
        if color[i] == 0 and not dfs(i):
            return []  # Cycle detected
    
    return result[::-1]  # Reverse for correct order
```

## Problem Pattern Recognition

### 🔍 Course Scheduling Patterns

| Pattern | Description | Example Problems |
|---------|-------------|------------------|
| **Basic Feasibility** | "Can all courses be completed?" | LeetCode 207 |
| **Find Valid Order** | "Return any valid completion order" | LeetCode 210 |
| **Optimal Scheduling** | "Minimum time/semesters needed" | LeetCode 630, 1136 |
| **Query Dependencies** | "Is A prerequisite of B?" | LeetCode 1462 |

```python
# Pattern recognition signals:
"prerequisite", "course", "schedule", "semester", "complete"
"before", "after", "depends on", "required"
```

### 🔧 Dependency Resolution Patterns

| Pattern | Description | Example Problems |
|---------|-------------|------------------|
| **Multi-level Dependencies** | Nested dependency relationships | LeetCode 1203 |
| **Resource Availability** | Items available based on supplies | LeetCode 2115 |
| **Unique Reconstruction** | Only one valid ordering exists | LeetCode 444 |
| **Propagation Problems** | Values propagate through dependencies | LeetCode 851 |

```python
# Pattern recognition signals:
"dependency", "installation", "build", "recipe", "supplies"
"order", "sequence", "arrangement", "process"
```

## Decision Framework

### 🎯 Quick Algorithm Selection

```
What's your primary goal?

📚 Course Scheduling
├── Just check if possible? → Kahn's (cycle detection)
├── Need specific order? → Kahn's or DFS
├── Minimum time/levels? → Kahn's with level tracking
└── Query relationships? → Floyd-Warshall + topological

🔧 Dependency Resolution  
├── Package installation? → Kahn's (natural model)
├── Build system? → DFS (dependency chains)
├── Parallel execution? → Kahn's (level processing)
└── Complex constraints? → Custom hybrid approach

⚡ Performance Critical
├── Memory constrained? → DFS-based
├── Need lexicographic? → Kahn's with priority queue
├── Many disconnected components? → DFS-based
└── Very dense graph? → Consider both, profile
```

### 🎯 Problem Type Mapping

| Problem Keywords | Algorithm Choice | Key Insight |
|-----------------|------------------|-------------|
| **"course schedule"** | Kahn's Algorithm | Natural prerequisite model |
| **"minimum time/semesters"** | Kahn's with levels | Level-by-level processing |
| **"installation order"** | Kahn's Algorithm | Dependency satisfaction |
| **"build dependencies"** | DFS-based | Dependency chain analysis |
| **"lexicographically smallest"** | Kahn's + Priority Queue | Natural ordering support |
| **"detect circular"** | Either (Kahn's easier) | Cycle detection |
| **"parallel execution"** | Kahn's with levels | Batch processing |

## Advanced Techniques

### 🚀 Optimization Strategies

#### 1. Lexicographic Topological Sort
```python
def lexicographic_topological_sort(graph, n):
    import heapq
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1
    
    # Use min-heap instead of queue
    heap = [i for i in range(n) if in_degree[i] == 0]
    heapq.heapify(heap)
    
    result = []
    while heap:
        node = heapq.heappop(heap)
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)
    
    return result if len(result) == n else []
```

#### 2. Parallel Execution Planning
```python
def get_parallel_levels(graph, n):
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1
    
    levels = []
    current_level = [i for i in range(n) if in_degree[i] == 0]
    
    while current_level:
        levels.append(current_level[:])
        next_level = []
        
        for node in current_level:
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    next_level.append(neighbor)
        
        current_level = next_level
    
    return levels
```

#### 3. All Topological Orderings
```python
def all_topological_sorts(graph, n):
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1
    
    def backtrack(path, remaining_in_degree):
        if len(path) == n:
            return [path[:]]
        
        results = []
        for node in range(n):
            if remaining_in_degree[node] == 0 and node not in path:
                # Add this node to path
                path.append(node)
                new_in_degree = remaining_in_degree[:]
                new_in_degree[node] = -1  # Mark as used
                
                # Update in-degrees
                for neighbor in graph[node]:
                    new_in_degree[neighbor] -= 1
                
                results.extend(backtrack(path, new_in_degree))
                path.pop()
        
        return results
    
    return backtrack([], in_degree)
```

## Performance Considerations

### 🚀 Time Complexity
- **Both algorithms**: O(V + E) for basic topological sort
- **Lexicographic**: O(V log V + E) due to priority queue
- **All orderings**: O(V! × (V + E)) - exponential
- **Level processing**: O(V + E) with O(V) levels

### 💾 Space Complexity
- **Kahn's**: O(V) for queue + in-degree array
- **DFS**: O(V) for recursion stack + color array  
- **Lexicographic**: O(V) for priority queue
- **Level processing**: O(V) for level storage

### ⚡ Practical Optimizations

1. **Use adjacency lists** for sparse graphs
2. **Avoid recursion** for very deep graphs (iterative DFS)
3. **Batch processing** for parallel execution
4. **Early termination** when cycle detected
5. **Memory pooling** for frequent operations

## Common Pitfalls and Solutions

### ⚠️ Frequent Mistakes

1. **Forgetting cycle detection**: Always check if all vertices processed
2. **Incorrect in-degree calculation**: Count edges properly
3. **Modifying original graph**: Use copies if needed for multiple sorts
4. **Stack overflow in DFS**: Use iterative version for deep graphs
5. **Wrong edge direction**: Ensure dependencies point correctly

### 💡 Best Practices

1. **Always validate input**: Check for self-loops, valid indices
2. **Handle empty graphs**: Edge case with no vertices/edges
3. **Clear error messaging**: Specify where cycles detected
4. **Use appropriate data structures**: Lists vs sets for different needs
5. **Document edge directions**: Make dependency relationships clear

## Real-World Applications

### 🌟 Industry Use Cases

#### Software Development
- **Build Systems**: Maven, Gradle dependency resolution
- **Package Managers**: npm, pip installation order
- **Code Analysis**: Import dependency checking
- **Deployment**: Service startup ordering

#### Project Management
- **Task Scheduling**: Critical path method (CPM)
- **Resource Planning**: Equipment and personnel allocation
- **Manufacturing**: Assembly line sequencing
- **Supply Chain**: Supplier dependency management

#### Academic Systems
- **Curriculum Design**: Course prerequisite planning
- **Graduation Planning**: Degree requirement satisfaction
- **Research Dependencies**: Paper citation analysis
- **Skill Development**: Learning path optimization

## Interview Strategy

### 🎯 Problem Recognition

1. **Look for keywords**: "prerequisite", "dependency", "order", "schedule"
2. **Identify relationships**: What depends on what?
3. **Check for cycles**: Are circular dependencies possible?
4. **Consider constraints**: Time limits, parallel processing, lexicographic order

### 🔄 Solution Approach

1. **Model as directed graph**: Items as vertices, dependencies as edges
2. **Choose appropriate algorithm**: Based on requirements and constraints
3. **Handle edge cases**: Empty input, cycles, disconnected components
4. **Optimize if needed**: Lexicographic order, parallel levels, multiple solutions

### 💪 Practice Progression

1. **Master basic topological sort** - understand both algorithms
2. **Practice cycle detection** - key for validation
3. **Learn level processing** - important for scheduling
4. **Tackle complex constraints** - multi-level dependencies
5. **Optimize for specific needs** - lexicographic, parallel, etc.

## Template Selection Guide

### For Course Scheduling Problems:
- **Basic feasibility**: Use Kahn's algorithm
- **Need specific order**: Use either algorithm
- **Minimum time**: Use Kahn's with level tracking
- **Lexicographic order**: Use Kahn's with priority queue

### For Dependency Resolution:
- **Package installation**: Use Kahn's algorithm
- **Build systems**: Consider DFS for dependency chains
- **Complex multi-level**: Custom approach with nested topological sorts
- **Parallel execution**: Use Kahn's with level processing

Choose the algorithm and variation that best matches your specific requirements. Start with the basic template and add optimizations as needed for your use case!