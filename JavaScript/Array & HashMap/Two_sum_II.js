/*
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] 
and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

*/
// input: sorted array of nums
// output: array with two indices where elements add to target
var twoSum = function(numbers, target) {

    //edge case: if no numbers return -1
    if (!numbers) return -1;
    //edge case: if not target, return empty array
    
    //initialize a left pointer (0) and right pointer (length - 1)
    let left = 0, right = numbers.length - 1, temp = 0; 
    //create a temp sum variable intiialized to 0;

    //loop while left is less than right
    while (left < right){
        //reassign the temp sum to be the left value plus right
        temp = numbers[left] + numbers[right];
        //check if temp sum is greater than target
        if (temp > target){
            //decrement the right pointer 
            right--;
        }
        //otherwise check if temp sum is less than target
        else if (temp < target){
            //increment the left pointer
            left++;
        }
        //otherwise -> return an array with left and right pointers (indices)
        else {
            return [left + 1, right + 1]
        }
    }
    //otherwise  return -1
    return -1;
};

console.log(twoSum([2,7,11,15], 9))