# String Algorithms

This repository contains implementations of five fundamental string algorithms: **KMP (Knuth-Morris-Pratt)**, **Rabin-Karp Rolling Hash**, **Z-Algorithm**, **Suffix Array**, and advanced string processing techniques.

## What are String Algorithms?

String algorithms efficiently solve problems involving:
- **Pattern matching**: Finding occurrences of patterns in text
- **String preprocessing**: Building auxiliary data structures for fast queries
- **Substring analysis**: Finding repeated, longest, or distinct substrings
- **Text processing**: Palindromes, rotations, and string transformations

## Algorithm Comparison

| Algorithm | Preprocessing | Search | Space | Best Use Case |
|-----------|--------------|--------|-------|---------------|
| **KMP** | O(m) | O(n) | O(m) | Single pattern, many searches |
| **Rabin-Karp** | O(m) | O(n) avg, O(nm) worst | O(1) | Multiple patterns, rolling hash |
| **Z-Algorithm** | O(n+m) | O(n+m) | O(n+m) | Pattern matching, prefix analysis |
| **Suffix Array** | O(n log²n) | O(m log n) | O(n) | Multiple queries, substring problems |

**Legend**: n = text length, m = pattern length

## 1. KMP (Knuth-Morris-Pratt) Algorithm

### 🎯 Core Concept
Uses **failure function (LPS array)** to avoid re-examining characters when pattern mismatch occurs.

### ⚙️ Key Advantages
- **Linear time guarantee**: Always O(n + m), no worst-case degradation
- **No backtracking**: Never re-examines text characters
- **Optimal for single pattern**: Best choice for finding one pattern many times
- **Failure function applications**: Useful beyond just pattern matching

### 📝 Core Applications
- **Pattern matching**: Find all occurrences efficiently
- **Palindrome problems**: Shortest palindrome, palindrome detection
- **String periodicity**: Detect repeating patterns
- **String rotation**: Check if one string is rotation of another

### 🎯 When to Choose KMP
```
✅ Choose when:
- Need guaranteed linear time
- Single pattern, multiple searches
- Working with failure function/LPS concepts
- Need to avoid worst-case behavior

❌ Don't choose when:
- Multiple patterns to search simultaneously
- Need simplicity over optimality
- Working with very short patterns
```

### 💡 LeetCode Pattern Recognition
```
"Find first occurrence of pattern"
"Shortest palindrome"
"Repeated substring pattern"
"String rotation problems"
"Longest prefix that is also suffix"
```

## 2. Rabin-Karp Rolling Hash Algorithm

### 🎯 Core Concept
Uses **polynomial rolling hash** to convert string matching into integer comparison with O(1) rolling updates.

### ⚙️ Key Advantages
- **Multiple pattern search**: Efficiently search for many patterns
- **Rolling hash property**: O(1) updates when sliding window
- **2D extension**: Can handle 2D pattern matching
- **Probabilistic**: Fast average case with controllable collision rate

### 📝 Core Applications
- **Multiple pattern matching**: Search for many patterns simultaneously
- **Substring problems**: Longest duplicate substring, distinct substrings
- **Rolling window**: Problems requiring sliding window with string comparison
- **2D pattern matching**: Find 2D patterns in 2D grids

### 🎯 When to Choose Rabin-Karp
```
✅ Choose when:
- Multiple patterns to search
- Need rolling hash for sliding windows
- Working with substring frequency problems
- 2D pattern matching required

❌ Don't choose when:
- Need guaranteed worst-case performance
- Single pattern search (KMP is better)
- Hash collisions are unacceptable
```

### 💡 LeetCode Pattern Recognition
```
"Find repeated DNA sequences"
"Longest duplicate substring"
"Multiple pattern search"
"Rolling window with string comparison"
"Distinct substrings counting"
```

## 3. Z-Algorithm

### 🎯 Core Concept
Computes **Z-array** where Z[i] = length of longest substring starting from i that matches prefix.

### ⚙️ Key Advantages
- **Simpler than KMP**: Easier to understand and implement
- **Linear time**: O(n) preprocessing and search
- **Direct prefix information**: Z-array gives immediate prefix overlap info
- **Versatile**: Good for various string problems beyond pattern matching

