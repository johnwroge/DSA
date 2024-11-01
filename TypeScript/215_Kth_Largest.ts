/*
'''
215. Kth Largest Element in an Array
Solved
Medium
Topics
Companies
Given an integer array nums and an integer k, return the kth largest element
 in the array.

Note that it is the kth largest element in the sorted order,
 not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

'''
*/

import { MaxPriorityQueue } from "@datastructures-js/priority-queue";

var findKthLargest = function(nums: number[], k: number) {
  
  
    let maxPriorityQueue = new MaxPriorityQueue();
    
    // we need to add all elements to our mpq manually time-0(n) 
    nums.forEach((num: number) => maxPriorityQueue.enqueue(num))
    
    
    // keep  removing(pop) element from the top 
    while(k>1){
      maxPriorityQueue.dequeue()
      k--
    }
    
    // by default maxPriorityQueue.front() returns an objects {priority:5, element:5} 
    // priority will give same result.
    return maxPriorityQueue.front().element
    
  };

var findKthLargest = function(nums: number[], k: number) {
    let min = Math.min(...nums);
    let max = Math.max(...nums);
    let count: number[] = new Array(max - min + 1).fill(0);

    for (let n of nums){
        count[n - min] += 1;
    }

    let remain: number = k;
    for (let i = count.length - 1; i >= 0; i--){
        remain -= count[i];
        if (remain <= 0){
            return i + min
        }
    }

    return -1;
};