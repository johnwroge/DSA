"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximized?
"""

def is_a_right_triangle(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def three_sum(nums, target):
    res = []
    for i in range(len(nums)):
        j, k = i + 1, len(nums) - 1
        if i - 1 >= 0 and nums[i] == nums[i - 1]:
            continue
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < target:
                j += 1
            elif total > target:
                k -= 1
            else:
                if is_a_right_triangle(nums[i], nums[j], nums[k]):
                    res.append([nums[i], nums[j], nums[k]])
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    while k - 1 >= j and nums[k] == nums[k - 1]:
                        k -= 1
                j += 1
                k -= 1
    return res


def my_solution():
    results = []
    for n in range(3, 1000):
        arr = [i for i in range(n)]
        candidates = three_sum(arr, n)
        results.append((n, len(candidates)))
    results.sort(key = lambda x: x[1])
    return results[-1]

# optimized

def count_right_triangles(p):
    count = 0
    for a in range(1, p // 3 + 1):
        for b in range(a, (p - a) // 2 + 1):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1
    return count

def solution():
    max_count = 0
    best_p = 0
    
    for p in range(3, 1001):
        count = count_right_triangles(p)
        if count > max_count:
            max_count = count
            best_p = p
    
    return best_p

print(solution())

