/*
541

Given a string s and an integer k, reverse the first k characters for every 2k characters
 counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k 
but greater than or equal to k characters, then reverse the first k characters and leave
 the other as original.


Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"

*/

/*
Strings are not mutable in python, so the best way to do this is convert the string to
a list and then perform the operations needed. 
*/

function reverseStr(s: string, k: number): string {
    const list_string: string[] = s.split("");
  
    for (let i = 0; i < list_string.length; i += 2 * k) {
      const chunk = list_string.slice(i, i + k).reverse();
      list_string.splice(i, k, ...chunk);
    }
  
    return list_string.join("");
  }

console.log(reverseStr("abcd", 2));
