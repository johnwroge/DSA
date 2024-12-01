
'''
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103
'''

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = dict()
        for n in arr:
            if n in seen:
                return True
            seen[n * 0.5] = True
            seen[n * 2] = True
        return False


# Brute Force

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Step 1: Iterate through all pairs of indices
        for i in range(len(arr)):
            for j in range(len(arr)):
                # Step 2: Check the conditions
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        # No valid pair found
        return False

# Using a Set

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            # Check if 2 * num or num / 2 exists in the set
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add the current number to the set
            seen.add(num)
        # No valid pair found
        return False

# Using Binary Search

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Step 1: Sort the array
        arr.sort()

        for i in range(len(arr)):
            # Step 2: Calculate the target (double of current number)
            target = 2 * arr[i]
            # Step 3: Custom binary search for the target
            index = self._custom_binary_search(arr, target)
            # If the target exists and is not the same index
            if index >= 0 and index != i:
                return True
        # No valid pair found
        return False

    def _custom_binary_search(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            # Avoid potential overflow
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # Target not found