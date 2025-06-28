"""
LeetCode Problems where Word Search Trie can be applied:

79. Word Search
212. Word Search II
1023. Camelcase Matching
1166. Design File System
1707. Maximum XOR With an Element From Array
1858. Longest Word With All Prefixes
2292. Products of a Local Array
527. Word Abbreviation
1065. Index Pairs of a String
425. Word Squares
"""

class WordSearchTrieNode:
    """Specialized Trie Node for word search problems"""
    
    def __init__(self):
        self.children = {}
        self.is_end_word = False
        self.word = None  # Store the complete word for easy retrieval
        self.ref = 0  # Reference counter for pruning

class WordSearchTrie:
    """
    Trie optimized for word search in 2D grids
    Includes pruning optimizations for better performance
    """
    
    def __init__(self):
        self.root = WordSearchTrieNode()
    
    def insert(self, word):
        """Insert word into trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = WordSearchTrieNode()
            node = node.children[char]
        
        node.is_end_word = True
        node.word = word
    
    def remove_word(self, word):
        """Remove word and prune unnecessary nodes"""
        def _remove_helper(node, word, index):
            if index == len(word):
                if node.is_end_word:
                    node.is_end_word = False
                    node.word = None
                    return len(node.children) == 0
                return False
            
            char = word[index]
            if char not in node.children:
                return False
            
            should_delete = _remove_helper(node.children[char], word, index + 1)
            
            if should_delete:
                del node.children[char]
                return not node.is_end_word and len(node.children) == 0
            
            return False
        
        _remove_helper(self.root, word, 0)

def exist(board, word):
    """
    LeetCode 79: Word Search
    Check if word exists in 2D character grid
    
    Uses backtracking with visited tracking
    Time: O(N * 4^L) where N = cells, L = word length
    """
    if not board or not board[0]:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def backtrack(row, col, index):
        # Base case: found complete word
        if index == len(word):
            return True
        
        # Check bounds and character match
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            board[row][col] != word[index]):
            return False
        
        # Mark cell as visited
        temp = board[row][col]
        board[row][col] = '#'
        
        # Explore all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        found = False
        
        for dr, dc in directions:
            if backtrack(row + dr, col + dc, index + 1):
                found = True
                break
        
        # Restore cell
        board[row][col] = temp
        return found
    
    # Try starting from each cell
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    
    return False

def findWords(board, words):
    """
    LeetCode 212: Word Search II
    Find all words from list that exist in 2D character grid
    
    Uses Trie + DFS for optimal performance with multiple words
    Time: O(N * 4^L * W) worst case, but much better with pruning
    """
    if not board or not board[0] or not words:
        return []
    
    # Build trie from words
    trie = WordSearchTrie()
    for word in words:
        trie.insert(word)
    
    rows, cols = len(board), len(board[0])
    result = []
    
    def dfs(row, col, node):
        # Get current character
        char = board[row][col]
        
        # Check if character exists in trie
        if char not in node.children:
            return
        
        node = node.children[char]
        
        # Check if we found a complete word
        if node.is_end_word:
            result.append(node.word)
            node.is_end_word = False  # Avoid duplicates
            # Optionally remove word from trie for optimization
            # trie.remove_word(node.word)
        
        # Mark cell as visited
        board[row][col] = '#'
        
        # Explore all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                board[new_row][new_col] != '#'):
                dfs(new_row, new_col, node)
        
        # Restore cell
        board[row][col] = char
    
    # Start DFS from each cell
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, trie.root)
    
    return result

def camelMatch(queries, pattern):
    """
    LeetCode 1023: Camelcase Matching
    Check if queries match camelcase pattern
    
    Uses trie-like pattern matching with case sensitivity
    """
    def matches_pattern(query, pattern):
        i = j = 0
        
        while i < len(query) and j < len(pattern):
            if query[i] == pattern[j]:
                i += 1
                j += 1
            elif query[i].islower():
                i += 1
            else:
                # Found uppercase letter not in pattern
                return False
        
        # Check remaining characters in query
        while i < len(query):
            if query[i].isupper():
                return False
            i += 1
        
        # Check if we matched entire pattern
        return j == len(pattern)
    
    return [matches_pattern(query, pattern) for query in queries]

class FileSystem:
    """
    LeetCode 1166: Design File System
    File system with path creation and value retrieval
    """
    
    def __init__(self):
        self.trie = {}
    
    def createPath(self, path, value):
        """Create path with given value"""
        if path == "/":
            return False
        
        components = [comp for comp in path.split('/') if comp]
        node = self.trie
        
        # Check if parent path exists
        for i, comp in enumerate(components[:-1]):
            if comp not in node:
                return False
            node = node[comp]
        
        # Create final component
        last_comp = components[-1]
        if last_comp in node:
            return False  # Path already exists
        
        node[last_comp] = {'value': value, 'children': {}}
        return True
    
    def get(self, path):
        """Get value for given path"""
        if path == "/":
            return -1
        
        components = [comp for comp in path.split('/') if comp]
        node = self.trie
        
        for comp in components:
            if comp not in node:
                return -1
            node = node[comp]
        
        return node.get('value', -1)

def findAllIndexPairs(text, words):
    """
    LeetCode 1065: Index Pairs of a String
    Find all index pairs where words appear as substrings
    
    Uses Trie for efficient multiple pattern matching
    """
    trie = WordSearchTrie()
    
    # Insert all words into trie
    for word in words:
        trie.insert(word)
    
    result = []
    n = len(text)
    
    # Check each starting position
    for i in range(n):
        node = trie.root
        
        # Extend as far as possible from position i
        for j in range(i, n):
            char = text[j]
            if char not in node.children:
                break
            
            node = node.children[char]
            
            # Check if we found a complete word
            if node.is_end_word:
                result.append([i, j])
    
    return result

def wordSquares(words):
    """
    LeetCode 425: Word Squares
    Build word squares where k-th row and column read the same
    
    Uses Trie for efficient prefix lookups during backtracking
    """
    if not words:
        return []
    
    # Build trie for prefix lookups
    trie = WordSearchTrie()
    for word in words:
        trie.insert(word)
    
    def get_words_with_prefix(prefix):
        """Get all words starting with prefix"""
        node = trie.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Collect all words from this node
        words_found = []
        
        def dfs(node, current_word):
            if node.is_end_word:
                words_found.append(current_word)
            for char, child_node in node.children.items():
                dfs(child_node, current_word + char)
        
        dfs(node, prefix)
        return words_found
    
    def backtrack(square):
        if len(square) == len(words[0]):
            return [square[:]]
        
        results = []
        
        # Determine prefix for next word
        row_index = len(square)
        prefix = ""
        for col_index in range(row_index):
            prefix += square[col_index][row_index]
        
        # Try all words with this prefix
        candidate_words = get_words_with_prefix(prefix)
        
        for word in candidate_words:
            # Check if this word is valid for current position
            valid = True
            
            # Check column constraints
            for col_index in range(row_index + 1, len(word)):
                column_prefix = ""
                for row in square:
                    column_prefix += row[col_index]
                column_prefix += word[col_index]
                
                if not any(w.startswith(column_prefix) for w in words):
                    valid = False
                    break
            
            if valid:
                square.append(word)
                results.extend(backtrack(square))
                square.pop()
        
        return results
    
    all_squares = []
    for word in words:
        all_squares.extend(backtrack([word]))
    
    return all_squares

class PatternMatcher:
    """
    Advanced pattern matching using Trie for complex patterns
    """
    
    def __init__(self):
        self.trie = WordSearchTrie()
    
    def add_pattern(self, pattern):
        """Add pattern to matcher"""
        self.trie.insert(pattern)
    
    def find_matches_in_text(self, text):
        """Find all pattern matches in text"""
        matches = []
        n = len(text)
        
        for i in range(n):
            node = self.trie.root
            for j in range(i, n):
                char = text[j]
                if char not in node.children:
                    break
                
                node = node.children[char]
                if node.is_end_word:
                    matches.append((i, j, node.word))
        
        return matches
    
    def find_matches_in_grid(self, grid):
        """Find pattern matches in 2D grid (all 8 directions)"""
        if not grid or not grid[0]:
            return []
        
        rows, cols = len(grid), len(grid[0])
        matches = []
        
        # 8 directions: right, down, diagonal, etc.
        directions = [
            (0, 1),   # right
            (1, 0),   # down
            (1, 1),   # diagonal down-right
            (1, -1),  # diagonal down-left
            (0, -1),  # left
            (-1, 0),  # up
            (-1, -1), # diagonal up-left
            (-1, 1)   # diagonal up-right
        ]
        
        def search_direction(start_row, start_col, dr, dc):
            """Search for patterns in specific direction"""
            node = self.trie.root
            r, c = start_row, start_col
            path = []
            
            while (0 <= r < rows and 0 <= c < cols):
                char = grid[r][c]
                if char not in node.children:
                    break
                
                node = node.children[char]
                path.append((r, c))
                
                if node.is_end_word:
                    matches.append({
                        'word': node.word,
                        'start': (start_row, start_col),
                        'end': (r, c),
                        'direction': (dr, dc),
                        'path': path[:]
                    })
                
                r += dr
                c += dc
        
        # Search from each starting position in all directions
        for i in range(rows):
            for j in range(cols):
                for dr, dc in directions:
                    search_direction(i, j, dr, dc)
        
        return matches

class MultiDimensionalWordSearch:
    """
    Word search in multiple dimensions and with various constraints
    """
    
    def __init__(self):
        self.trie = WordSearchTrie()
    
    def add_words(self, words):
        """Add multiple words to search for"""
        for word in words:
            self.trie.insert(word)
    
    def search_with_wildcards(self, board, wildcard='*'):
        """Search allowing wildcard characters"""
        if not board or not board[0]:
            return []
        
        rows, cols = len(board), len(board[0])
        results = []
        
        def dfs(row, col, node, path):
            if node.is_end_word:
                results.append({
                    'word': node.word,
                    'path': path[:],
                    'coordinates': [(r, c) for r, c in path]
                })
            
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            
            char = board[row][col]
            path.append((row, col))
            
            # Mark as visited
            board[row][col] = '#'
            
            # Try exact character match
            if char != '#' and char in node.children:
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    dfs(row + dr, col + dc, node.children[char], path)
            
            # Try wildcard match
            if char == wildcard:
                for next_char, child_node in node.children.items():
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    for dr, dc in directions:
                        dfs(row + dr, col + dc, child_node, path)
            
            # Restore state
            path.pop()
            board[row][col] = char
        
        # Start from each position
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, self.trie.root, [])
        
        return results
    
    def search_with_max_distance(self, board, max_distance):
        """Search with maximum allowed distance between consecutive characters"""
        if not board or not board[0]:
            return []
        
        rows, cols = len(board), len(board[0])
        results = []
        
        def calculate_distance(pos1, pos2):
            """Calculate Manhattan distance between positions"""
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
        
        def dfs(row, col, node, path, last_pos):
            if node.is_end_word:
                results.append({
                    'word': node.word,
                    'path': path[:],
                    'total_distance': sum(
                        calculate_distance(path[i], path[i+1]) 
                        for i in range(len(path)-1)
                    )
                })
            
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            
            # Check distance constraint
            if last_pos and calculate_distance(last_pos, (row, col)) > max_distance:
                return
            
            char = board[row][col]
            if char == '#' or char not in node.children:
                return
            
            # Mark as visited
            board[row][col] = '#'
            path.append((row, col))
            
            # Continue search from all reachable positions
            for i in range(rows):
                for j in range(cols):
                    if board[i][j] != '#':
                        dfs(i, j, node.children[char], path, (row, col))
            
            # Restore state
            path.pop()
            board[row][col] = char
        
        # Start from each position
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, self.trie.root, [], None)
        
        return results

# Template for optimized word search with pruning
def optimized_word_search(board, words):
    """
    Highly optimized word search with multiple pruning techniques
    """
    if not board or not board[0] or not words:
        return []
    
    # Build frequency map for early pruning
    board_freq = {}
    for row in board:
        for char in row:
            board_freq[char] = board_freq.get(char, 0) + 1
    
    # Filter words that can't possibly exist
    valid_words = []
    for word in words:
        word_freq = {}
        for char in word:
            word_freq[char] = word_freq.get(char, 0) + 1
        
        # Check if board has enough characters
        can_form = True
        for char, count in word_freq.items():
            if board_freq.get(char, 0) < count:
                can_form = False
                break
        
        if can_form:
            valid_words.append(word)
    
    if not valid_words:
        return []
    
    # Build trie with valid words
    trie = WordSearchTrie()
    for word in valid_words:
        trie.insert(word)
    
    rows, cols = len(board), len(board[0])
    result = set()
    
    def dfs(row, col, node, visited):
        char = board[row][col]
        
        if char not in node.children:
            return
        
        node = node.children[char]
        
        if node.is_end_word:
            result.add(node.word)
        
        # Mark as visited
        visited.add((row, col))
        
        # Explore neighbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                (new_row, new_col) not in visited):
                dfs(new_row, new_col, node, visited)
        
        # Backtrack
        visited.remove((row, col))
    
    # Start DFS from each cell
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, trie.root, set())
    
    return list(result)