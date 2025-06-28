"""
LeetCode Problems where Dictionary Trie can be applied:

208. Implement Trie (Prefix Tree)
336. Palindrome Pairs
421. Maximum XOR of Two Numbers in an Array
677. Map Sum Pairs
745. Prefix and Suffix Search
820. Short Encoding of Words
1065. Index Pairs of a String
472. Concatenated Words
648. Replace Words
1804. Implement Trie II (Prefix Tree)
1858. Longest Word With All Prefixes
2416. Sum of Prefix Scores of Strings
"""

class DictionaryTrieNode:
    """Enhanced Trie Node for dictionary operations"""
    
    def __init__(self):
        self.children = {}
        self.is_end_word = False
        self.word = None
        self.count = 0  # Number of words passing through this node
        self.value = 0  # For map-sum operations
        self.prefix_count = 0  # Count of words with this prefix

class DictionaryTrie:
    """
    Enhanced Trie for advanced dictionary operations
    
    Supports: insert, search, delete, prefix operations, counting
    """
    
    def __init__(self):
        self.root = DictionaryTrieNode()
        self.word_count = 0
    
    def insert(self, word, value=1):
        """Insert word with optional value"""
        node = self.root
        node.count += 1
        
        for char in word:
            if char not in node.children:
                node.children[char] = DictionaryTrieNode()
            node = node.children[char]
            node.count += 1
            node.prefix_count += 1
        
        if not node.is_end_word:
            self.word_count += 1
        
        node.is_end_word = True
        node.word = word
        node.value = value
    
    def search(self, word):
        """Search for exact word"""
        node = self._find_node(word)
        return node is not None and node.is_end_word
    
    def startsWith(self, prefix):
        """Check if any word starts with prefix"""
        return self._find_node(prefix) is not None
    
    def countWordsEqualTo(self, word):
        """Count occurrences of exact word"""
        node = self._find_node(word)
        return 1 if node and node.is_end_word else 0
    
    def countWordsStartingWith(self, prefix):
        """Count words starting with prefix"""
        node = self._find_node(prefix)
        return node.prefix_count if node else 0
    
    def _find_node(self, prefix):
        """Helper to find node for prefix"""
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
                node.prefix_count -= 1
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            should_delete = _delete_helper(node.children[char], word, index + 1)
            node.prefix_count -= 1
            
            if should_delete:
                del node.children[char]
                return not node.is_end_word and len(node.children) == 0
            
            return False
        
        if self.search(word):
            _delete_helper(self.root, word, 0)
            self.word_count -= 1

class MapSum:
    """
    LeetCode 677: Map Sum Pairs
    Trie that supports sum of values for all words with given prefix
    """
    
    def __init__(self):
        self.trie = DictionaryTrie()
        self.word_values = {}  # Track individual word values
    
    def insert(self, key, val):
        """Insert key-value pair"""
        # Calculate delta for existing key
        delta = val - self.word_values.get(key, 0)
        self.word_values[key] = val
        
        # Update trie with delta
        node = self.trie.root
        for char in key:
            if char not in node.children:
                node.children[char] = DictionaryTrieNode()
            node = node.children[char]
            node.value += delta
        
        node.is_end_word = True
        node.word = key
    
    def sum(self, prefix):
        """Sum all values of words starting with prefix"""
        node = self.trie._find_node(prefix)
        return node.value if node else 0

class WordFilter:
    """
    LeetCode 745: Prefix and Suffix Search
    Support queries for words with given prefix and suffix
    """
    
    def __init__(self, words):
        self.trie = DictionaryTrie()
        
        # Insert all suffix-prefix combinations
        for weight, word in enumerate(words):
            # For each suffix, create entries with all possible prefixes
            for i in range(len(word) + 1):
                suffix = word[i:]
                # Use special character to separate suffix and prefix
                key = suffix + "#" + word
                self.trie.insert(key, weight)
    
    def f(self, prefix, suffix):
        """Find word with given prefix and suffix with highest weight"""
        # Search for suffix + "#" + prefix
        search_key = suffix + "#" + prefix
        
        # Find all words with this pattern
        node = self.trie._find_node(search_key)
        if not node:
            return -1
        
        # Find maximum weight among all valid words
        max_weight = -1
        self._find_max_weight(node, max_weight)
        return max_weight
    
    def _find_max_weight(self, node, max_weight):
        """DFS to find maximum weight in subtree"""
        if node.is_end_word:
            max_weight = max(max_weight, node.value)
        
        for child in node.children.values():
            max_weight = max(max_weight, self._find_max_weight(child, max_weight))
        
        return max_weight