### 📝 Core Applications
- **Pattern matching**: Linear time search with simple logic
- **Prefix analysis**: Direct access to prefix overlap lengths
- **String borders**: Find all borders (prefix = suffix)
- **Period detection**: Find fundamental periods of strings

### 🎯 When to Choose Z-Algorithm
```
✅ Choose when:
- Want simpler alternative to KMP
- Need prefix overlap information
- Working with string borders/periods
- Prefer straightforward implementation

❌ Don't choose when:
- Memory usage is critical (needs O(n) extra space)
- Working with very large texts
- Need the most optimized solution
```

### 💡 LeetCode Pattern Recognition
```
"Longest prefix that is also suffix"
"String pattern matching"
"Border detection problems"
"Period and repetition analysis"
```

## 4. Suffix Array

### 🎯 Core Concept
Array of starting positions of all suffixes sorted lexicographically, enhanced with **LCP (Longest Common Prefix) array**.

### ⚙️ Key Advantages
- **Multiple queries**: Efficient for many pattern searches
- **Substring problems**: Excellent for longest/distinct substring problems
- **Space efficient**: O(n) space for unlimited queries
- **LCP array power**: Enables advanced substring analysis

### 📝 Core Applications
- **Multiple pattern queries**: Many different patterns in same text
- **Longest repeated substring**: Direct solution using LCP array
- **Distinct substring counting**: Formula using LCP array
- **Generalized problems**: Multiple string analysis

### 🎯 When to Choose Suffix Array
```
✅ Choose when:
- Many different pattern queries on same text
- Need longest/shortest/distinct substring analysis
- Working with multiple strings
- Advanced text processing required

❌ Don't choose when:
- Single pattern search (overkill)
- Construction time is critical
- Simple problems (use simpler algorithms)
```

### 💡 LeetCode Pattern Recognition
```
"Longest duplicate substring"
"Count distinct substrings"
"Multiple pattern search"
"Longest common substring"
"k-th lexicographic substring"
```

## Decision Framework

### 🔍 Quick Algorithm Selection

```
What's your primary need?

🔎 Single Pattern Search
├── Need guaranteed linear time? → KMP
├── Want simplicity? → Z-Algorithm  
└── Need rolling hash features? → Rabin-Karp

🔎 Multiple Pattern Search
├── Few patterns, rolling window? → Rabin-Karp
├── Many patterns on same text? → Suffix Array
└── Simple prefix matching? → Z-Algorithm

🔎 Substring Analysis
├── Longest duplicate/repeated? → Suffix Array
├── Count distinct substrings? → Suffix Array
├── Rolling hash problems? → Rabin-Karp
└── Prefix/suffix analysis? → KMP or Z-Algorithm

🔎 Advanced Text Processing
├── Multiple strings? → Generalized Suffix Array
├── 2D patterns? → 2D Rabin-Karp
├── String borders/periods? → Z-Algorithm or KMP
└── Complex preprocessing? → Suffix Array
```

### 🎯 Problem Type Mapping

| Problem Pattern | Primary Choice | Alternative |
|----------------|----------------|-------------|
| **"Find pattern in text"** | KMP | Z-Algorithm |
| **"Multiple pattern search"** | Rabin-Karp | Suffix Array |
| **"Longest duplicate substring"** | Suffix Array | Rabin-Karp |
| **"Repeated DNA sequences"** | Rabin-Karp | Hash Set |
| **"Shortest palindrome"** | KMP | Z-Algorithm |
| **"String rotation"** | KMP | Rolling Hash |
| **"Count distinct substrings"** | Suffix Array | Rolling Hash |
| **"Longest common substring"** | Generalized SA | Rolling Hash |

## Implementation Strategy Guide

### 1. Starting Templates
```python
# For single pattern matching
def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    # ... KMP logic

# For multiple patterns or rolling windows
rh = RollingHash()
hashes = rh.compute_rolling_hashes(text, pattern_length)

# For complex substring analysis
sa = SuffixArray(text)
result = sa.longest_repeated_substring()

# For simple prefix analysis
z = z_algorithm(text + "$" + pattern)
```

