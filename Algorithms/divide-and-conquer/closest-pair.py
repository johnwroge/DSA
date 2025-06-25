"""
Closest Pair of Points - Divide and Conquer

LeetCode #973: K Closest Points to Origin
LeetCode #1478: Allocate Mailboxes

Core pattern: Divide points into two halves, find closest pair in each half and across dividing line.
"""

import math

def closest_pair(points):
    # Sort points by x-coordinate
    points.sort(key=lambda p: p[0])
    return _closest_pair(points)

def _closest_pair(points):
    n = len(points)
    
    # Base case: use brute force for small number of points
    if n <= 3:
        return min_distance_brute(points)
    
    # Divide points into two halves
    mid = n // 2
    mid_point = points[mid]
    
    # Recursively find closest pair in each half
    left_min = _closest_pair(points[:mid])
    right_min = _closest_pair(points[mid:])
    
    # Find minimum of left and right halves
    min_dist = min(left_min, right_min)
    
    # Find points close to the dividing line
    strip = [p for p in points if abs(p[0] - mid_point[0]) < min_dist]
    strip.sort(key=lambda p: p[1])  # Sort by y-coordinate
    
    # Check points in strip
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j][1] - strip[i][1] < min_dist:
            dist = distance(strip[i], strip[j])
            min_dist = min(min_dist, dist)
            j += 1
    
    return min_dist

def min_distance_brute(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Example usage
if __name__ == "__main__":
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(closest_pair(points))