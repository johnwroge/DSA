"""
LeetCode Problems where Suffix Array can be applied:

28. Find the Index of the First Occurrence in a String
208. Implement Trie (Prefix Tree)
336. Palindrome Pairs
718. Maximum Length of Repeated Subarray
1044. Longest Duplicate Substring
1062. Longest Repeating Substring
1316. Distinct Echo Substrings
1392. Longest Happy Prefix
1698. Number of Distinct Substrings in a String
1923. Longest Common Subpath
2261. K Divisible Elements Subarrays
"""

def build_suffix_array_naive(s):
    """
    Build suffix array using naive O(n^2 log n) approach
    Good for understanding, but not efficient for large strings
    
    Returns: list of starting indices of sorted suffixes
    """
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()
    return [idx for _, idx in suffixes]

def build_suffix_array_optimized(s):
    """
    Build suffix array using O(n log^2 n) approach with radix sort
    More efficient than naive approach
    """
    n = len(s)
    if n == 0:
        return []
    
    # Create initial order based on single characters
    order = list(range(n))
    order.sort(key=lambda i: s[i])
    
    # Create equivalence classes
    equivalence = [0] * n
    for i in range(1, n):
        equivalence[order[i]] = equivalence[order[i-1]]
        if s[order[i]] != s[order[i-1]]:
            equivalence[order[i]] += 1
    
    # Double the length in each iteration
    length = 1
    while length < n:
        # Sort by (equivalence[i], equivalence[i + length])
        order.sort(key=lambda i: (equivalence[i], equivalence[(i + length) % n]))
        
        # Update equivalence classes
        new_equivalence = [0] * n
        for i in range(1, n):
            new_equivalence[order[i]] = new_equivalence[order[i-1]]
            if (equivalence[order[i]], equivalence[(order[i] + length) % n]) != \
               (equivalence[order[i-1]], equivalence[(order[i-1] + length) % n]):
                new_equivalence[order[i]] += 1
        
        equivalence = new_equivalence
        length *= 2
    
    return order

def build_lcp_array(s, suffix_array):
    """
    Build Longest Common Prefix (LCP) array from suffix array
    
    LCP[i] = length of longest common prefix between
             suffixes at positions suffix_array[i] and suffix_array[i+1]
    
    Time: O(n), Space: O(n)
    """
    n = len(s)
    if n <= 1:
        return []
    
    # Build rank array (inverse of suffix array)
    rank = [0] * n
    for i in range(n):
        rank[suffix_array[i]] = i
    
    lcp = [0] * (n - 1)
    current_lcp = 0
    
    for i in range(n):
        if rank[i] == n - 1:
            current_lcp = 0
            continue
        
        # Find next suffix in sorted order
        j = suffix_array[rank[i] + 1]
        
        # Compute LCP between suffixes starting at i and j
        while (i + current_lcp < n and j + current_lcp < n and 
               s[i + current_lcp] == s[j + current_lcp]):
            current_lcp += 1
        
        lcp[rank[i]] = current_lcp
        
        # Decrease current_lcp by 1 for next iteration (optimization)
        if current_lcp > 0:
            current_lcp -= 1
    
    return lcp

