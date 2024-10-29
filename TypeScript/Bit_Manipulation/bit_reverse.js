/*
190. Reverse Bits
Easy
4.1K
1.1K
Companies
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned 
integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned 
integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Constraints:

The input must be a binary string of length 32
 

Follow up: If this function is called many times, how would you optimize it?
*/

/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
//  var reverseBits = function(n) {
//      //convert the number to base2 then stringify, split, and reverse 
//     let reversedArray = n.toString(2).split("").reverse()
//     //the converted number may not be 32 digits so pad the end 
//     while(reversedArray.length <32){ reversedArray.push('0')}
//     //join the string, then convert to Integer from base 2
//     return  parseInt(reversedArray.join(""),2) 

//  };

// var reverseBits = function(n) {
//   var s = '';
//   var count = 0;
//   var index = 31;
//   while (n > 0) {
//     if (n % 2 !== 0) count += Math.pow(2, index);
//     index--;
//     n = Math.floor(n / 2);
//   }
//   return count;
// };



var reverseBits = function (n, bit = 0) {
    for (let i = 0; i < 32; i++) {
        bit <<= 1;      // Double * 2
        bit |= (n & 1); // Flip
        n >>=  1;           // Reduce * 0.5
    }

    return bit >>> 0;
};
