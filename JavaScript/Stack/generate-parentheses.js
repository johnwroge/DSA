/*

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 2, a solution set is:

[
  "(())",
  "()()"
]

Given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Given n = 0, a solution set is:

[
  ""
]

*/

//input: number
//output: array of strings

//requirements: open parens must be closed 

const generateParentheses = n => {

//create results array
const results = [];
//create helper function
const generate = (str, l, r) => {
  //base case: check if right is 0 -> 
  if (r === 0){
    //push into results array, return
    results.push(str)

  }
  //check if l > 0 -> call helper with r - 1
  if (l > 0)
    generate(str + '(', l - 1, r)
  if (l < r)
    generate(str + ')', l, r - 1)
}
//call helper passing in n
generate('', n, n)
//return result array
return results; 

  
};

module.exports = {generateParentheses};
