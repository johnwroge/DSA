"""
LeetCode Problems where Z-Algorithm can be applied:

28. Find the Index of the First Occurrence in a String
214. Shortest Palindrome
459. Repeated Substring Pattern
686. Repeated String Match
796. Rotate String
1392. Longest Happy Prefix
1566. Detect Pattern of Length M Repeated K or More Times
1668. Maximum Repeating Substring
3008. Find Beautiful Indices in the Given Array II
"""

def z_algorithm(s):
    """
    Z-Algorithm: Compute Z-array for string s
    
    Z[i] = length of longest substring starting from s[i] 
           which is also a prefix of s
    
    Time: O(n), Space: O(n)
    """
    n = len(s)
    if n == 0:
        return []
    
    z = [0] * n
    z[0] = n  # By definition, entire string matches with itself
    
    left = right = 0  # Window [left, right] of rightmost match
    
    for i in range(1, n):
        if i <= right:
            # We're inside a previous match window
            # z[i - left] is the Z-value for corresponding position
            z[i] = min(right - i + 1, z[i - left])
        
        # Try to extend the match
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        # Update the window if we found a match extending further right
        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1
    
    return z

def z_search(text, pattern):
    """
    Use Z-algorithm for pattern matching
    Find all occurrences of pattern in text
    
    Time: O(n + m), Space: O(n + m)
    """
    if not pattern:
        return [0]
    
    # Create combined string: pattern + "$" + text
    # "$" is a separator that doesn't appear in pattern or text
    combined = pattern + "$" + text
    z = z_algorithm(combined)
    
    matches = []
    pattern_len = len(pattern)
    
    # Check Z-values starting from position len(pattern) + 1
    for i in range(pattern_len + 1, len(combined)):
        if z[i] == pattern_len:
            # Found a match at position i - pattern_len - 1 in original text
            matches.append(i - pattern_len - 1)
    
    return matches

def z_search_first(text, pattern):
    """
    Find first occurrence of pattern in text using Z-algorithm
    """
    matches = z_search(text, pattern)
    return matches[0] if matches else -1

def strStr(haystack, needle):
    """
    LeetCode 28: Find the Index of the First Occurrence in a String
    """
    return z_search_first(haystack, needle)

def shortestPalindrome(s):
    """
    LeetCode 214: Shortest Palindrome
    Find shortest palindrome by adding characters to the front
    """
    if not s:
        return ""
    
    # Use Z-algorithm on s + "#" + reverse(s)
    rev_s = s[::-1]
    combined = s + "#" + rev_s
    z = z_algorithm(combined)
    
    # Find longest prefix of s that matches suffix of reverse(s)
    max_overlap = 0
    n = len(s)
    
    for i in range(n + 1, len(combined)):
        # Check if this Z-value represents a suffix that reaches the end
        if i + z[i] == len(combined):
            max_overlap = z[i]
    
    # Add the non-overlapping part of reverse to the front
    return rev_s[:n - max_overlap] + s

def repeatedSubstringPattern(s):
    """
    LeetCode 459: Repeated Substring Pattern
    Check if string can be constructed by repeating a substring
    """
    n = len(s)
    z = z_algorithm(s)
    
    # Check all possible period lengths
    for period in range(1, n):
        if n % period == 0:  # Period must divide string length
            # Check if period repeats throughout the string
            valid = True
            for i in range(period, n, period):
                if z[i] < period:
                    valid = False
                    break
            if valid:
                return True
    
    return False

def longestPrefix(s):
    """
    LeetCode 1392: Longest Happy Prefix
    Find longest prefix that is also suffix (excluding the string itself)
    """
    z = z_algorithm(s)
    n = len(s)
    
    # Find longest Z-value where i + z[i] == n (reaches the end)
    max_length = 0
    for i in range(1, n):
        if i + z[i] == n:
            max_length = max(max_length, z[i])
    
    return s[:max_length]

def rotateString(s, goal):
    """
    LeetCode 796: Rotate String
    Check if s can be rotated to become goal
    """
    if len(s) != len(goal):
        return False
    
    # Check if goal appears in s + s using Z-algorithm
    return z_search_first(s + s, goal) != -1

def maxRepeating(sequence, word):
    """
    LeetCode 1668: Maximum Repeating Substring
    Find maximum k such that word repeated k times is substring of sequence
    """
    max_k = 0
    k = 1
    
    while k * len(word) <= len(sequence):
        repeated_word = word * k
        if z_search_first(sequence, repeated_word) != -1:
            max_k = k
        k += 1
    
    return max_k

def hasPattern(arr, m, k):
    """
    LeetCode 1566: Detect Pattern of Length M Repeated K or More Times
    Check if array has pattern of length m repeated k or more times consecutively
    """
    if len(arr) < m * k:
        return False
    
    # Convert array to string for Z-algorithm
    s = ''.join(map(str, arr))
    
    # Check each possible starting position
    for start in range(len(s) - m * k + 1):
        pattern = s[start:start + m]
        
        # Use Z-algorithm to check consecutive repetitions
        test_string = s[start:]
        z = z_algorithm(test_string)
        
        consecutive_matches = 1
        pos = m
        
        while pos < len(test_string) and z[pos] >= m:
            consecutive_matches += 1
            if consecutive_matches >= k:
                return True
            pos += m
    
    return False

