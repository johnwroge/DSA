/*
739. Daily Temperatures
Medium
10.6K
237
Companies
Given an array of integers temperatures represents the daily temperatures, return an array 
answer such that answer[i] is the number of days you have to wait after the ith day to get 
a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100


*/

/*
imput: array of integers
output: array of integers
*/

// var dailyTemperatures = function(T) {
//    let stack = [];
//    let result = new Array(T.length).fill(0);
//     for(let i=0; i < T.length; i++){
//         while(stack.length && T[i] > T[stack[stack.length-1]]){
//             let temp = stack.pop();
//             result[temp] = i-temp;
//         }
//         stack.push(i)
//     }
//     return result;
// };





var dailyTemperatures = function(T) {
    //create a stack 
   let stack = [];
   //create an answer array of length of t filled with 0
   let result = new Array(T.length).fill(0); 
   //loop from end of T array to beginning
    for (let i = T.length - 1; i >= 0; i--){
        //while there is length in the stack and the current element is greater than or equal to 
        //the element in T at the index corresponding to element at the last position in the stack
            //if true, pop item off stacl
        while(stack.length && T[i] >= T[stack[stack.length - 1]]){
         stack.pop();
        }
        //if there are still elements in stack
            //reassing the element at current index in result array to be the 
            //last elemenent in the stack minus the current index
        if(stack.length){
            let temp = stack[stack.length - 1];
            result[i] = temp - i;   
        }
        //push the element in the stack
        stack.push(i)
    }
    //return the results array
    return result;
};