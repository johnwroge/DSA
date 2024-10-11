/*
Given a rod of n inches and a table p of prices, determine the maximum revenue r of n by cutting
up the rod and selling the pieces


*/

const price = [0, 1, 5, 8, 9, 10, 17, 17, 20]

function cutRod(price, n) {
    const dp = new Array(n + 1).fill(0);
    
    for (let i = 1; i <= n; i++) {
      let maxPrice = -Infinity;
      
      for (let j = 1; j <= i; j++) {
        maxPrice = Math.max(maxPrice, price[j] + dp[i - j]);
      }
      
      dp[i] = maxPrice;
    }
    console.log(dp)
    return dp[n];
  }

console.log(cutRod(price, 8))