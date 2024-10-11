/**
 * @param {number} n
 * @return {number}
 */

/*
2571. Minimum Operations to Reduce an Integer to 0
Medium
311
176
Companies
You are given a positive integer n, you can do the following operation any number of times:

Add or subtract a power of 2 from n.
Return the minimum number of operations to make n equal to 0.

A number x is power of 2 if x == 2i where i >= 0.

Example 1:

Input: n = 39
Output: 3
Explanation: We can do the following operations:
- Add 20 = 1 to n, so now n = 40.
- Subtract 23 = 8 from n, so now n = 32.
- Subtract 25 = 32 from n, so now n = 0.
It can be shown that 3 is the minimum number of operations we need 
to make n equal to 0.
Example 2:

Input: n = 54
Output: 3
Explanation: We can do the following operations:
- Add 21 = 2 to n, so now n = 56.
- Add 23 = 8 to n, so now n = 64.
- Subtract 26 = 64 from n, so now n = 0.
So the minimum number of operations is 3.
 

Constraints:

1 <= n <= 105
*/


//inputs: n: positive integer, 
//output: integer representing number of operations to make n equal to 0



function minOperations(n) {
    //initialize count variable
    let count = 0;
    //loop while n is not 0
    while (n !== 0){
        //get length of n in binary to string and subtract 1
        const exp = n.toString(2).length - 1;
        console.log(exp)
        //reassign n to be the minimum of either n minus 2 raised to the exp or 
        n = Math.min(n - 2**exp, 2**(exp+1) - n);
        count++;
    }
    return count;
};


// var minOperations = function(n) {
//     let count = 0;
//     while (n !== 0){
//         const exp = Math.floor(Math.log(n)/Math.log(2));
//         n = Math.min(n - 2**exp, 2**(exp+1) - n);
//         count++;
//     }
//     return count;
// };
console.log(minOperations(39))