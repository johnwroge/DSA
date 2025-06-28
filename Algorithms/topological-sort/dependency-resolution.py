"""
LeetCode Problems where Dependency Resolution can be applied:

1203. Sort Items by Groups Respecting Dependencies
2115. Find All Possible Recipes from Given Supplies
444. Sequence Reconstruction
851. Loud and Rich
329. Longest Increasing Path in a Matrix
310. Minimum Height Trees
997. Find the Town Judge
1632. Rank Transform of a Matrix
1857. Largest Color Value in a Directed Graph
2050. Parallel Courses III
"""

from collections import defaultdict, deque
import heapq

def sortItems(n, m, group, beforeItems):
    """
    LeetCode 1203: Sort Items by Groups Respecting Dependencies
    Sort items respecting both item dependencies and group dependencies
    
    Uses nested topological sort - first on groups, then on items within groups
    """
    # Assign unique group IDs to ungrouped items
    group_id = m
    for i in range(n):
        if group[i] == -1:
            group[i] = group_id
            group_id += 1
    
    # Build item and group dependency graphs
    item_graph = defaultdict(list)
    item_indegree = [0] * n
    group_graph = defaultdict(set)
    group_indegree = defaultdict(int)
    
    # Initialize group indegrees
    for i in range(group_id):
        group_indegree[i] = 0
    
    for i in range(n):
        for prereq in beforeItems[i]:
            # Add item dependency
            item_graph[prereq].append(i)
            item_indegree[i] += 1
            
            # Add group dependency if items are in different groups
            if group[prereq] != group[i]:
                if group[i] not in group_graph[group[prereq]]:
                    group_graph[group[prereq]].add(group[i])
                    group_indegree[group[i]] += 1
    
    # Topological sort for groups
    def topological_sort_groups():
        queue = deque([g for g in group_indegree if group_indegree[g] == 0])
        group_order = []
        
        while queue:
            curr_group = queue.popleft()
            group_order.append(curr_group)
            
            for next_group in group_graph[curr_group]:
                group_indegree[next_group] -= 1
                if group_indegree[next_group] == 0:
                    queue.append(next_group)
        
        return group_order if len(group_order) == len(group_indegree) else []
    
    # Topological sort for items within a group
    def topological_sort_items(items):
        # Build subgraph for items in this group
        subgraph = defaultdict(list)
        sub_indegree = {item: 0 for item in items}
        
        for item in items:
            for prereq in beforeItems[item]:
                if prereq in sub_indegree:  # prereq is in same group
                    subgraph[prereq].append(item)
                    sub_indegree[item] += 1
        
        queue = deque([item for item in items if sub_indegree[item] == 0])
        item_order = []
        
        while queue:
            curr_item = queue.popleft()
            item_order.append(curr_item)
            
            for next_item in subgraph[curr_item]:
                sub_indegree[next_item] -= 1
                if sub_indegree[next_item] == 0:
                    queue.append(next_item)
        
        return item_order if len(item_order) == len(items) else []
    
    # Sort groups
    group_order = topological_sort_groups()
    if not group_order:
        return []
    
    # Group items by their group ID
    group_items = defaultdict(list)
    for i in range(n):
        group_items[group[i]].append(i)
    
    # Sort items within each group and combine
    result = []
    for g in group_order:
        if group_items[g]:
            item_order = topological_sort_items(group_items[g])
            if not item_order:
                return []
            result.extend(item_order)
    
    return result

def findAllRecipes(recipes, ingredients, supplies):
    """
    LeetCode 2115: Find All Possible Recipes from Given Supplies
    Find all recipes that can be made given initial supplies
    
    Uses topological sort where supplies are sources and recipes are nodes
    """
    # Build ingredient dependency graph
    graph = defaultdict(list)
    indegree = defaultdict(int)
    recipe_set = set(recipes)
    supply_set = set(supplies)
    
    for i, recipe in enumerate(recipes):
        indegree[recipe] = 0  # Initialize
        
        for ingredient in ingredients[i]:
            if ingredient in recipe_set:  # Ingredient is another recipe
                graph[ingredient].append(recipe)
                indegree[recipe] += 1
            elif ingredient not in supply_set:  # Ingredient not available
                indegree[recipe] = float('inf')  # Mark as impossible
    
    # Start with recipes that only need supplies (indegree 0)
    queue = deque()
    for recipe in recipes:
        if indegree[recipe] == 0:
            queue.append(recipe)
    
    makeable_recipes = []
    
    while queue:
        recipe = queue.popleft()
        makeable_recipes.append(recipe)
        
        # This recipe can now be used as ingredient for other recipes
        for dependent_recipe in graph[recipe]:
            if indegree[dependent_recipe] != float('inf'):
                indegree[dependent_recipe] -= 1
                if indegree[dependent_recipe] == 0:
                    queue.append(dependent_recipe)
    
    return makeable_recipes

