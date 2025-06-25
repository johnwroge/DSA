"""
Huffman Coding Algorithm Templates
Applicable LeetCode Problems:
- 1167. Minimum Cost to Connect Sticks
- 215. Kth Largest Element in an Array (heap usage)
- 347. Top K Frequent Elements
- 703. Kth Largest Element in a Stream
- 1046. Last Stone Weight
"""

import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    """Node for Huffman tree"""
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    """
    Build Huffman tree from text
    Time: O(n log n), Space: O(n)
    """
    if not text:
        return None
    
    # Count character frequencies
    freq_map = Counter(text)
    
    # Special case: single character
    if len(freq_map) == 1:
        char = list(freq_map.keys())[0]
        root = HuffmanNode(freq=freq_map[char])
        root.left = HuffmanNode(char=char, freq=freq_map[char])
        return root
    
    # Create min heap with leaf nodes
    heap = [HuffmanNode(char=char, freq=freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)
    
    # Build tree bottom-up
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        internal = HuffmanNode(
            freq=left.freq + right.freq,
            left=left,
            right=right
        )
        
        heapq.heappush(heap, internal)
    
    return heap[0]

def generate_huffman_codes(root):
    """
    Generate Huffman codes from tree
    Returns: dict mapping character to binary code
    """
    if not root:
        return {}
    
    codes = {}
    
    def dfs(node, code):
        if node.char is not None:  # Leaf node
            codes[node.char] = code if code else "0"  # Handle single char case
            return
        
        if node.left:
            dfs(node.left, code + "0")
        if node.right:
            dfs(node.right, code + "1")
    
    dfs(root, "")
    return codes

def huffman_encode(text):
    """
    Encode text using Huffman coding
    Returns: (encoded_text, huffman_tree, codes)
    """
    if not text:
        return "", None, {}
    
    # Build tree and generate codes
    tree = build_huffman_tree(text)
    codes = generate_huffman_codes(tree)
    
    # Encode text
    encoded = "".join(codes[char] for char in text)
    
    return encoded, tree, codes

def huffman_decode(encoded_text, tree):
    """
    Decode Huffman encoded text
    Time: O(n), Space: O(1) extra
    """
    if not encoded_text or not tree:
        return ""
    
    decoded = []
    current = tree
    
    for bit in encoded_text:
        # Traverse tree based on bit
        if bit == "0":
            current = current.left
        else:
            current = current.right
        
        # If leaf node, add character and reset
        if current.char is not None:
            decoded.append(current.char)
            current = tree
    
    return "".join(decoded)

def calculate_compression_ratio(original_text, encoded_text):
    """
    Calculate compression ratio
    """
    original_bits = len(original_text) * 8  # Assuming 8 bits per character
    compressed_bits = len(encoded_text)
    
    if original_bits == 0:
        return 0
    
    return (original_bits - compressed_bits) / original_bits

def huffman_with_frequency_map(freq_map):
    """
    Build Huffman tree from frequency map
    Useful when you already have character frequencies
    """
    if not freq_map:
        return None, {}
    
    if len(freq_map) == 1:
        char = list(freq_map.keys())[0]
        root = HuffmanNode(freq=freq_map[char])
        root.left = HuffmanNode(char=char, freq=freq_map[char])
        return root, {char: "0"}
    
    heap = [HuffmanNode(char=char, freq=freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        internal = HuffmanNode(
            freq=left.freq + right.freq,
            left=left,
            right=right
        )
        
        heapq.heappush(heap, internal)
    
    tree = heap[0]
    codes = generate_huffman_codes(tree)
    
    return tree, codes

def min_cost_connect_sticks(sticks):
    """
    LeetCode 1167: Minimum Cost to Connect Sticks
    Similar to Huffman coding - always combine two smallest
    """
    if len(sticks) <= 1:
        return 0
    
    heapq.heapify(sticks)
    total_cost = 0
    
    while len(sticks) > 1:
        first = heapq.heappop(sticks)
        second = heapq.heappop(sticks)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(sticks, cost)
    
    return total_cost

def last_stone_weight(stones):
    """
    LeetCode 1046: Last Stone Weight
    Uses max heap (simulated with negative values)
    """
    if not stones:
        return 0
    
    # Python heapq is min heap, so use negative values for max heap
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)
    
    while len(max_heap) > 1:
        first = -heapq.heappop(max_heap)   # Heaviest
        second = -heapq.heappop(max_heap)  # Second heaviest
        
        if first != second:
            heapq.heappush(max_heap, -(first - second))
    
    return -max_heap[0] if max_heap else 0

def optimal_merge_pattern(files):
    """
    Optimal merge pattern - merge files with minimum cost
    Cost of merging two files = sum of their sizes
    """
    if len(files) <= 1:
        return 0
    
    heapq.heapify(files)
    total_cost = 0
    
    while len(files) > 1:
        first = heapq.heappop(files)
        second = heapq.heappop(files)
        
        merge_cost = first + second
        total_cost += merge_cost
        
        heapq.heappush(files, merge_cost)
    
    return total_cost

def huffman_tree_height(root):
    """
    Calculate height of Huffman tree
    """
    if not root:
        return 0
    
    if root.char is not None:  # Leaf node
        return 0
    
    left_height = huffman_tree_height(root.left) if root.left else 0
    right_height = huffman_tree_height(root.right) if root.right else 0
    
    return 1 + max(left_height, right_height)

def average_code_length(codes, freq_map):
    """
    Calculate average code length for Huffman coding
    """
    if not codes or not freq_map:
        return 0
    
    total_chars = sum(freq_map.values())
    weighted_length = sum(len(codes[char]) * freq for char, freq in freq_map.items())
    
    return weighted_length / total_chars

def is_valid_huffman_code(codes):
    """
    Check if given codes form a valid Huffman code (prefix property)
    """
    if not codes:
        return True
    
    code_list = list(codes.values())
    
    # Check prefix property
    for i in range(len(code_list)):
        for j in range(len(code_list)):
            if i != j and code_list[i].startswith(code_list[j]):
                return False
    
    return True