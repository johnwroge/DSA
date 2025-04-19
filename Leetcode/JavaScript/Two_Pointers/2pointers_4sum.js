/*Given an array nums of n integers, return an array of all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

*/



 //[-2, -1, 0, 0, 1, 2], target = 0
//  var fourSum = function(nums, target) {
//     const sorted = nums.sort((a,b) => a - b)
//     //create a temp sum
//     let temp;
//     //create results array
//     const results = [];
//     //create a left1, right1, and right 2 pointer
//     let left1;
//     let right2 = nums.length - 1;
//     let right1 = right2 - 1;
//     //loop from 0 to length of the array
//     for (let i = 0; i < nums.length; i++){
//         //while left1 is less than right 1
//         left1 = i + 1;
//         while (left1 < right1 && i !== left1 && right1 !== right2){
//             console.log(i, left1, right1, right2)
//         //assign temp sum to add all these values together 
//             temp = nums[i] + nums[left1] + nums[right1] + nums[right2];
//         //check is the temp sum equal to the target, and if true, 
//         if (temp === target){
//             //put all elements into array and push array into results
//             results.push([nums[i], nums[left1], nums[right1], nums[right2]])
//             left1 += 1;
//             right2 -= 1;
//         }
//         //otherwise temp sum less than target
//         else if (temp < target){
//             //if true, increment the left 1
//             left1 += 1;
//         } 
//          //otherwise decrement right 1 pointer
//         else if (temp > target) {
//             right1 -= 1; 
//         } else {
//             break; 
//         }
       
//         }
//         right2--; 
//     }
//     //return the results array
// return results; 
// };



var fourSum = function (nums, target) {
    const sortedNums = nums.sort((a, b) => a - b);
    const res = [];
    const quad = [];

    const kSum = (k, start, target) => {
        if (k > 2) {
            for (let i = start; i < sortedNums.length; i++) {
                if (i !== start && sortedNums[i] === sortedNums[i - 1]) {
                    continue;
                }
                quad.push(sortedNums[i]);
                kSum(k - 1, i + 1, target - sortedNums[i]);
                quad.pop();
            }
        } else {
            let left = start;
            let right = sortedNums.length - 1;

            while (left < right) {
                const sum = sortedNums[left] + sortedNums[right];
                if (sum < target) {
                    left++;
                } else if (sum > target) {
                    right--;
                } else {
                    res.push(
                        quad.concat([sortedNums[left], sortedNums[right]])
                    );
                    left++;
                    while (
                        left < right &&
                        sortedNums[left] === sortedNums[left - 1]
                    ) {
                        left++;
                    }
                }
            }
        }
    };
    kSum(4, 0, target);
    return res;
};

//solution 2

var fourSum2 = function(nums, target) {
    let res = []
    nums.sort((a,b)=>a-b)

    for(let i =0; i< nums.length-3;i++){
        for(let j =i+1; j<nums.length-2;j++){
            let f = nums[i];
            let s = nums[j];
            let left = j+1;
            let right = nums.length-1;
            while(left<right){
                let sum = f + s + nums[left] + nums[right];
                if(sum < target) left++
                else if(sum > target) right--
                else {
                    res.push([f,s,nums[left],nums[right]]);
                    while(nums[left] == nums[left+1])left++
                    while(nums[right] == nums[right-1]) right--
                    left++
                    right--
                }
            }
            while(nums[j] == nums[j+1]) j++
        }
        while(nums[i] == nums[i+1]) i++
    }
    return res
};

console.log(fourSum([-2, -1, 0, 0, 1, 2], 0))