class SuffixArray:
    """
    Complete Suffix Array data structure with LCP array
    Supports efficient substring queries
    """
    
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.suffix_array = build_suffix_array_optimized(s)
        self.lcp_array = build_lcp_array(s, self.suffix_array)
        
        # Build rank array for quick lookups
        self.rank = [0] * self.n
        for i in range(self.n):
            self.rank[self.suffix_array[i]] = i
    
    def pattern_search(self, pattern):
        """
        Find all occurrences of pattern using binary search on suffix array
        
        Time: O(m log n + k) where m = len(pattern), k = number of matches
        """
        if not pattern:
            return list(range(self.n))
        
        # Binary search for leftmost occurrence
        left = self._binary_search_left(pattern)
        if left == -1:
            return []
        
        # Binary search for rightmost occurrence
        right = self._binary_search_right(pattern)
        
        # Return all positions between left and right
        return [self.suffix_array[i] for i in range(left, right + 1)]
    
    def _binary_search_left(self, pattern):
        """Find leftmost position where pattern could be inserted"""
        left, right = 0, self.n - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            suffix_start = self.suffix_array[mid]
            suffix = self.s[suffix_start:]
            
            if suffix.startswith(pattern):
                result = mid
                right = mid - 1  # Look for earlier occurrence
            elif suffix < pattern:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    def _binary_search_right(self, pattern):
        """Find rightmost position where pattern occurs"""
        left, right = 0, self.n - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            suffix_start = self.suffix_array[mid]
            suffix = self.s[suffix_start:]
            
            if suffix.startswith(pattern):
                result = mid
                left = mid + 1  # Look for later occurrence
            elif suffix < pattern:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    def longest_repeated_substring(self):
        """Find longest repeated substring using LCP array"""
        if not self.lcp_array:
            return ""
        
        max_lcp = max(self.lcp_array)
        if max_lcp == 0:
            return ""
        
        # Find position with maximum LCP
        max_pos = self.lcp_array.index(max_lcp)
        start_pos = self.suffix_array[max_pos]
        
        return self.s[start_pos:start_pos + max_lcp]
    
    def count_distinct_substrings(self):
        """Count number of distinct substrings"""
        total_substrings = self.n * (self.n + 1) // 2
        
        # Subtract repeated substrings using LCP array
        repeated = sum(self.lcp_array)
        
        return total_substrings - repeated
    
    def k_th_substring(self, k):
        """Find k-th lexicographically smallest substring"""
        count = 0
        
        for i in range(self.n):
            suffix_start = self.suffix_array[i]
            # Number of substrings starting from this suffix
            available = self.n - suffix_start
            
            if i > 0:
                # Subtract substrings that are common with previous suffix
                available -= self.lcp_array[i - 1]
            
            if count + available >= k:
                # k-th substring is in this suffix
                pos_in_suffix = k - count - 1
                if i > 0:
                    pos_in_suffix += self.lcp_array[i - 1]
                
                return self.s[suffix_start:suffix_start + pos_in_suffix + 1]
            
            count += available
        
        return ""

def longestDupSubstring(s):
    """
    LeetCode 1044: Longest Duplicate Substring
    Find longest duplicate substring using suffix array
    """
    if not s:
        return ""
    
    sa = SuffixArray(s)
    return sa.longest_repeated_substring()

def numDistinct(s):
    """
    LeetCode 1698: Number of Distinct Substrings in a String
    Count distinct substrings using suffix array
    """
    sa = SuffixArray(s)
    return sa.count_distinct_substrings()

def longestRepeatingSubstring(s):
    """
    LeetCode 1062: Longest Repeating Substring
    Find length of longest repeating substring
    """
    sa = SuffixArray(s)
    longest = sa.longest_repeated_substring()
    return len(longest)

def findLength(nums1, nums2):
    """
    LeetCode 718: Maximum Length of Repeated Subarray
    Find longest common subarray using generalized suffix array
    """
    # Convert to strings with separator
    s1 = ''.join(map(str, nums1))
    s2 = ''.join(map(str, nums2))
    
    # Create combined string with unique separator
    separator = chr(max(ord(c) for c in s1 + s2) + 1) if s1 + s2 else '#'
    combined = s1 + separator + s2
    
    sa = SuffixArray(combined)
    
    # Find maximum LCP between suffixes from different strings
    max_length = 0
    s1_len = len(s1)
    
    for i in range(len(sa.lcp_array)):
        pos1 = sa.suffix_array[i]
        pos2 = sa.suffix_array[i + 1]
        
        # Check if suffixes come from different original strings
        if (pos1 <= s1_len and pos2 > s1_len) or (pos1 > s1_len and pos2 <= s1_len):
            max_length = max(max_length, sa.lcp_array[i])
    
    return max_length

