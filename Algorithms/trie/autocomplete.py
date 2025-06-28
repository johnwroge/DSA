"""
LeetCode Problems where Autocomplete Trie can be applied:

208. Implement Trie (Prefix Tree)
211. Design Add and Search Words Data Structure
212. Word Search II
642. Design Search Autocomplete System
676. Implement Magic Dictionary
720. Longest Word in Dictionary
1268. Search Suggestions System
1233. Remove Sub-Folders from the Filesystem
1506. Find Root of N-Ary Tree
2416. Sum of Prefix Scores of Strings
"""

class TrieNode:
    """Standard Trie Node for autocomplete functionality"""
    
    def __init__(self):
        self.children = {}  # Character -> TrieNode
        self.is_end_word = False
        self.word = None  # Store complete word for easy retrieval
        self.frequency = 0  # For frequency-based suggestions
        self.suggestions = []  # Precomputed suggestions for faster retrieval

class Trie:
    """
    Basic Trie implementation for autocomplete
    
    Supports: insert, search, startsWith, delete
    Time: O(m) for all operations where m = word length
    Space: O(ALPHABET_SIZE * N * M) where N = number of words, M = avg length
    """
    
    def __init__(self):
        self.root = TrieNode()
        self.size = 0
    
    def insert(self, word):
        """Insert word into trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        if not node.is_end_word:
            self.size += 1
        node.is_end_word = True
        node.word = word
    
    def search(self, word):
        """Check if word exists in trie"""
        node = self._find_node(word)
        return node is not None and node.is_end_word
    
    def startsWith(self, prefix):
        """Check if any word starts with prefix"""
        return self._find_node(prefix) is not None
    
    def _find_node(self, prefix):
        """Helper to find node corresponding to prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    def delete(self, word):
        """Delete word from trie"""
        def _delete_helper(node, word, index):
            if index == len(word):
                if not node.is_end_word:
                    return False
                node.is_end_word = False
                node.word = None
                # Return True if node has no children (can be deleted)
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            should_delete_child = _delete_helper(node.children[char], word, index + 1)
            
            if should_delete_child:
                del node.children[char]
                # Return True if current node can be deleted
                return not node.is_end_word and len(node.children) == 0
            
            return False
        
        if self.search(word):
            _delete_helper(self.root, word, 0)
            self.size -= 1
    
    def get_all_words_with_prefix(self, prefix):
        """Get all words starting with prefix"""
        prefix_node = self._find_node(prefix)
        if not prefix_node:
            return []
        
        words = []
        self._dfs_collect_words(prefix_node, prefix, words)
        return words
    
    def _dfs_collect_words(self, node, current_word, words):
        """DFS to collect all words from current node"""
        if node.is_end_word:
            words.append(current_word)
        
        for char, child_node in node.children.items():
            self._dfs_collect_words(child_node, current_word + char, words)

class AutocompleteSystem:
    """
    LeetCode 642: Design Search Autocomplete System
    Support autocomplete with frequency-based suggestions
    """
    
    def __init__(self, sentences, times):
        self.trie = Trie()
        self.current_prefix = ""
        
        # Insert initial sentences with frequencies
        for sentence, frequency in zip(sentences, times):
            for _ in range(frequency):
                self.trie.insert(sentence)
        
        # Build frequency map
        self.frequency = {}
        for sentence, freq in zip(sentences, times):
            self.frequency[sentence] = freq
    
    def input(self, c):
        """Process input character and return top 3 suggestions"""
        if c == '#':
            # End of input - save current sentence
            if self.current_prefix:
                self.trie.insert(self.current_prefix)
                self.frequency[self.current_prefix] = self.frequency.get(self.current_prefix, 0) + 1
            self.current_prefix = ""
            return []
        
        self.current_prefix += c
        
        # Get all words with current prefix
        candidates = self.trie.get_all_words_with_prefix(self.current_prefix)
        
        # Sort by frequency (desc) then lexicographically (asc)
        candidates.sort(key=lambda x: (-self.frequency.get(x, 0), x))
        
        return candidates[:3]

