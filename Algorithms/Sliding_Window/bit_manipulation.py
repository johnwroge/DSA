"""
LeetCode 1461: Check If a String Contains All Binary Codes of Size K
LeetCode 1310: XOR Queries of a Subarray 
"""

def sliding_window_with_bits(s, k):
    n = len(s)
    # Total possible patterns of length k (for binary string)
    total_patterns = 1 << k
    # Set to store encountered patterns
    patterns_seen = set()
    
    # Check if all patterns exist
    for i in range(n - k + 1):
        # Extract current pattern and convert to integer
        current_pattern = 0
        for j in range(k):
            bit = int(s[i + j])
            current_pattern = (current_pattern << 1) | bit
        
        patterns_seen.add(current_pattern)
    
    # Check if all possible patterns were found
    return len(patterns_seen) == total_patterns