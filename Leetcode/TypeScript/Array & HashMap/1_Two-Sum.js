/*
1. 
  Given an array of numbers and a target number,
  return true if two of the numbers in the array add up to the target.
  Otherwise, return false.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.
  The straightforward way to solve this problem would take O(n²)time. Is it possible to do this in O(n) time? 

  Example:

  const nums = [2, 5, 11, 15]
  twoSum(num, 7) -> true
  Rational:  nums[0] + nums[1] = 2 + 5 = 7,

  twoSum(nums, 9) -> false
  Rational: No elements inside the array sum up to the target number
*/

const twoSum = (arr, target) => {
  //create a hash map to store value and index
  const hash = {};
  //declare a potential value
  let potentialValue;
  //iterate over the arr storing the element and index in hash
  for (let i = 0; i < arr.length; i++) {
    hash[arr[i]] = i;
  }
  //iterate over the hash
  for (let key in hash) {
    //evaluate potential value as the target minus the current key
    potentialValue = target - key;
    //check if there is a key of this potential value
    if (hash[potentialValue]) return true;
    //if true, return true
  }
  //otherwise return false
  return false;
};

/*
Extension:
Given an array of numbers and a target number, 
return true if three of the numbers in the array add up to the target.
Otherwise, return false.

The straightforward way to solve this problem would take O(n³) time. Is it possible to do this in O(n²) time?

*/

const threeSum_brute_force = (arr, target) => {
  //iterate over the arr with index i, from i to length - 2
  for (let i = 0; i < arr.length - 2; i++) {
    //iterate over the arr with index j f}rom j to length - 1
    for (let j = i + 1; j < arr.length - 1; j++) {
      //iterate over the arr with index k from k to length
      for (let k = j + 1; j < arr.length; j++) {
        //check if arri, j, k sum to target, return true
        console.log(i, j, k);
        if (arr[i] + arr[j] + arr[k] === target) return true;
      }
    }
  }
  return false;
};

//using three pointers, doesn't taken duplicates into consideration

const threeSum_optimized = (arr, target) => {
  const sorted = arr.sort((a, b) => a - b);
  let right = arr.length - 1;
  for (let i = 0; i < arr.length - 2; i++) {
    let left = i + 1;
    while (left < right) {
      let temp = arr[i] + arr[left] + arr[right];
      if (temp === target) return true;
      else if (temp < target) left++;
      else right--;
    }
  }
  return false;
};

//takes duplicates and unique indices into consideration
var threeSum2 = function (nums) {
  const results = [];
  nums.sort((a, b) => a - b);
  let sum;
  let j;
  let k;
  for (let i = 0; i < nums.length; i++) {
    k = nums.length - 1;
    j = i + 1;
    while (j < k) {
      console.log(sum);
      sum = nums[i] + nums[j] + nums[k];
      if (sum > 0) {
        k--;
      } else if (sum < 0) {
        j++;
      } else {
        results.push([nums[i], nums[j], nums[k]]);
        break;
      }
    }
  }
  return results;
};

// console.log(threeSum([-1, 0, 1, 2, -1, -4]));

//module.exports = { twoSum, threeSum };
