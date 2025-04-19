/*
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
 the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
 it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

*/

function houseRobberRecursion(arr){
    function stealFromhouse(index){
        if (index >= arr.length) return 0;
        console.log(arr[index])
        return Math.max(arr[index] + stealFromhouse(index + 2), stealFromhouse(index + 1))
    }
return stealFromhouse(0);
}


console.log(houseRobberRecursion([2,1,1,2]))







//approach dynamic programming

const houseRobber = (nums) => {
    //create a rob1 initialized to 0
    let rob1 = 0;
    //create a rob2 initialized to 0
    let rob2 = 0;
    //iterate over nums
    for (let i = 0; i < nums.length; i++){
        //create a temp variable and assign to maximum of either nums[i] + rob2, or rob1
        let current = Math.max(nums[i] + rob1, rob2)
        //reassign max 1 to be max 2
        rob1 = rob2;
        //reassign max2 to be temp
        rob2 = current;
    }
//return max 2
return rob2; 
}
// console.log(houseRobber([2,1,1,2]))
/*
current: 

*/