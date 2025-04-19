/*
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

*/


var climbStairs = function(k, cache = {}) {     
            if (cache[k]) return cache[k];
            //base case: if current n is 1 return 1
            if (k === 1) return 1;
            //base case: if current n is 2 return 2
            if (k === 2) return 2; 
            //check if key exists, if yes return value
            //otherwise assign key in the cache to be eval result 
           return cache[k] = climbStairs(k - 1, cache) + climbStairs(k - 2, cache)
            //of call dfs with n + 1 and n + 2
    };
    
    
    var climbStairs = function(n) {     
        const cache = {1: 1, 2: 2};
        for (let i = 3; i <= n; i++){
            cache[i] = cache[i - 1] + cache[i - 2];
        }
    return cache[n];
    };