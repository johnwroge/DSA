"""
Edit Distance (Levenshtein Distance) Template
Applicable LeetCode Problems:
- 72. Edit Distance
- 161. One Edit Distance
- 583. Delete Operation for Two Strings
- 712. Minimum ASCII Delete Sum for Two Strings
- 44. Wildcard Matching (variant)
- 10. Regular Expression Matching (variant)
- 97. Interleaving String (variant)
"""

def edit_distance(word1, word2):
    """
    Classic Edit Distance - minimum operations to convert word1 to word2
    Operations: insert, delete, replace
    Time: O(m*n), Space: O(m*n)
    """
    m, n = len(word1), len(word2)
    
    # dp[i][j] = min operations to convert word1[0:i] to word2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters from word1
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters to get word2
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete from word1
                    dp[i][j-1],    # Insert into word1
                    dp[i-1][j-1]   # Replace in word1
                )
    
    return dp[m][n]

def edit_distance_with_path(word1, word2):
    """
    Returns both the minimum edit distance and the sequence of operations
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    # Reconstruct path
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i-1] == word2[j-1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
            operations.append(f"Replace '{word1[i-1]}' with '{word2[j-1]}'")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            operations.append(f"Delete '{word1[i-1]}'")
            i -= 1
        else:
            operations.append(f"Insert '{word2[j-1]}'")
            j -= 1
    
    return dp[m][n], list(reversed(operations))

def edit_distance_space_optimized(word1, word2):
    """
    Space optimized version - only stores current and previous row
    Time: O(m*n), Space: O(min(m,n))
    """
    # Make word1 the shorter string for space optimization
    if len(word1) > len(word2):
        word1, word2 = word2, word1
    
    m, n = len(word1), len(word2)
    prev = list(range(m + 1))
    curr = [0] * (m + 1)
    
    for j in range(1, n + 1):
        curr[0] = j
        for i in range(1, m + 1):
            if word1[i-1] == word2[j-1]:
                curr[i] = prev[i-1]
            else:
                curr[i] = 1 + min(prev[i], curr[i-1], prev[i-1])
        prev, curr = curr, prev
    
    return prev[m]

def delete_operations_only(word1, word2):
    """
    Variation: Only delete operations allowed (LeetCode 583)
    Convert to LCS problem: deletions = len(word1) + len(word2) - 2*LCS
    """
    def lcs_length(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    lcs_len = lcs_length(word1, word2)
    return len(word1) + len(word2) - 2 * lcs_len

def is_one_edit_distance(s, t):
    """
    Check if strings are exactly one edit distance apart (LeetCode 161)
    """
    m, n = len(s), len(t)
    
    # Ensure s is the shorter string
    if m > n:
        return is_one_edit_distance(t, s)
    
    # Length difference > 1
    if n - m > 1:
        return False
    
    for i in range(m):
        if s[i] != t[i]:
            if m == n:
                return s[i+1:] == t[i+1:]  # Replace
            else:
                return s[i:] == t[i+1:]    # Insert
    
    return n - m == 1  # Insert at end