class MagicDictionary:
    """
    LeetCode 676: Implement Magic Dictionary
    Dictionary that supports search with exactly one character difference
    """
    
    def __init__(self):
        self.trie = Trie()
    
    def buildDict(self, dictionary):
        """Build dictionary from word list"""
        for word in dictionary:
            self.trie.insert(word)
    
    def search(self, searchWord):
        """Search for word with exactly one character changed"""
        return self._search_with_mismatch(self.trie.root, searchWord, 0, False)
    
    def _search_with_mismatch(self, node, word, index, has_mismatch):
        """Recursive search allowing exactly one mismatch"""
        if index == len(word):
            return has_mismatch and node.is_end_word
        
        char = word[index]
        
        # Try exact match
        if char in node.children:
            if self._search_with_mismatch(node.children[char], word, index + 1, has_mismatch):
                return True
        
        # Try mismatch (only if we haven't used our mismatch yet)
        if not has_mismatch:
            for next_char, child_node in node.children.items():
                if next_char != char:
                    if self._search_with_mismatch(child_node, word, index + 1, True):
                        return True
        
        return False

class WordDictionary:
    """
    LeetCode 211: Design Add and Search Words Data Structure
    Support adding words and searching with '.' wildcard
    """
    
    def __init__(self):
        self.trie = Trie()
    
    def addWord(self, word):
        """Add word to dictionary"""
        self.trie.insert(word)
    
    def search(self, word):
        """Search word with '.' as wildcard for any character"""
        return self._search_helper(self.trie.root, word, 0)
    
    def _search_helper(self, node, word, index):
        """Recursive search handling wildcards"""
        if index == len(word):
            return node.is_end_word
        
        char = word[index]
        
        if char == '.':
            # Wildcard - try all possible characters
            for child_node in node.children.values():
                if self._search_helper(child_node, word, index + 1):
                    return True
            return False
        else:
            # Regular character
            if char not in node.children:
                return False
            return self._search_helper(node.children[char], word, index + 1)

def suggestedProducts(products, searchWord):
    """
    LeetCode 1268: Search Suggestions System
    Return top 3 lexicographically minimum products for each prefix
    """
    trie = Trie()
    
    # Sort products for lexicographical order
    products.sort()
    
    # Insert all products
    for product in products:
        trie.insert(product)
    
    result = []
    prefix = ""
    
    for char in searchWord:
        prefix += char
        suggestions = trie.get_all_words_with_prefix(prefix)
        suggestions.sort()  # Ensure lexicographical order
        result.append(suggestions[:3])  # Top 3 suggestions
    
    return result

def longestWord(words):
    """
    LeetCode 720: Longest Word in Dictionary
    Find longest word that can be built one character at a time
    """
    trie = Trie()
    
    # Insert all words
    for word in words:
        trie.insert(word)
    
    def can_build_incrementally(word):
        """Check if word can be built character by character"""
        for i in range(1, len(word)):
            if not trie.search(word[:i]):
                return False
        return True
    
    # Find longest word that can be built incrementally
    longest = ""
    for word in words:
        if can_build_incrementally(word):
            if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                longest = word
    
    return longest