### 2. Performance Optimization Tips
```python
# Use appropriate base and modulus for rolling hash
rh = RollingHash(base=31, mod=10**9 + 7)

# For collision-sensitive applications, use double hashing
drh = DoubleRollingHash()

# Coordinate compression for large alphabets
compress = {char: i for i, char in enumerate(sorted(set(text)))}
```

### 3. Common Preprocessing Patterns
```python
# Pattern + separator + text (for Z-algorithm and KMP)
combined = pattern + "$" + text

# Suffix array with LCP for advanced queries
sa = SuffixArray(text)
lcp = sa.lcp_array

# Rolling hash for sliding window problems
rolling_hashes = rh.compute_rolling_hashes(text, window_size)
```

## Performance Analysis

### 🚀 Time Complexity Summary

| Operation | KMP | Rabin-Karp | Z-Algorithm | Suffix Array |
|-----------|-----|------------|-------------|--------------|
| **Preprocessing** | O(m) | O(m) | O(n+m) | O(n log²n) |
| **Single Search** | O(n) | O(n) avg | O(n+m) | O(m log n) |
| **k Pattern Search** | O(kn) | O(n+km) | O(kn) | O(k m log n) |
| **Build Once, Query Many** | ❌ | ❌ | ❌ | ✅ |

### 💾 Space Complexity
- **KMP**: O(m) for LPS array
- **Rabin-Karp**: O(1) basic, O(k) for k patterns  
- **Z-Algorithm**: O(n+m) for combined string
- **Suffix Array**: O(n) for SA + LCP arrays

### ⚡ Practical Considerations

1. **Short patterns**: Simple algorithms often faster due to low constants
2. **Long patterns**: Sophisticated algorithms show their advantage
3. **Multiple searches**: Amortize preprocessing cost over many queries
4. **Memory constraints**: Choose algorithm based on space requirements
5. **Collision handling**: Use double hashing for critical applications

## Common Pitfalls and Solutions

### ⚠️ Frequent Mistakes

1. **Hash collisions**: Not handling false positives in Rabin-Karp
2. **Modular arithmetic**: Incorrect handling of negative numbers
3. **Index confusion**: Off-by-one errors in pattern matching
4. **LPS computation**: Bugs in KMP failure function
5. **Suffix array indexing**: Confusion between suffix positions and ranks

### 💡 Best Practices

1. **Always verify matches** in Rabin-Karp after hash equality
2. **Use proven hash parameters** (base=31, mod=10^9+7)
3. **Test edge cases**: Empty strings, single characters, no matches
4. **Choose appropriate separator** characters for combined strings
5. **Profile performance** for your specific use case

## Advanced Topics

### 🧠 Advanced Techniques

- **Generalized Suffix Arrays**: Multiple string processing
- **Suffix Trees**: More space but faster queries
- **Aho-Corasick**: Multiple pattern matching with automata
- **Manacher's Algorithm**: Linear-time palindrome detection
- **Heavy-Light Decomposition**: Tree string problems

### 🌟 Real-World Applications

- **Text editors**: Find/replace, syntax highlighting
- **Bioinformatics**: DNA sequence analysis, genome assembly
- **Data compression**: Finding repeated patterns
- **Information retrieval**: Search engines, document similarity
- **Security**: Malware signature detection, intrusion detection

## Interview Strategy

### 🎯 Pattern Recognition Process

1. **Identify the core need**: Single vs multiple patterns, preprocessing allowed?
2. **Check constraints**: String length, number of queries, memory limits
3. **Select appropriate algorithm** using decision framework
4. **Start with clear template** and adapt to specific requirements
5. **Handle edge cases** and verify correctness

### 🔄 Problem-Solving Steps

1. **Understand the problem type** (pattern matching, substring analysis, etc.)
2. **Choose the right algorithm** based on requirements
3. **Implement incrementally** (basic version first, then optimizations)
4. **Test thoroughly** with edge cases
5. **Analyze complexity** and optimize if needed

### 💪 Practice Progression

1. **Master KMP first** - fundamental pattern matching
2. **Learn rolling hash** - versatile for many problems
3. **Understand Z-algorithm** - simpler alternative to KMP
4. **Tackle suffix arrays** - advanced substring problems
5. **Combine techniques** - use multiple algorithms together

Choose the algorithm that best matches your problem's characteristics. When in doubt, start with the simplest solution that meets your requirements and optimize if necessary!