def palindromePairs(words):
    """
    LeetCode 336: Palindrome Pairs
    Find pairs of words that form palindromes when concatenated
    """
    def is_palindrome(s):
        return s == s[::-1]
    
    # Build trie of reversed words
    trie = DictionaryTrie()
    for i, word in enumerate(words):
        reversed_word = word[::-1]
        trie.insert(reversed_word, i)  # Store index as value
    
    result = []
    
    for i, word in enumerate(words):
        # Case 1: word + reverse(other_word) is palindrome
        # Look for words whose reverse is a suffix of current word
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]
            
            # Check if prefix is palindrome and suffix exists in trie
            if is_palindrome(prefix):
                node = trie._find_node(suffix)
                if node and node.is_end_word and node.value != i:
                    result.append([node.value, i])
            
            # Check if suffix is palindrome and prefix exists in trie
            if j > 0 and is_palindrome(suffix):
                node = trie._find_node(prefix)
                if node and node.is_end_word and node.value != i:
                    result.append([i, node.value])
    
    return result

def minimumLengthEncoding(words):
    """
    LeetCode 820: Short Encoding of Words
    Find minimum length string that encodes all words as suffixes
    """
    # Build trie of reversed words
    trie = DictionaryTrie()
    word_nodes = {}
    
    # Insert reversed words
    for word in set(words):  # Remove duplicates
        reversed_word = word[::-1]
        trie.insert(reversed_word)
        word_nodes[word] = trie._find_node(reversed_word)
    
    # Calculate encoding length
    total_length = 0
    
    for word, node in word_nodes.items():
        # If node has no children, it's a leaf (word is not suffix of others)
        if len(node.children) == 0:
            total_length += len(word) + 1  # +1 for '#' separator
    
    return total_length

def findAllConcatenatedWordsInADict(words):
    """
    LeetCode 472: Concatenated Words
    Find words that are concatenated from other words in the array
    """
    word_set = set(words)
    memo = {}
    
    def canBreak(word, start=0):
        """Check if word[start:] can be broken into dictionary words"""
        if start == len(word):
            return True
        
        if start in memo:
            return memo[start]
        
        for end in range(start + 1, len(word) + 1):
            prefix = word[start:end]
            # Must use other words (not the word itself) and at least 2 words total
            if (prefix in word_set and prefix != word and 
                canBreak(word, end)):
                memo[start] = True
                return True
        
        memo[start] = False
        return False
    
    result = []
    for word in words:
        memo.clear()
        if len(word) > 0 and canBreak(word):
            result.append(word)
    
    return result

def replaceWords(dictionary, sentence):
    """
    LeetCode 648: Replace Words
    Replace words with their roots from dictionary
    """
    trie = DictionaryTrie()
    
    # Insert all roots
    for root in dictionary:
        trie.insert(root)
    
    def findRoot(word):
        """Find shortest root for word"""
        node = trie.root
        for i, char in enumerate(word):
            if char not in node.children:
                return word  # No root found
            node = node.children[char]
            if node.is_end_word:
                return word[:i + 1]  # Found root
        return word  # No root found
    
    words = sentence.split()
    return ' '.join(findRoot(word) for word in words)

class BitTrie:
    """
    Trie for binary representations (useful for XOR problems)
    """
    
    def __init__(self, max_bits=32):
        self.root = {}
        self.max_bits = max_bits
    
    def insert(self, num):
        """Insert number's binary representation"""
        node = self.root
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]
    
    def find_max_xor(self, num):
        """Find number in trie that gives maximum XOR with num"""
        node = self.root
        max_xor = 0
        
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            # Try to go opposite direction for maximum XOR
            opposite_bit = 1 - bit
            
            if opposite_bit in node:
                max_xor |= (1 << i)
                node = node[opposite_bit]
            elif bit in node:
                node = node[bit]
            else:
                # No valid path
                break
        
        return max_xor