class TrieWithFrequency:
    """
    Enhanced Trie with frequency tracking for better autocomplete
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, frequency=1):
        """Insert word with frequency"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.frequency += frequency  # Track frequency at each prefix
        
        node.is_end_word = True
        node.word = word
    
    def get_top_k_suggestions(self, prefix, k=3):
        """Get top k suggestions for prefix based on frequency"""
        prefix_node = self._find_node(prefix)
        if not prefix_node:
            return []
        
        # Collect all words with frequencies
        candidates = []
        self._collect_words_with_frequency(prefix_node, prefix, candidates)
        
        # Sort by frequency (desc) then lexicographically (asc)
        candidates.sort(key=lambda x: (-x[1], x[0]))
        
        return [word for word, freq in candidates[:k]]
    
    def _find_node(self, prefix):
        """Find node for given prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    def _collect_words_with_frequency(self, node, current_word, candidates):
        """Collect words with their frequencies"""
        if node.is_end_word:
            candidates.append((current_word, node.frequency))
        
        for char, child_node in node.children.items():
            self._collect_words_with_frequency(child_node, current_word + char, candidates)

def removeSubfolders(folder):
    """
    LeetCode 1233: Remove Sub-Folders from the Filesystem
    Remove folders that are subfolders of others
    """
    trie = Trie()
    
    # Insert all folder paths
    for path in folder:
        # Split path into components
        components = [comp for comp in path.split('/') if comp]
        trie.insert('/'.join(components))
    
    result = []
    
    def dfs(node, current_path):
        if node.is_end_word:
            result.append('/' + current_path.replace('/', '/'))
            return  # Don't explore subfolders
        
        for component, child_node in node.children.items():
            new_path = current_path + '/' + component if current_path else component
            dfs(child_node, new_path)
    
    dfs(trie.root, '')
    return result

class PrefixTrieOptimized:
    """
    Memory-optimized trie for prefix operations
    Uses compressed paths for better space efficiency
    """
    
    def __init__(self):
        self.root = {'is_end': False, 'edges': {}}
    
    def insert(self, word):
        """Insert word with path compression"""
        node = self.root
        i = 0
        
        while i < len(word):
            char = word[i]
            
            if char in node['edges']:
                # Follow existing edge
                edge_label, child_node = node['edges'][char]
                
                # Find common prefix
                j = 0
                while (j < len(edge_label) and 
                       i + j < len(word) and 
                       edge_label[j] == word[i + j]):
                    j += 1
                
                if j == len(edge_label):
                    # Consumed entire edge
                    node = child_node
                    i += j
                else:
                    # Need to split edge
                    common_prefix = edge_label[:j]
                    remaining_edge = edge_label[j:]
                    remaining_word = word[i + j:]
                    
                    # Create intermediate node
                    intermediate = {'is_end': False, 'edges': {}}
                    intermediate['edges'][remaining_edge[0]] = (remaining_edge, child_node)
                    
                    # Update current edge
                    node['edges'][char] = (common_prefix, intermediate)
                    
                    # Add remaining word
                    if remaining_word:
                        new_child = {'is_end': True, 'edges': {}}
                        intermediate['edges'][remaining_word[0]] = (remaining_word, new_child)
                    else:
                        intermediate['is_end'] = True
                    
                    return
            else:
                # Create new edge
                remaining_word = word[i:]
                new_child = {'is_end': True, 'edges': {}}
                node['edges'][char] = (remaining_word, new_child)
                return
        
        node['is_end'] = True
    
    def search(self, word):
        """Search for exact word"""
        node = self.root
        i = 0
        
        while i < len(word):
            char = word[i]
            
            if char not in node['edges']:
                return False
            
            edge_label, child_node = node['edges'][char]
            
            # Check if word matches edge label
            if i + len(edge_label) > len(word):
                return False
            
            if word[i:i + len(edge_label)] != edge_label:
                return False
            
            node = child_node
            i += len(edge_label)
        
        return node['is_end']

# Template for autocomplete with ranking
class RankedAutocomplete:
    """
    Autocomplete system with multiple ranking factors
    """
    
    def __init__(self):
        self.trie = TrieWithFrequency()
        self.word_scores = {}  # Additional scoring factors
    
    def add_word(self, word, frequency=1, score=0):
        """Add word with frequency and additional score"""
        self.trie.insert(word, frequency)
        self.word_scores[word] = score
    
    def suggest(self, prefix, k=5):
        """Get suggestions with combined ranking"""
        candidates = self.trie.get_all_words_with_prefix(prefix)
        
        # Calculate combined score
        scored_candidates = []
        for word in candidates:
            freq_node = self.trie._find_node(word)
            frequency = freq_node.frequency if freq_node else 0
            additional_score = self.word_scores.get(word, 0)
            
            # Combined score: frequency + additional factors
            combined_score = frequency + additional_score
            scored_candidates.append((word, combined_score))
        
        # Sort by score (desc) then alphabetically (asc)
        scored_candidates.sort(key=lambda x: (-x[1], x[0]))
        
        return [word for word, score in scored_candidates[:k]]