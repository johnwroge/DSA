"""
LeetCode 28: Find the Index of the First Occurrence in a String (KMP algorithm is often preferred but sliding window can work)
LeetCode 30: Substring with Concatenation of All Words
"""

def string_pattern_matching(s, pattern):
    m, n = len(pattern), len(s)
    if m > n:
        return []
    
    # Build pattern frequency map
    pattern_count = {}
    for ch in pattern:
        pattern_count[ch] = pattern_count.get(ch, 0) + 1
    
    # Number of distinct characters in pattern
    required_chars = len(pattern_count)
    
    # Window variables
    window_count = {}
    formed = 0  # Number of characters matched with correct frequency
    result = []
    
    left = right = 0
    
    while right < n:
        # Add character to window
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Check if this character matches required frequency
        if char in pattern_count and window_count[char] == pattern_count[char]:
            formed += 1
        
        # Try to minimize window
        while left <= right and formed == required_chars:
            # Check if window size matches pattern size
            if right - left + 1 == m:
                result.append(left)
            
            # Remove leftmost character
            char = s[left]
            window_count[char] -= 1
            
            # If this affects a required character
            if char in pattern_count and window_count[char] < pattern_count[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return result