def find_all_periods(s):
    """
    Find all periods of string using Z-algorithm
    
    A period p means s[i] == s[i + p] for all valid i
    """
    n = len(s)
    z = z_algorithm(s)
    periods = []
    
    # Check each possible period length
    for p in range(1, n):
        is_period = True
        
        # Check if p is a valid period using Z-array
        for i in range(p, n, p):
            if z[i] < min(p, n - i):
                is_period = False
                break
        
        if is_period:
            periods.append(p)
    
    return periods

def count_distinct_substrings_z(s):
    """
    Count distinct substrings using Z-algorithm approach
    
    For each suffix, count how many distinct prefixes it has
    """
    n = len(s)
    total = 0
    
    for i in range(n):
        suffix = s[i:]
        z = z_algorithm(suffix)
        
        # Count distinct prefixes of this suffix
        distinct_prefixes = set()
        for j in range(len(suffix)):
            prefix = suffix[:j+1]
            distinct_prefixes.add(prefix)
        
        # This approach is O(n^3), better to use suffix array for this
        
    # Better approach: count using Z-algorithm properties
    all_substrings = set()
    for i in range(n):
        for j in range(i, n):
            all_substrings.add(s[i:j+1])
    
    return len(all_substrings)

def longest_common_prefix_array(strings):
    """
    Find longest common prefix array using Z-algorithm
    """
    if not strings:
        return []
    
    result = []
    first = strings[0]
    
    for s in strings:
        # Find LCP between first string and current string
        combined = first + "$" + s
        z = z_algorithm(combined)
        
        # Find longest Z-value in the second part
        lcp_length = 0
        for i in range(len(first) + 1, len(combined)):
            if z[i] > lcp_length:
                lcp_length = z[i]
        
        result.append(first[:lcp_length])
    
    return result

def find_borders(s):
    """
    Find all borders of string using Z-algorithm
    
    A border is a string that is both prefix and suffix
    """
    z = z_algorithm(s)
    n = len(s)
    borders = []
    
    # Check all positions where Z-value + position equals string length
    for i in range(1, n):
        if i + z[i] == n:
            borders.append(s[:z[i]])
    
    return borders

def z_algorithm_2d(matrix):
    """
    2D version of Z-algorithm for 2D pattern matching
    
    For each row, compute Z-array, then extend to 2D
    """
    if not matrix or not matrix[0]:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    result = []
    
    for i in range(rows):
        # Convert row to string and compute Z-array
        row_string = ''.join(matrix[i])
        z_row = z_algorithm(row_string)
        result.append(z_row)
    
    return result

def beautiful_indices(s, a, b, k):
    """
    LeetCode 3008: Find Beautiful Indices in the Given Array II
    Find beautiful indices using Z-algorithm for efficient pattern matching
    """
    # Find all occurrences of pattern 'a'
    a_matches = z_search(s, a)
    
    # Find all occurrences of pattern 'b'  
    b_matches = z_search(s, b)
    
    beautiful = []
    
    # For each occurrence of 'a', check if there's a 'b' within distance k
    for i in a_matches:
        for j in b_matches:
            if abs(i - j) <= k:
                beautiful.append(i)
                break
    
    return sorted(beautiful)

# Template for suffix and prefix matching
def suffix_prefix_match(s1, s2):
    """
    Find longest suffix of s1 that matches prefix of s2
    """
    combined = s2 + "$" + s1
    z = z_algorithm(combined)
    
    max_match = 0
    s2_len = len(s2)
    
    for i in range(s2_len + 1, len(combined)):
        # Check if this Z-value represents a suffix match
        pos_in_s1 = i - s2_len - 1
        if pos_in_s1 + z[i] == len(s1):
            max_match = max(max_match, z[i])
    
    return max_match

# Template for palindrome detection using Z-algorithm
def is_palindrome_z(s):
    """
    Check if string is palindrome using Z-algorithm
    """
    rev_s = s[::-1]
    combined = s + "$" + rev_s
    z = z_algorithm(combined)
    
    n = len(s)
    # Check if there's a Z-value of n at position n+1
    return len(z) > n and z[n + 1] == n

def manacher_using_z(s):
    """
    Find all palindromic substrings using Z-algorithm approach
    """
    # This is more complex and typically Manacher's algorithm is preferred
    # But we can use Z-algorithm for specific palindrome problems
    
    palindromes = []
    n = len(s)
    
    # Check all possible centers (including between characters)
    for center in range(2 * n - 1):
        if center % 2 == 0:
            # Odd length palindrome
            i = center // 2
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                palindromes.append(s[left:right+1])
                left -= 1
                right += 1
        else:
            # Even length palindrome
            i = center // 2
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                palindromes.append(s[left:right+1])
                left -= 1
                right += 1
    
    return list(set(palindromes))  # Remove duplicates