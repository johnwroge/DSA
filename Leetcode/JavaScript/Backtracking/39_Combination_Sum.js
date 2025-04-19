/*
39. Combination Sum
Medium
16K
320
Companies
Given an array of distinct integers candidates and a target integer target,
 return a list of all unique combinations of candidates where the chosen numbers 
 sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
*/


/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */



//  var combinationSum = function(candidates,target, index = 0, combo = [], combos = []) {
    
//     const baseCase = target < 0; 
//     if (baseCase) return combos;
    
//     const baseCase2 = target === 0; 
//     if (baseCase2){
//        return combos.push(combo.slice())
//     }
  

// for (let i = index; i < candidates.length; i++){
//     backTrack(candidates, target, i, combo, combos)

// }
// return combos; 
// };

// const backTrack = (candidates, target,i, combo, combos) => {
//     combo.push(candidates[i]);
//     combinationSum(candidates, target - candidates[i],i, combo, combos);
//     combo.pop()
// }

var combinationSum = function (candidates, target){

    const results = [];
    
    const dfs = (i, combo, t)=> {

        if (target === t){
            results.push(combo.slice())
            return;
        }

        if (t > target || i >= candidates.length){
            return; 
        }

        combo.push(candidates[i]);
        dfs(i, combo, t + candidates[i]);
        combo.pop()
        dfs(i + 1, combo, t)

    }

dfs(0,[],0)
return results;

}







console.log(combinationSum([2,3,6,7],  7))