def findMaximumXOR(nums):
    """
    LeetCode 421: Maximum XOR of Two Numbers in an Array
    Find maximum XOR of any two numbers in array
    """
    bit_trie = BitTrie()
    
    # Insert all numbers
    for num in nums:
        bit_trie.insert(num)
    
    max_xor = 0
    # For each number, find the one that gives maximum XOR
    for num in nums:
        max_xor = max(max_xor, bit_trie.find_max_xor(num))
    
    return max_xor

def sumPrefixScores(words):
    """
    LeetCode 2416: Sum of Prefix Scores of Strings
    Calculate sum of prefix scores for each word
    """
    trie = DictionaryTrie()
    
    # Insert all words and count prefixes
    for word in words:
        trie.insert(word)
    
    result = []
    
    for word in words:
        score = 0
        node = trie.root
        
        # Sum scores for all prefixes of this word
        for char in word:
            if char in node.children:
                node = node.children[char]
                score += node.prefix_count
            else:
                break
        
        result.append(score)
    
    return result

class MultiStringTrie:
    """
    Trie optimized for operations on multiple strings
    """
    
    def __init__(self):
        self.root = DictionaryTrieNode()
        self.words = []
    
    def insert_all(self, words):
        """Insert multiple words efficiently"""
        self.words = words
        for word in words:
            self._insert_single(word)
    
    def _insert_single(self, word):
        """Insert single word"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = DictionaryTrieNode()
            node = node.children[char]
            node.prefix_count += 1
        
        node.is_end_word = True
        node.word = word
    
    def get_all_prefixes(self, word):
        """Get all prefixes of word that exist in trie"""
        prefixes = []
        node = self.root
        
        for i, char in enumerate(word):
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_end_word:
                prefixes.append(word[:i + 1])
        
        return prefixes
    
    def longest_common_prefix(self):
        """Find longest common prefix of all words"""
        if not self.words:
            return ""
        
        node = self.root
        prefix = ""
        
        while len(node.children) == 1 and not node.is_end_word:
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]
        
        return prefix
    
    def group_by_prefix(self, prefix_length):
        """Group words by their first prefix_length characters"""
        groups = {}
        
        def collect_words(node, current_prefix, target_length):
            if len(current_prefix) == target_length:
                words_with_prefix = []
                self._collect_all_words(node, current_prefix, words_with_prefix)
                if words_with_prefix:
                    groups[current_prefix] = words_with_prefix
                return
            
            for char, child_node in node.children.items():
                collect_words(child_node, current_prefix + char, target_length)
        
        collect_words(self.root, "", prefix_length)
        return groups
    
    def _collect_all_words(self, node, current_prefix, words):
        """Collect all complete words from current node"""
        if node.is_end_word:
            words.append(current_prefix)
        
        for char, child_node in node.children.items():
            self._collect_all_words(child_node, current_prefix + char, words)

# Template for word validation using trie
class WordValidator:
    """
    Validate words against dictionary using various criteria
    """
    
    def __init__(self, dictionary):
        self.trie = DictionaryTrie()
        for word in dictionary:
            self.trie.insert(word)
    
    def is_valid_word(self, word):
        """Check if word exists in dictionary"""
        return self.trie.search(word)
    
    def has_valid_prefix(self, word):
        """Check if word has any valid prefix in dictionary"""
        node = self.trie.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            if node.is_end_word:
                return True
        return False
    
    def can_be_completed(self, prefix):
        """Check if prefix can be completed to form valid word"""
        return self.trie.startsWith(prefix)
    
    def get_suggestions(self, prefix, max_suggestions=10):
        """Get word suggestions for prefix"""
        prefix_node = self.trie._find_node(prefix)
        if not prefix_node:
            return []
        
        suggestions = []
        self._collect_suggestions(prefix_node, prefix, suggestions, max_suggestions)
        return suggestions[:max_suggestions]
    
    def _collect_suggestions(self, node, current_word, suggestions, max_count):
        """Collect suggestions using DFS"""
        if len(suggestions) >= max_count:
            return
        
        if node.is_end_word:
            suggestions.append(current_word)
        
        for char, child_node in sorted(node.children.items()):
            if len(suggestions) < max_count:
                self._collect_suggestions(child_node, current_word + char, suggestions, max_count)