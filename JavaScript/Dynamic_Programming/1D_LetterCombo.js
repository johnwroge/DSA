/**
 * @param {string} digits
 * @return {string[]}
 */
//  var letterCombinations = function(digits) {
//     const result = [];
//     if (!digits) {
//         return result;
//     }
//     const mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];
//     const combination = new Array(digits.length).fill('');
//     backtrack(result, mapping, combination, digits, 0);
//     return result;
// };

// function backtrack(result, mapping, combination, digits, index) {
//     if (index === digits.length) {
//         result.push(combination.join(''));
//     } else {
//         const letters = mapping[digits.charAt(index)];
       
//         for (const letter of letters) {
//             combination[index] = letter;
//             backtrack(result, mapping, combination, digits, index + 1);
//         }
//     }
// }

/*  */

var letterCombinations = function(digits) {

    const results = [];
    const candidates = 
    {
        0:"",
        1:"",
        2:"abc",
        3:"def",
        4:"ghi",
        5:"jkl",
        6:"mno",
        7:"pqrs",
        8:"tuv",
        9:"wxyz"
    }
   
    
    const backtrack = function (index, string){

        if (string.length === digits.length){
            results.push(string);
            return;
        }
        
        const letter = digits.charAt(index)
    
        for (let char of candidates[letter]){ 
            backtrack(index + 1, string + char)
        }
    
    }
    if (digits.length){
        backtrack(0,"")
    }
    return results; 
}
    
    

console.log(letterCombinations("23"))