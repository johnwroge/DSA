# Segment Tree Algorithms

This repository contains implementations of four essential segment tree data structures: **Fenwick Tree (Binary Indexed Tree)**, **Point Update Segment Tree**, **Range Query Segment Tree**, and **Range Update Segment Tree with Lazy Propagation**.

## What are Segment Trees?

Segment trees are tree data structures that allow efficient querying and updating of array ranges. They excel at problems requiring:
- **Range queries**: sum, min, max, GCD, XOR over a range
- **Point/range updates**: modify single elements or entire ranges
- **Dynamic arrays**: handle updates while maintaining query efficiency

## Algorithm Comparison

| Data Structure | Build | Point Update | Range Update | Range Query | Space | Best Use Case |
|---------------|-------|-------------|-------------|-------------|-------|---------------|
| **Fenwick Tree** | O(n log n) | O(log n) | ❌ | O(log n) | O(n) | Prefix sums, simple range queries |
| **Point Update Segment Tree** | O(n) | O(log n) | ❌ | O(log n) | O(n) | General range queries with point updates |
| **Range Query Segment Tree** | O(n) | O(log n) | ❌ | O(log n) | O(n) | Complex queries, multiple operations |
| **Lazy Segment Tree** | O(n) | O(log n) | O(log n) | O(log n) | O(n) | Range updates with range queries |

## 1. Fenwick Tree (Binary Indexed Tree)

### 🎯 Core Concept
Efficiently handle **prefix sum queries** and **point updates** using bit manipulation tricks.

### ⚙️ Key Advantages
- **Simplest implementation** among segment trees
- **Minimal memory usage** (just one array)
- **Fastest for prefix sums** due to cache-friendly operations
- **Easy to understand** bit manipulation logic

### 📝 Common Use Cases
- **Inversion counting**: Count smaller/larger elements
- **Coordinate compression**: Handle large value ranges
- **Dynamic prefix sums**: Frequent updates with prefix queries
- **2D range queries**: Matrix sum queries

### 🎯 When to Choose Fenwick Tree
```
✅ Choose when:
- You only need sum queries (not min/max)
- Updates are point updates (not range updates)
- Memory is constrained
- Implementation simplicity is important

❌ Don't choose when:
- Need range updates
- Need min/max/GCD queries
- Need complex custom operations
```

### 💡 LeetCode Pattern Recognition
```
"Count smaller numbers after self"
"Range sum with updates"
"Inversion counting"
"Coordinate compression problems"
```

## 2. Point Update Segment Tree

### 🎯 Core Concept
Classic segment tree supporting **any associative operation** with **point updates** only.

### ⚙️ Key Advantages
- **Supports any operation**: sum, min, max, GCD, XOR, etc.
- **Clean recursive structure** that's easy to modify
- **Optimal for point updates** with complex queries
- **Foundation for advanced techniques**

### 📝 Common Use Cases
- **Range min/max queries**: Find extremes in ranges
- **Multiple statistics**: Track sum, min, max simultaneously
- **Custom operations**: GCD, XOR, custom functions
- **Order statistics**: Kth smallest element

### 🎯 When to Choose Point Update Segment Tree
```
✅ Choose when:
- Need operations other than sum (min, max, GCD, etc.)
- Updates are mostly point updates
- Need custom/complex operations
- Want clean, extensible code

❌ Don't choose when:
- Only need prefix sums (use Fenwick)
- Need frequent range updates (use Lazy)
- Memory is very constrained
```

### 💡 LeetCode Pattern Recognition
```
"Range minimum/maximum query"
"Custom operation over ranges"
"Multiple statistics tracking"
"Order statistics problems"
```

## 3. Range Query Segment Tree

### 🎯 Core Concept
Advanced segment tree supporting **multiple query types** and **complex node structures**.

### ⚙️ Key Advantages
- **Multiple operations** in single tree
- **Persistent versions** for historical queries
- **Complex node data** (multiple values per node)
- **Advanced querying** like mode, median

### 📝 Common Use Cases
- **Multi-statistic tracking**: Sum, min, max, count together
- **Persistent queries**: Query historical versions
- **Complex range operations**: Mode, median, custom metrics
- **Coordinate compression**: Large value ranges

### 🎯 When to Choose Range Query Segment Tree
```
✅ Choose when:
- Need multiple query types simultaneously
- Working with complex data per node
- Need persistent/historical queries
- Have custom complex operations

❌ Don't choose when:
- Simple single-operation queries
- Need range updates frequently
- Implementation complexity is a concern
```

### 💡 LeetCode Pattern Recognition
```
"Multiple statistics in ranges"
"Historical/versioned queries"
"Complex range operations"
"Mode/median in ranges"
```

## 4. Range Update Segment Tree (Lazy Propagation)

### 🎯 Core Concept
Most powerful segment tree supporting **efficient range updates** using **lazy propagation**.

### ⚙️ Key Advantages
- **Range updates in O(log n)** instead of O(n)
- **Supports both addition and assignment**
- **Lazy propagation** delays updates until necessary
- **Most versatile** for complex update patterns

### 📝 Common Use Cases
- **Range addition**: Add value to entire ranges
- **Range assignment**: Set ranges to specific values
- **Difference arrays**: Multiple range operations
- **Interval scheduling**: Overlapping intervals

### 🎯 When to Choose Lazy Segment Tree
```
✅ Choose when:
- Frequent range updates required
- Both range updates AND range queries needed
- Working with intervals/schedules
- Need maximum performance for ranges

❌ Don't choose when:
- Only point updates (use simpler trees)
- Implementation complexity is prohibitive
- Memory usage is critical
```

