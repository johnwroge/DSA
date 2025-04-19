/*
371. Sum of Two Integers
Medium
3.3K
4.7K
Companies
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
*/

/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
// var getSum = function(a, b) {
//     let carry;
//     while (b !== 0){
//         carry = (a & b) << 1;
//         a = a ^ b;
//         b = carry;
//     } 
//     return a; 
// };

var getSum = (a,b) => {
    let carry;
    while(a !== 0){
        carry = a & b;
        b = a ^ b;
        a = carry << 1; 
    }
    return b; 
}