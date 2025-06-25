"""
Union-Find (Disjoint Set Union) Template
Applicable LeetCode Problems:
- 200. Number of Islands
- 547. Number of Provinces  
- 684. Redundant Connection
- 685. Redundant Connection II
- 721. Accounts Merge
- 737. Sentence Similarity II
- 765. Couples Holding Hands
- 778. Swim in Rising Water
- 803. Bricks Falling When Hit
- 827. Making A Large Island
- 839. Similar String Groups
- 924. Minimize Malware Spread
- 952. Largest Component Size by Common Factor
- 959. Regions Cut By Slashes
- 990. Satisfiability of Equality Equations
- 1202. Smallest String With Swaps
- 1319. Number of Operations to Make Network Connected
- 1361. Validate Binary Tree Nodes
- 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
- 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
"""

class UnionFind:
    """
    Basic Union-Find with path compression and union by rank
    Time: O(α(n)) per operation where α is inverse Ackermann function (practically constant)
    Space: O(n)
    """
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Number of connected components
    
    def find(self, x):
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        """Union two sets by rank"""
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            
            self.count -= 1
            return True
        return False
    
    def connected(self, x, y):
        """Check if two elements are in the same set"""
        return self.find(x) == self.find(y)
    
    def get_components(self):
        """Return number of connected components"""
        return self.count
    
    def get_component_sizes(self):
        """Return dictionary mapping root -> component size"""
        from collections import defaultdict
        sizes = defaultdict(int)
        for i in range(len(self.parent)):
            sizes[self.find(i)] += 1
        return dict(sizes)

class WeightedUnionFind:
    """
    Weighted Union-Find for problems involving distances/weights
    Useful for problems where you need to track relative positions
    """
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.weight = [0] * n  # weight[x] = weight from x to its parent
        self.count = n
    
    def find(self, x):
        """Find root and update weights (path compression)"""
        if self.parent[x] != x:
            root = self.find(self.parent[x])
            self.weight[x] += self.weight[self.parent[x]]
            self.parent[x] = root
        return self.parent[x]
    
    def union(self, x, y, w):
        """Union x and y with weight: weight(y) = weight(x) + w"""
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x != root_y:
            self.parent[root_y] = root_x
            self.weight[root_y] = self.weight[x] - self.weight[y] + w
            self.count -= 1
            return True
        else:
            # Check if the new edge is consistent
            return self.weight[y] == self.weight[x] + w
    
    def diff(self, x, y):
        """Return weight(y) - weight(x) if connected, None otherwise"""
        if self.find(x) == self.find(y):
            return self.weight[y] - self.weight[x]
        return None

class UnionFindWithSize:
    """
    Union-Find that tracks size of each component
    """
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n
        self.max_size = 1
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x != root_y:
            # Union by size
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.max_size = max(self.max_size, self.size[root_x])
            self.count -= 1
            return True
        return False
    
    def get_size(self, x):
        """Get size of component containing x"""
        return self.size[self.find(x)]
    
    def get_max_size(self):
        """Get size of largest component"""
        return self.max_size

# =============== COMMON PATTERNS ===============

def number_of_islands_uf(grid):
    """
    LeetCode 200: Number of Islands using Union-Find
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    # Count water cells to subtract from total
    water_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '0':
                water_count += 1
    
    uf = UnionFind(rows * cols)
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < rows and 0 <= nj < cols and 
                        grid[ni][nj] == '1'):
                        uf.union(i * cols + j, ni * cols + nj)
    
    return uf.get_components() - water_count

def accounts_merge_uf(accounts):
    """
    LeetCode 721: Accounts Merge using Union-Find
    """
    uf = UnionFind(len(accounts))
    email_to_account = {}
    
    # Map emails to account indices
    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_account:
                uf.union(i, email_to_account[email])
            else:
                email_to_account[email] = i
    
    # Group emails by account root
    from collections import defaultdict
    account_emails = defaultdict(list)
    for email, account_idx in email_to_account.items():
        root = uf.find(account_idx)
        account_emails[root].append(email)
    
    # Build result
    result = []
    for root, emails in account_emails.items():
        name = accounts[root][0]
        result.append([name] + sorted(emails))
    
    return result

def redundant_connection_uf(edges):
    """
    LeetCode 684: Redundant Connection using Union-Find
    """
    uf = UnionFind(len(edges) + 1)
    
    for u, v in edges:
        if uf.connected(u, v):
            return [u, v]
        uf.union(u, v)
    
    return []

def min_spanning_tree_kruskal(n, edges):
    """
    Kruskal's algorithm for Minimum Spanning Tree using Union-Find
    edges: [(weight, u, v), ...]
    """
    edges.sort()  # Sort by weight
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []
    
    for weight, u, v in edges:
        if uf.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v))
            
            if len(mst_edges) == n - 1:
                break
    
    return mst_weight, mst_edges

def satisfiability_equations_uf(equations):
    """
    LeetCode 990: Satisfiability of Equality Equations
    """
    uf = UnionFind(26)  # 26 letters
    
    # Process equality equations first
    for eq in equations:
        if eq[1] == '=':
            x, y = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
            uf.union(x, y)
    
    # Check inequality equations
    for eq in equations:
        if eq[1] == '!':
            x, y = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
            if uf.connected(x, y):
                return False
    
    return True

# Example usage
if __name__ == "__main__":
    # Basic usage
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(2, 3)
    print(f"Components: {uf.get_components()}")  # 3
    print(f"0 and 1 connected: {uf.connected(0, 1)}")  # True
    print(f"0 and 2 connected: {uf.connected(0, 2)}")  # False
    
    # With size tracking
    uf_size = UnionFindWithSize(4)
    uf_size.union(0, 1)
    uf_size.union(2, 3)
    uf_size.union(0, 2)
    print(f"Max component size: {uf_size.get_max_size()}")  # 4