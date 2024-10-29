/*
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

 

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
Example 3:

Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.
 
*/


var calPoints = function(operations) {
    
    //create a stack
    const stack = [];
    //iterate over operations
    for (let i = 0; i < operations.length; i++){
        //if the current val is an integer, push into stack
        //else if the current character is a +, 
             if (operations[i] === "+"){
            //create a variable to store the previous two values in stack added together 
            let value = stack[stack.length - 1] + stack[stack.length - 2];
            //push variable into stack
            stack.push(value);
        }
        //else if the current character is a D
        else if (operations[i] === "D"){
            //push the last score * 2 into the stack
            stack.push(stack[stack.length - 1] * 2)
        }
        //else if the current character is a C
        else if (operations[i] === "C"){
            //remove the last score in the stack
            stack.pop()
        }
        else if (typeof Number(operations[i]) === 'number'){
            stack.push(Number(operations[i]))
        }
    }
console.log(stack)
//return a sum of all the values in the stack
return stack.reduce((acc,curr) => {
    return acc + curr; 
},0)

};

console.log(calPoints(["1","C"]))