class GeneralizedSuffixArray:
    """
    Suffix array for multiple strings
    Useful for finding common substrings among multiple strings
    """
    
    def __init__(self, strings):
        self.strings = strings
        self.string_ids = []
        self.positions = []
        
        # Create combined string with unique separators
        combined = ""
        current_pos = 0
        
        for string_id, s in enumerate(strings):
            for pos, char in enumerate(s):
                combined += char
                self.string_ids.append(string_id)
                self.positions.append(pos)
            
            # Add unique separator
            if string_id < len(strings) - 1:
                separator = chr(1000 + string_id)  # Unique separator
                combined += separator
                self.string_ids.append(-1)  # Mark as separator
                self.positions.append(-1)
        
        self.combined = combined
        self.sa = SuffixArray(combined)
    
    def longest_common_substring(self):
        """Find longest substring common to all input strings"""
        num_strings = len(self.strings)
        max_length = 0
        result = ""
        
        # Use sliding window on LCP array
        for i in range(len(self.sa.lcp_array)):
            min_lcp = float('inf')
            strings_seen = set()
            
            # Extend window to include suffixes from all strings
            for j in range(i, len(self.sa.suffix_array)):
                suffix_pos = self.sa.suffix_array[j]
                
                if suffix_pos < len(self.string_ids):
                    string_id = self.string_ids[suffix_pos]
                    
                    if string_id != -1:  # Not a separator
                        strings_seen.add(string_id)
                        
                        # Update minimum LCP in current window
                        if j > i:
                            min_lcp = min(min_lcp, self.sa.lcp_array[j - 1])
                        
                        # Check if we have suffixes from all strings
                        if len(strings_seen) == num_strings and min_lcp > max_length:
                            max_length = min_lcp
                            start_pos = self.sa.suffix_array[i]
                            result = self.combined[start_pos:start_pos + max_length]
        
        return result

def palindromePairs(words):
    """
    LeetCode 336: Palindrome Pairs
    Find pairs of words that form palindromes using suffix array concepts
    """
    def is_palindrome(s):
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    # For each pair of words, check if concatenation forms palindrome
    for i in range(n):
        for j in range(n):
            if i != j:
                combined = words[i] + words[j]
                if is_palindrome(combined):
                    result.append([i, j])
    
    return result

def distinctEchoSubstrings(text):
    """
    LeetCode 1316: Distinct Echo Substrings
    Count distinct echo substrings using suffix array
    """
    n = len(text)
    sa = SuffixArray(text)
    echo_substrings = set()
    
    # Check all possible echo lengths (must be even)
    for length in range(2, n + 1, 2):
        half_length = length // 2
        
        # Check all substrings of this length
        for i in range(n - length + 1):
            substring = text[i:i + length]
            first_half = substring[:half_length]
            second_half = substring[half_length:]
            
            if first_half == second_half:
                echo_substrings.add(substring)
    
    return len(echo_substrings)

# Template for range minimum query on LCP array
class LCPRangeMinQuery:
    """
    Support range minimum queries on LCP array for advanced suffix array operations
    """
    
    def __init__(self, lcp_array):
        self.lcp = lcp_array
        self.n = len(lcp_array)
        
        # Build sparse table for range minimum queries
        self.sparse_table = self._build_sparse_table()
    
    def _build_sparse_table(self):
        """Build sparse table for O(1) range minimum queries"""
        if not self.lcp:
            return []
        
        log_n = self.n.bit_length()
        table = [[0] * log_n for _ in range(self.n)]
        
        # Initialize first column
        for i in range(self.n):
            table[i][0] = self.lcp[i]
        
        # Fill remaining columns
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                table[i][j] = min(table[i][j-1], table[i + (1 << (j-1))][j-1])
                i += 1
            j += 1
        
        return table
    
    def query(self, left, right):
        """Query minimum LCP value in range [left, right]"""
        if left > right or right >= self.n:
            return float('inf')
        
        if left == right:
            return self.lcp[left]
        
        # Find largest power of 2 that fits in range
        length = right - left + 1
        log_length = (length - 1).bit_length() - 1
        
        return min(
            self.sparse_table[left][log_length],
            self.sparse_table[right - (1 << log_length) + 1][log_length]
        )

# Template for advanced suffix array applications
def suffix_array_pattern_matching_with_errors(text, pattern, max_errors):
    """
    Pattern matching allowing up to max_errors mismatches using suffix array
    """
    sa = SuffixArray(text)
    matches = []
    
    # For each suffix, check if pattern matches with at most max_errors
    for i in range(len(text) - len(pattern) + 1):
        errors = 0
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                errors += 1
                if errors > max_errors:
                    break
        
        if errors <= max_errors:
            matches.append(i)
    
    return matches