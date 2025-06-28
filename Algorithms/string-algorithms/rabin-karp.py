"""
LeetCode Problems where Rabin-Karp Algorithm can be applied:

28. Find the Index of the First Occurrence in a String
187. Repeated DNA Sequences
214. Shortest Palindrome
686. Repeated String Match
718. Maximum Length of Repeated Subarray
1044. Longest Duplicate Substring
1062. Longest Repeating Substring
1316. Distinct Echo Substrings
1392. Longest Happy Prefix
1698. Number of Distinct Substrings in a String
1923. Longest Common Subpath
2261. K Divisible Elements Subarrays
"""

class RollingHash:
    """
    Rolling Hash implementation for efficient string hashing
    
    Uses polynomial rolling hash with prime modulus
    Supports forward and backward rolling
    """
    
    def __init__(self, base=31, mod=10**9 + 7):
        self.base = base
        self.mod = mod
        self.pow_base = [1]  # Powers of base
    
    def _extend_powers(self, length):
        """Extend powers array to required length"""
        while len(self.pow_base) <= length:
            self.pow_base.append((self.pow_base[-1] * self.base) % self.mod)
    
    def compute_hash(self, s):
        """Compute hash of entire string"""
        hash_val = 0
        for i, char in enumerate(s):
            hash_val = (hash_val * self.base + ord(char)) % self.mod
        return hash_val
    
    def compute_rolling_hashes(self, s, length):
        """
        Compute rolling hashes of all substrings of given length
        
        Returns: list of (hash, start_index) tuples
        """
        if length > len(s):
            return []
        
        self._extend_powers(length)
        
        hashes = []
        current_hash = 0
        
        # Compute initial hash
        for i in range(length):
            current_hash = (current_hash * self.base + ord(s[i])) % self.mod
        
        hashes.append((current_hash, 0))
        
        # Roll the hash for remaining positions
        for i in range(length, len(s)):
            # Remove leftmost character
            current_hash = (current_hash - ord(s[i - length]) * self.pow_base[length - 1]) % self.mod
            # Add rightmost character
            current_hash = (current_hash * self.base + ord(s[i])) % self.mod
            # Ensure positive
            current_hash = (current_hash + self.mod) % self.mod
            
            hashes.append((current_hash, i - length + 1))
        
        return hashes

def rabin_karp_search(text, pattern):
    """
    Basic Rabin-Karp pattern matching
    
    Time: O(n + m) average, O(nm) worst case
    Space: O(1)
    """
    if not pattern:
        return [0]
    
    n, m = len(text), len(pattern)
    if m > n:
        return []
    
    rh = RollingHash()
    pattern_hash = rh.compute_hash(pattern)
    
    matches = []
    current_hash = 0
    base_pow = 1
    
    # Compute initial hash and base power
    for i in range(m):
        current_hash = (current_hash * rh.base + ord(text[i])) % rh.mod
        if i < m - 1:
            base_pow = (base_pow * rh.base) % rh.mod
    
    # Check first window
    if current_hash == pattern_hash and text[:m] == pattern:
        matches.append(0)
    
    # Roll the hash for remaining positions
    for i in range(m, n):
        # Remove leftmost character
        current_hash = (current_hash - ord(text[i - m]) * base_pow) % rh.mod
        # Add rightmost character
        current_hash = (current_hash * rh.base + ord(text[i])) % rh.mod
        # Ensure positive
        current_hash = (current_hash + rh.mod) % rh.mod
        
        # Check for match (with verification to avoid false positives)
        if current_hash == pattern_hash and text[i - m + 1:i + 1] == pattern:
            matches.append(i - m + 1)
    
    return matches

def findRepeatedDnaSequences(s):
    """
    LeetCode 187: Repeated DNA Sequences
    Find all 10-letter DNA sequences that appear more than once
    """
    if len(s) < 10:
        return []
    
    rh = RollingHash()
    hashes = rh.compute_rolling_hashes(s, 10)
    
    hash_count = {}
    for hash_val, start_idx in hashes:
        substring = s[start_idx:start_idx + 10]
        if hash_val not in hash_count:
            hash_count[hash_val] = []
        hash_count[hash_val].append(substring)
    
    result = []
    for hash_val, substrings in hash_count.items():
        if len(substrings) > 1:
            result.append(substrings[0])  # Add one representative
    
    return result

