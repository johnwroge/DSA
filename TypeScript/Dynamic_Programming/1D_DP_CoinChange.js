/*
You are given an integer array coins representing coins of different
 denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
 If that amount of money cannot be made up by any combination of 
 the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
*/


var coinChange = function(coins, amount) {
    //create current index
    let idx;
    //create current amt
    let current; 
    //create a table wih length if amount + 1, filled with Infinity
    let table = new Array(amount + 1).fill(Infinity);
    //iterate over the coins 
    //fill table with amt at 
    table[0] = 0;
    for (let coin of coins){
        //for each table index 
        for (let i = 0; i < table.length; i++){
            //create conditional checking if coin is less than or equal to i
            if (coin <= i){
        //calculate the current index (i - coin)
            idx = i - coin;
        //create a potential amount that is element at current index + 1
            current = table[idx] + 1; 
        //assign the element at the idx in the table to the min of either the potamt or the current             amt
            table[i] = Math.min(current, table[i]);
            }
            
    ``}
    }
    //return a conditional testing if the coins at the length - 1 is infinity,
        //if true, return -1
        //if false, return the element at the table [length - 1]
    return table[table.length - 1] === Infinity ? -1 : table[table.length - 1];
};

//soln2

const coinSum = (coins, amount) => {

    const ways = new Array(amount + 1).fill(Infinity);
    ways[0] = 0;

    for (coin of coins){
        for (let n = coin; n < ways.length; n++){
            ways[n] = Math.min(ways[n], 1 + ways[n - coin]);
        }
    }
return ways[n] === Infinity ? -1 : ways[amount];
}

//recursive solution
var coinChange2 = function(coins, amount) { 
    let result = countCoinChange(coins, amount)
    return result === Infinity ? -1 : result
};

const countCoinChange2 = (coins, amount, memo={}) => {
    if(amount === 0) return 0
    if(amount < 0) return Infinity
    if(memo[amount] !== undefined) return memo[amount]

    let min = Infinity 

    for(let coin of coins) {
        const restAmount = amount - coin 
        min = Math.min(countCoinChange(coins, restAmount, memo) + 1, min) 
    }

    memo[amount] = min
    return memo[amount] 
}
