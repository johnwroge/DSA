"""
Longest Common Subsequence (LCS) Template
Applicable LeetCode Problems:
- 1143. Longest Common Subsequence
- 583. Delete Operation for Two Strings  
- 712. Minimum ASCII Delete Sum for Two Strings
- 1092. Shortest Common Supersequence
- 1035. Uncrossed Lines
"""

def lcs_length(text1, text2):
    """
    Returns the length of the longest common subsequence
    Time: O(m*n), Space: O(m*n)
    """
    m, n = len(text1), len(text2)
    
    # dp[i][j] = LCS length of text1[0:i] and text2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def lcs_string(text1, text2):
    """
    Returns the actual LCS string
    Time: O(m*n), Space: O(m*n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct LCS
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            result.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(result))

def lcs_space_optimized(text1, text2):
    """
    Space optimized version - only stores current and previous row
    Time: O(m*n), Space: O(min(m,n))
    """
    # Make text1 the shorter string for space optimization
    if len(text1) > len(text2):
        text1, text2 = text2, text1
    
    m, n = len(text1), len(text2)
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)
    
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if text1[i-1] == text2[j-1]:
                curr[i] = prev[i-1] + 1
            else:
                curr[i] = max(prev[i], curr[i-1])
        prev, curr = curr, prev
    
    return prev[m]