def longestDupSubstring(s):
    """
    LeetCode 1044: Longest Duplicate Substring
    Find longest duplicate substring using binary search + rolling hash
    """
    def has_duplicate_of_length(length):
        """Check if there's a duplicate substring of given length"""
        if length == 0:
            return True
        
        rh = RollingHash()
        hashes = rh.compute_rolling_hashes(s, length)
        
        seen = set()
        for hash_val, start_idx in hashes:
            if hash_val in seen:
                return s[start_idx:start_idx + length]
            seen.add(hash_val)
        return None
    
    # Binary search on length
    left, right = 0, len(s) - 1
    result = ""
    
    while left <= right:
        mid = (left + right) // 2
        duplicate = has_duplicate_of_length(mid)
        
        if duplicate:
            result = duplicate
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def findLength(nums1, nums2):
    """
    LeetCode 718: Maximum Length of Repeated Subarray
    Find length of longest common subarray using rolling hash
    """
    def has_common_subarray(length):
        """Check if there's a common subarray of given length"""
        if length == 0:
            return True
        
        # Hash all subarrays of nums1
        rh = RollingHash()
        hashes1 = rh.compute_rolling_hashes(nums1, length)
        hash_set = {hash_val for hash_val, _ in hashes1}
        
        # Check subarrays of nums2
        hashes2 = rh.compute_rolling_hashes(nums2, length)
        for hash_val, _ in hashes2:
            if hash_val in hash_set:
                return True
        
        return False
    
    # Binary search on length
    left, right = 0, min(len(nums1), len(nums2))
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if has_common_subarray(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def distinctEchoSubstrings(text):
    """
    LeetCode 1316: Distinct Echo Substrings
    Count distinct substrings that are concatenation of two identical strings
    """
    n = len(text)
    rh = RollingHash()
    echo_hashes = set()
    
    # Check all possible echo substring lengths (must be even)
    for length in range(2, n + 1, 2):
        half_length = length // 2
        
        # Get hashes for all substrings of half_length
        hashes = rh.compute_rolling_hashes(text, half_length)
        hash_to_indices = {}
        
        for hash_val, start_idx in hashes:
            if hash_val not in hash_to_indices:
                hash_to_indices[hash_val] = []
            hash_to_indices[hash_val].append(start_idx)
        
        # Check for echo substrings
        for hash_val, indices in hash_to_indices.items():
            for idx in indices:
                # Check if the same hash appears immediately after
                if idx + half_length < n:
                    next_substring = text[idx + half_length:idx + length]
                    if len(next_substring) == half_length:
                        next_hash = rh.compute_hash(next_substring)
                        if next_hash == hash_val:
                            # Verify it's actually the same substring
                            if text[idx:idx + half_length] == next_substring:
                                echo_hash = rh.compute_hash(text[idx:idx + length])
                                echo_hashes.add(echo_hash)
    
    return len(echo_hashes)

def numDistinct(s):
    """
    LeetCode 1698: Number of Distinct Substrings in a String
    Count number of distinct substrings using rolling hash
    """
    n = len(s)
    rh = RollingHash()
    all_hashes = set()
    
    # Generate all substring hashes
    for length in range(1, n + 1):
        hashes = rh.compute_rolling_hashes(s, length)
        for hash_val, _ in hashes:
            all_hashes.add(hash_val)
    
    return len(all_hashes)

class DoubleRollingHash:
    """
    Double rolling hash to reduce collision probability
    Uses two different bases and moduli
    """
    
    def __init__(self):
        self.rh1 = RollingHash(base=31, mod=10**9 + 7)
        self.rh2 = RollingHash(base=37, mod=10**9 + 9)
    
    def compute_hash(self, s):
        """Compute double hash of string"""
        h1 = self.rh1.compute_hash(s)
        h2 = self.rh2.compute_hash(s)
        return (h1, h2)
    
    def compute_rolling_hashes(self, s, length):
        """Compute double rolling hashes"""
        hashes1 = self.rh1.compute_rolling_hashes(s, length)
        hashes2 = self.rh2.compute_rolling_hashes(s, length)
        
        return [((h1, h2), idx) for (h1, idx1), (h2, idx2) in zip(hashes1, hashes2)]

def longestCommonSubpath(n, paths):
    """
    LeetCode 1923: Longest Common Subpath
    Find longest common subpath among all paths using double hashing
    """
    def has_common_subpath(length):
        """Check if there's a common subpath of given length"""
        if length == 0:
            return True
        
        drh = DoubleRollingHash()
        
        # Get hashes from first path
        if not paths:
            return False
        
        hashes = drh.compute_rolling_hashes(paths[0], length)
        common_hashes = {hash_val for hash_val, _ in hashes}
        
        # Intersect with hashes from other paths
        for path in paths[1:]:
            if not common_hashes:
                break
            
            path_hashes = drh.compute_rolling_hashes(path, length)
            path_hash_set = {hash_val for hash_val, _ in path_hashes}
            common_hashes &= path_hash_set
        
        return len(common_hashes) > 0
    
    if not paths:
        return 0
    
    # Binary search on length
    left, right = 0, min(len(path) for path in paths)
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if has_common_subpath(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def kDivisibleElements(nums, k, p):
    """
    LeetCode 2261: K Divisible Elements Subarrays
    Count distinct subarrays with at most k elements divisible by p
    """
    n = len(nums)
    rh = RollingHash()
    valid_hashes = set()
    
    # Check all possible subarrays
    for i in range(n):
        divisible_count = 0
        for j in range(i, n):
            if nums[j] % p == 0:
                divisible_count += 1
            
            if divisible_count <= k:
                subarray = nums[i:j+1]
                hash_val = rh.compute_hash([str(x) for x in subarray])
                valid_hashes.add(hash_val)
            else:
                break
    
    return len(valid_hashes)

# Template for multiple pattern matching
def multi_pattern_search(text, patterns):
    """
    Search for multiple patterns efficiently using rolling hash
    
    Args:
        text: input text
        patterns: list of patterns to search for
    
    Returns:
        dict mapping pattern to list of match positions
    """
    rh = RollingHash()
    results = {}
    
    # Group patterns by length for efficiency
    patterns_by_length = {}
    for pattern in patterns:
        length = len(pattern)
        if length not in patterns_by_length:
            patterns_by_length[length] = []
        patterns_by_length[length].append(pattern)
    
    # Process each length group
    for length, pattern_group in patterns_by_length.items():
        # Compute pattern hashes
        pattern_hashes = {}
        for pattern in pattern_group:
            hash_val = rh.compute_hash(pattern)
            pattern_hashes[hash_val] = pattern
        
        # Get rolling hashes of text
        text_hashes = rh.compute_rolling_hashes(text, length)
        
        # Find matches
        for hash_val, start_idx in text_hashes:
            if hash_val in pattern_hashes:
                pattern = pattern_hashes[hash_val]
                # Verify match to avoid false positives
                if text[start_idx:start_idx + length] == pattern:
                    if pattern not in results:
                        results[pattern] = []
                    results[pattern].append(start_idx)
    
    return results

# Template for palindrome detection using rolling hash
def count_palindromic_substrings_hash(s):
    """
    Count palindromic substrings using rolling hash for efficiency
    """
    n = len(s)
    rh_forward = RollingHash(base=31)
    rh_backward = RollingHash(base=31)
    
    count = 0
    
    # For each substring length
    for length in range(1, n + 1):
        # Get forward and backward hashes
        forward_hashes = rh_forward.compute_rolling_hashes(s, length)
        backward_hashes = rh_backward.compute_rolling_hashes(s[::-1], length)
        
        # Reverse the backward hashes to match positions
        backward_dict = {}
        for hash_val, start_idx in backward_hashes:
            # Convert to original string position
            orig_start = n - start_idx - length
            backward_dict[orig_start] = hash_val
        
        # Check for palindromes
        for hash_val, start_idx in forward_hashes:
            if start_idx in backward_dict and hash_val == backward_dict[start_idx]:
                # Verify it's actually a palindrome
                substr = s[start_idx:start_idx + length]
                if substr == substr[::-1]:
                    count += 1
    
    return count