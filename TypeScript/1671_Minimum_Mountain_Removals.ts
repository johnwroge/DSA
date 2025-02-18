/*
1671. Minimum Number of Removals to Make Mountain Array

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to
 make nums​​​ a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any
 elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making
 the array nums = [1,5,6,3,1].
 

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.

To calculate the number of elements to remove:

On the left side of the peak, there are i + 1 elements from nums[0] to nums[i]. Therefore, the number of elements to remove on the left side is i + 1 - L1.
On the right side, there are N - i elements from nums[i] to nums[N - 1]. The number of elements to remove on the right side is N - i - L2.
Thus, the total number of elements to remove for a given peak at index i is:

removals=(i + 1 − L1) + (N − i − L2) = N + 1 − L1 − L2
*/

function minimumMountainRemovals(nums: number[]): number {
    const N = nums.length;

    const lis_length: number[] = new Array(N).fill(1);
    const lds_length: number[] = new Array(N).fill(1);

    // Calculate the length of longest increasing subsequence that ends at i.
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < i; j++) {
        if (nums[i] > nums[j]) {
          lis_length[i] = Math.max(lis_length[i], lis_length[j] + 1);
        }
      }
    }

    // Calculate the length of longest decreasing subsequence that starts at i.
    for (let i = N - 1; i >= 0; i--) {
      for (let j = i + 1; j < N; j++) {
        if (nums[i] > nums[j]) {
          lds_length[i] = Math.max(lds_length[i], lds_length[j] + 1);
        }
      }
    }

    let min_removals = Infinity;
    for (let i = 0; i < N; i++) {
      if (lis_length[i] > 1 && lds_length[i] > 1) {
        min_removals = Math.min(min_removals, N - lis_length[i] - lds_length[i] + 1);
      }
    }

    return min_removals;
  }