### 💡 LeetCode Pattern Recognition
```
"Range addition/assignment"
"Multiple range operations"
"Interval problems with updates"
"Car pooling/flight booking patterns"
```

## Decision Framework

### 🔍 Quick Decision Tree

```
What type of updates do you need?

📍 Only Point Updates?
├── Only need prefix sums? → Fenwick Tree
├── Need min/max/custom ops? → Point Update Segment Tree
└── Need multiple operations? → Range Query Segment Tree

📊 Need Range Updates?
├── Simple range addition? → Lazy Segment Tree
├── Range assignment too? → Advanced Lazy Segment Tree
└── Multiple update types? → Custom Lazy Implementation
```

### 🎯 Problem Type Mapping

| Problem Pattern | Recommended Solution | Alternative |
|----------------|---------------------|-------------|
| **"Count inversions"** | Fenwick Tree | Point Update ST |
| **"Range sum with point updates"** | Fenwick Tree | Point Update ST |
| **"Range min/max queries"** | Point Update ST | Range Query ST |
| **"Multiple range statistics"** | Range Query ST | Multiple STs |
| **"Range addition operations"** | Lazy ST | Difference Array |
| **"Interval scheduling"** | Lazy ST | Event-based |

## Implementation Strategies

### 1. Starting Template Choice
```python
# For prefix sums and inversions
fenwick = FenwickTree(n)

# For range min/max with point updates
seg_tree = SegmentTree(arr, operation='min')

# For multiple operations
multi_tree = MultiOperationSegmentTree(arr)

# For range updates
lazy_tree = LazySegmentTree(arr, operation='sum', update_type='add')
```

### 2. Coordinate Compression Pattern
```python
# When dealing with large values
def compress_coordinates(values):
    sorted_vals = sorted(set(values))
    return {v: i for i, v in enumerate(sorted_vals)}

# Use compressed indices in segment tree
compress = compress_coordinates(arr)
compressed_arr = [compress[x] for x in arr]
```

### 3. Lazy Propagation Pattern
```python
# Standard lazy propagation template
def push_lazy(node, start, end):
    if has_lazy[node]:
        apply_update(node, start, end)
        if start != end:  # Not leaf
            propagate_to_children(node)
        clear_lazy(node)
```

## Performance Considerations

### 🚀 Time Complexity Summary
- **Build**: O(n) for all except Fenwick O(n log n)
- **Point Update**: O(log n) for all
- **Range Update**: O(log n) only for Lazy ST
- **Range Query**: O(log n) for all

### 💾 Space Complexity
- **Fenwick**: O(n) - most memory efficient
- **Standard ST**: O(4n) - typical segment tree
- **Multi-operation**: O(4n × operations) - scales with complexity
- **Lazy ST**: O(4n) + lazy arrays - highest overhead

### ⚡ Practical Performance Tips

1. **Use Fenwick when possible** - fastest for simple operations
2. **Coordinate compression** for large value ranges
3. **Iterative builds** can be faster than recursive
4. **Memory pooling** for frequent tree recreation
5. **Template specialization** for specific operations

## Common Pitfalls and Solutions

### ⚠️ Common Mistakes

1. **Wrong tree size**: Use `4 * n` for safety, not `2 * n`
2. **Index confusion**: Consistent 0-based or 1-based indexing
3. **Lazy propagation bugs**: Always push before accessing children
4. **Identity elements**: Wrong identity for min/max operations
5. **Coordinate compression**: Off-by-one in mapping

### 💡 Best Practices

1. **Start simple**: Begin with basic implementation, add features
2. **Test edge cases**: Empty ranges, single elements, boundary conditions
3. **Use templates**: Adapt proven templates rather than writing from scratch
4. **Modular design**: Separate operation logic from tree structure
5. **Profile performance**: Measure actual performance for your use case

## Advanced Topics

### 🧠 Advanced Techniques

- **Persistent Segment Trees**: Keep all historical versions
- **2D Segment Trees**: Handle 2D range queries/updates
- **Fractional Cascading**: Optimize multi-dimensional queries
- **Link-Cut Trees**: Dynamic tree connectivity
- **Heavy-Light Decomposition**: Tree path queries

### 🌟 Real-World Applications

- **Database indexing**: Range queries on sorted data
- **Graphics programming**: Rectangle intersection queries
- **Financial systems**: Time-series range analytics
- **Game development**: Collision detection, spatial queries
- **Data analytics**: Dynamic windowed aggregations

## Interview Strategy

### 🎯 Recognition Patterns

1. **"Range sum/min/max with updates"** → Segment Tree family
2. **"Count smaller/larger elements"** → Fenwick Tree
3. **"Multiple range operations"** → Lazy Propagation
4. **"Interval problems"** → Range Update ST

### 🔄 Problem-Solving Steps

1. **Identify operations needed** (point vs range updates/queries)
2. **Choose appropriate data structure** using decision framework
3. **Handle coordinate compression** if needed
4. **Implement incrementally** (build → query → update)
5. **Test with edge cases** and verify complexity

### 💪 Practice Progression

1. **Start with Fenwick Tree** - master the basics
2. **Learn Point Update ST** - understand tree structure  
3. **Practice Range Query ST** - handle complexity
4. **Master Lazy Propagation** - tackle hardest problems

Choose the segment tree variant that best matches your problem's requirements. When in doubt, start with the simplest solution that works and optimize if needed!