def sequenceReconstruction(nums, sequences):
    """
    LeetCode 444: Sequence Reconstruction
    Check if nums is the only sequence that can be reconstructed from sequences
    
    Uses topological sort with uniqueness checking
    """
    n = len(nums)
    graph = defaultdict(list)
    indegree = defaultdict(int)
    
    # Initialize indegree for all numbers
    for num in nums:
        indegree[num] = 0
    
    # Build graph from sequences
    for seq in sequences:
        for i in range(len(seq) - 1):
            u, v = seq[i], seq[i + 1]
            if u not in indegree or v not in indegree:
                return False  # Invalid number
            
            graph[u].append(v)
            indegree[v] += 1
    
    # Topological sort with uniqueness check
    queue = deque([num for num in nums if indegree[num] == 0])
    result = []
    
    while queue:
        if len(queue) > 1:  # Multiple choices - not unique
            return False
        
        num = queue.popleft()
        result.append(num)
        
        for neighbor in graph[num]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return result == nums

def loudAndRich(richer, quiet):
    """
    LeetCode 851: Loud and Rich
    Find least quiet person among those at least as rich as person i
    
    Uses topological sort with DP to propagate minimum values
    """
    n = len(quiet)
    graph = defaultdict(list)
    indegree = [0] * n
    
    # Build graph: edge from richer person to poorer person
    for a, b in richer:  # a is richer than b
        graph[a].append(b)
        indegree[b] += 1
    
    # Initialize answer array
    answer = list(range(n))  # Initially, each person is their own answer
    
    # Topological sort starting from richest people (indegree 0)
    queue = deque([i for i in range(n) if indegree[i] == 0])
    
    while queue:
        person = queue.popleft()
        
        # Propagate this person's answer to all people they're richer than
        for poorer_person in graph[person]:
            # Update answer for poorer person if current person is quieter
            if quiet[answer[person]] < quiet[answer[poorer_person]]:
                answer[poorer_person] = answer[person]
            
            indegree[poorer_person] -= 1
            if indegree[poorer_person] == 0:
                queue.append(poorer_person)
    
    return answer

