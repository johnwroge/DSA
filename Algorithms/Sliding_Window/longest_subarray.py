"""
LeetCode 3: Longest Substring Without Repeating Characters
LeetCode 159: Longest Substring with At Most Two Distinct Characters
LeetCode 424: Longest Repeating Character Replacement
"""

def longest_substring(s, k):
    # k is some constraint
    char_count = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Add current character to counter
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink window until our constraint is satisfied
        while not is_valid(char_count, k):
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length