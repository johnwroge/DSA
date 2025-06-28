"""
LeetCode Problems where KMP Algorithm can be applied:

28. Find the Index of the First Occurrence in a String
214. Shortest Palindrome
459. Repeated Substring Pattern
686. Repeated String Match
796. Rotate String
1392. Longest Happy Prefix
1566. Detect Pattern of Length M Repeated K or More Times
1668. Maximum Repeating Substring
2337. Move Pieces to Obtain a String
"""

def compute_lps(pattern):
    """
    Compute Longest Proper Prefix which is also Suffix (LPS) array
    Also known as failure function or partial match table
    
    Time: O(m), Space: O(m) where m = len(pattern)
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Don't increment i here
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    KMP pattern matching algorithm
    Find all occurrences of pattern in text
    
    Time: O(n + m), Space: O(m)
    where n = len(text), m = len(pattern)
    """
    if not pattern:
        return [0]  # Empty pattern matches at position 0
    
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    
    matches = []
    i = j = 0  # i for text, j for pattern
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            # Found a match
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches

def kmp_search_first(text, pattern):
    """
    Find first occurrence of pattern in text
    Returns index of first match, or -1 if not found
    """
    if not pattern:
        return 0
    
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            return i - j
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1

def strStr(haystack, needle):
    """
    LeetCode 28: Find the Index of the First Occurrence in a String
    """
    return kmp_search_first(haystack, needle)

def shortestPalindrome(s):
    """
    LeetCode 214: Shortest Palindrome
    Find shortest palindrome by adding characters to the front
    """
    if not s:
        return ""
    
    # Create string: s + "#" + reverse(s)
    # Find longest prefix of s that matches suffix of reverse(s)
    rev_s = s[::-1]
    combined = s + "#" + rev_s
    
    # Compute LPS array
    lps = compute_lps(combined)
    
    # LPS[-1] gives length of longest prefix that is also suffix
    # This tells us how much of s is already a palindrome from the start
    palindrome_length = lps[-1]
    
    # Add the remaining characters from reverse to the front
    return rev_s[:len(s) - palindrome_length] + s

def repeatedSubstringPattern(s):
    """
    LeetCode 459: Repeated Substring Pattern
    Check if string can be constructed by repeating a substring
    """
    n = len(s)
    lps = compute_lps(s)
    
    # If LPS[n-1] > 0 and n % (n - LPS[n-1]) == 0,
    # then string is made of repeating pattern
    last_lps = lps[n - 1]
    pattern_length = n - last_lps
    
    return last_lps > 0 and n % pattern_length == 0

def rotateString(s, goal):
    """
    LeetCode 796: Rotate String
    Check if s can be rotated to become goal
    """
    if len(s) != len(goal):
        return False
    
    # If goal is a rotation of s, then goal appears in s + s
    return kmp_search_first(s + s, goal) != -1

def longestPrefix(s):
    """
    LeetCode 1392: Longest Happy Prefix
    Find longest prefix that is also suffix (excluding the string itself)
    """
    lps = compute_lps(s)
    return s[:lps[-1]]

def repeatedStringMatch(a, b):
    """
    LeetCode 686: Repeated String Match
    Find minimum repetitions of a such that b is a substring
    """
    # Calculate minimum and maximum possible repetitions
    min_reps = (len(b) - 1) // len(a) + 1
    max_reps = min_reps + 1
    
    # Check min_reps repetitions
    repeated = a * min_reps
    if kmp_search_first(repeated, b) != -1:
        return min_reps
    
    # Check max_reps repetitions
    repeated = a * max_reps
    if kmp_search_first(repeated, b) != -1:
        return max_reps
    
    return -1

def hasPattern(arr, m, k):
    """
    LeetCode 1566: Detect Pattern of Length M Repeated K or More Times
    Check if array has pattern of length m repeated k or more times consecutively
    """
    if len(arr) < m * k:
        return False
    
    # Convert to string for pattern matching
    s = ''.join(map(str, arr))
    pattern = s[:m]
    
    # Use KMP to find consecutive occurrences
    matches = kmp_search(s, pattern)
    
    # Check for k consecutive matches starting at same position
    for start in matches:
        consecutive = 1
        pos = start + m
        
        while pos in matches and consecutive < k:
            consecutive += 1
            pos += m
        
        if consecutive >= k:
            return True
    
    return False

def maxRepeating(sequence, word):
    """
    LeetCode 1668: Maximum Repeating Substring
    Find maximum k such that word repeated k times is substring of sequence
    """
    max_k = 0
    k = 1
    
    while k * len(word) <= len(sequence):
        repeated_word = word * k
        if kmp_search_first(sequence, repeated_word) != -1:
            max_k = k
        k += 1
    
    return max_k

def build_failure_function_2d(pattern):
    """
    Build failure function for 2D pattern (for 2D KMP)
    """
    rows, cols = len(pattern), len(pattern[0])
    failure = {}
    
    for i in range(rows):
        row_pattern = ''.join(pattern[i])
        failure[i] = compute_lps(row_pattern)
    
    return failure

def kmp_2d_search(text, pattern):
    """
    2D KMP for finding 2D patterns in 2D text
    """
    if not text or not pattern or not text[0] or not pattern[0]:
        return []
    
    text_rows, text_cols = len(text), len(text[0])
    pat_rows, pat_cols = len(pattern), len(pattern[0])
    
    matches = []
    
    # For each row in text, find potential starting positions
    for start_row in range(text_rows - pat_rows + 1):
        # Check if pattern can start at this row
        row_matches = kmp_search(text[start_row], pattern[0])
        
        for col_start in row_matches:
            # Check if full 2D pattern matches starting here
            match = True
            for r in range(pat_rows):
                if col_start + pat_cols > text_cols:
                    match = False
                    break
                
                text_substr = text[start_row + r][col_start:col_start + pat_cols]
                if text_substr != pattern[r]:
                    match = False
                    break
            
            if match:
                matches.append((start_row, col_start))
    
    return matches

# Template for string matching with preprocessing
def string_match_with_preprocess(text, patterns):
    """
    Efficiently match multiple patterns using KMP
    
    Args:
        text: input text
        patterns: list of patterns to search for
    
    Returns:
        dict mapping pattern to list of match positions
    """
    results = {}
    
    for pattern in patterns:
        results[pattern] = kmp_search(text, pattern)
    
    return results

# Template for palindrome problems using KMP
def longest_palindromic_prefix(s):
    """
    Find longest palindromic prefix using KMP technique
    """
    # Use KMP on s + "#" + reverse(s)
    rev_s = s[::-1]
    combined = s + "#" + rev_s
    lps = compute_lps(combined)
    
    # Length of longest palindromic prefix
    return lps[-1]

def count_palindromic_substrings_kmp(s):
    """
    Count palindromic substrings using KMP approach
    """
    count = 0
    n = len(s)
    
    # Check each substring for being palindrome using KMP
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            # Check if substr is palindrome using KMP
            rev_substr = substr[::-1]
            if substr == rev_substr:
                count += 1
    
    return count

# Template for period and repetition problems
def find_all_periods(s):
    """
    Find all periods of string using KMP LPS array
    """
    n = len(s)
    lps = compute_lps(s)
    periods = []
    
    # Trace back through LPS array to find all periods
    length = lps[n - 1]
    while length > 0:
        period = n - length
        periods.append(period)
        length = lps[length - 1]
    
    # The string itself is always a period
    periods.append(n)
    
    return sorted(periods)