def longestIncreasingPath(matrix):
    """
    LeetCode 329: Longest Increasing Path in a Matrix
    Find longest increasing path in matrix using topological sort
    
    Uses implicit topological sort with memoization
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    memo = {}
    
    def dfs(r, c):
        if (r, c) in memo:
            return memo[(r, c)]
        
        max_length = 1  # At least the cell itself
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and 
                matrix[nr][nc] > matrix[r][c]):
                max_length = max(max_length, 1 + dfs(nr, nc))
        
        memo[(r, c)] = max_length
        return max_length
    
    result = 0
    for i in range(rows):
        for j in range(cols):
            result = max(result, dfs(i, j))
    
    return result

def findMinHeightTrees(n, edges):
    """
    LeetCode 310: Minimum Height Trees
    Find roots that give minimum height trees
    
    Uses iterative leaf removal (reverse topological sort)
    """
    if n <= 2:
        return list(range(n))
    
    # Build adjacency list
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    # Find initial leaves (degree 1)
    leaves = deque([i for i in range(n) if len(graph[i]) == 1])
    remaining = n
    
    # Remove leaves iteratively until 1 or 2 nodes remain
    while remaining > 2:
        leaf_count = len(leaves)
        remaining -= leaf_count
        
        # Remove current leaves
        for _ in range(leaf_count):
            leaf = leaves.popleft()
            neighbor = graph[leaf].pop()  # Only one neighbor for leaf
            graph[neighbor].remove(leaf)
            
            # Check if neighbor becomes a leaf
            if len(graph[neighbor]) == 1:
                leaves.append(neighbor)
    
    return list(leaves)

def findJudge(n, trust):
    """
    LeetCode 997: Find the Town Judge
    Find person who is trusted by everyone but trusts no one
    
    Uses in-degree and out-degree counting
    """
    if n == 1:
        return 1
    
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)
    
    for a, b in trust:
        out_degree[a] += 1
        in_degree[b] += 1
    
    # Judge has in_degree = n-1 and out_degree = 0
    for i in range(1, n + 1):
        if in_degree[i] == n - 1 and out_degree[i] == 0:
            return i
    
    return -1

def minimumTime(n, relations, time):
    """
    LeetCode 2050: Parallel Courses III
    Minimum time to complete all courses with parallel execution
    
    Uses topological sort with time calculation
    """
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for prereq, course in relations:
        graph[prereq].append(course)
        indegree[course] += 1
    
    # Use priority queue to process courses by completion time
    # (completion_time, course)
    pq = []
    completion_time = [0] * (n + 1)
    
    # Start with courses having no prerequisites
    for i in range(1, n + 1):
        if indegree[i] == 0:
            completion_time[i] = time[i - 1]
            heapq.heappush(pq, (completion_time[i], i))
    
    max_time = 0
    
    while pq:
        curr_time, course = heapq.heappop(pq)
        max_time = max(max_time, curr_time)
        
        # Update dependent courses
        for dependent in graph[course]:
            indegree[dependent] -= 1
            completion_time[dependent] = max(
                completion_time[dependent],
                curr_time + time[dependent - 1]
            )
            
            if indegree[dependent] == 0:
                heapq.heappush(pq, (completion_time[dependent], dependent))
    
    return max_time

class DependencyResolver:
    """
    Generic dependency resolution system
    """
    
    def __init__(self):
        self.dependencies = defaultdict(list)  # item -> list of dependencies
        self.dependents = defaultdict(list)    # item -> list of items that depend on it
        self.resolved = set()
        self.resolving = set()
    
    def add_dependency(self, item, dependency):
        """Add dependency: item depends on dependency"""
        self.dependencies[item].append(dependency)
        self.dependents[dependency].append(item)
    
    def resolve_dependencies(self, item):
        """Resolve dependencies for a specific item"""
        if item in self.resolved:
            return True
        
        if item in self.resolving:
            return False  # Circular dependency
        
        self.resolving.add(item)
        
        # Resolve all dependencies first
        for dependency in self.dependencies[item]:
            if not self.resolve_dependencies(dependency):
                return False
        
        self.resolving.remove(item)
        self.resolved.add(item)
        return True
    
    def get_installation_order(self, items):
        """Get order to install/process items respecting dependencies"""
        indegree = defaultdict(int)
        all_items = set(items)
        
        # Calculate indegrees
        for item in items:
            for dependency in self.dependencies[item]:
                if dependency in all_items:
                    indegree[item] += 1
        
        # Topological sort
        queue = deque([item for item in items if indegree[item] == 0])
        order = []
        
        while queue:
            item = queue.popleft()
            order.append(item)
            
            for dependent in self.dependents[item]:
                if dependent in all_items:
                    indegree[dependent] -= 1
                    if indegree[dependent] == 0:
                        queue.append(dependent)
        
        return order if len(order) == len(items) else []
    
    def check_circular_dependencies(self, items):
        """Check if there are circular dependencies among items"""
        for item in items:
            if not self.resolve_dependencies(item):
                return True
        return False
    
    def get_parallel_execution_plan(self, items):
        """Get plan for parallel execution - items that can run simultaneously"""
        indegree = defaultdict(int)
        all_items = set(items)
        
        for item in items:
            for dependency in self.dependencies[item]:
                if dependency in all_items:
                    indegree[item] += 1
        
        levels = []
        current_level = [item for item in items if indegree[item] == 0]
        
        while current_level:
            levels.append(current_level[:])
            next_level = []
            
            for item in current_level:
                for dependent in self.dependents[item]:
                    if dependent in all_items:
                        indegree[dependent] -= 1
                        if indegree[dependent] == 0:
                            next_level.append(dependent)
            
            current_level = next_level
        
        return levels

# Template for build system dependency resolution
def resolve_build_dependencies(targets, dependencies):
    """
    Resolve build order for targets with dependencies
    
    Args:
        targets: list of build targets
        dependencies: dict mapping target to list of dependencies
    
    Returns:
        Build order or None if circular dependencies exist
    """
    graph = defaultdict(list)
    indegree = defaultdict(int)
    
    # Initialize all targets
    for target in targets:
        indegree[target] = 0
    
    # Build dependency graph
    for target, deps in dependencies.items():
        for dep in deps:
            graph[dep].append(target)
            indegree[target] += 1
    
    # Topological sort
    queue = deque([target for target in targets if indegree[target] == 0])
    build_order = []
    
    while queue:
        target = queue.popleft()
        build_order.append(target)
        
        for dependent in graph[target]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)
    
    return build_order if len(build_order) == len(targets) else None

# Template for package manager dependency resolution
def install_packages(packages, dependencies, conflicts):
    """
    Resolve package installation order with conflicts
    
    Args:
        packages: list of packages to install
        dependencies: dict mapping package to list of required packages
        conflicts: list of (pkg1, pkg2) that cannot coexist
    
    Returns:
        Installation order and conflict resolution
    """
    # Check for conflicts
    package_set = set(packages)
    for pkg1, pkg2 in conflicts:
        if pkg1 in package_set and pkg2 in package_set:
            return None, f"Conflict between {pkg1} and {pkg2}"
    
    # Resolve dependencies using DependencyResolver
    resolver = DependencyResolver()
    
    for pkg, deps in dependencies.items():
        for dep in deps:
            resolver.add_dependency(pkg, dep)
    
    # Get installation order
    order = resolver.get_installation_order(packages)
    
    if not order:
        return None, "Circular dependencies detected"
    
    return order, "Success"